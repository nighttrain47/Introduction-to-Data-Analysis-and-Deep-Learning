# Vấn đề 11: Xử lý Missing PulseRate
# Xử lý dữ liệu thiếu trên biến huyết áp với các phương pháp ưu tiên

import pandas as pd
import numpy as np
import re

# ============== CHUẨN BỊ DỮ LIỆU ==============
# Đọc file CSV và thêm header
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')

# Tách Name
name_split = df['Name'].str.split(' ', n=1, expand=True)
df['Firstname'] = name_split[0]
df['Lastname'] = name_split[1]

# Chuẩn hóa Weight
def convert_weight_to_kg(weight_str):
    if pd.isna(weight_str) or weight_str == '':
        return None
    weight_str = str(weight_str).strip().lower()
    number_match = re.search(r'[\d.]+', weight_str)
    if not number_match:
        return None
    value = float(number_match.group())
    if 'lbs' in weight_str or 'lb' in weight_str:
        return round(value * 0.453592, 2)
    return round(value, 2)

df['Weight'] = df['Weight'].apply(convert_weight_to_kg)
df = df.dropna(how='all')

# Phân rã cột huyết áp (melt)
pulse_columns = {
    'm0006': {'Sex': 'Male', 'Time': '00-06'},
    'm0612': {'Sex': 'Male', 'Time': '06-12'},
    'm1218': {'Sex': 'Male', 'Time': '12-18'},
    'f0006': {'Sex': 'Female', 'Time': '00-06'},
    'f0612': {'Sex': 'Female', 'Time': '06-12'},
    'f1218': {'Sex': 'Female', 'Time': '12-18'}
}

id_vars = ['ID', 'Firstname', 'Lastname', 'Age', 'Weight']
value_vars = list(pulse_columns.keys())

df_melted = df.melt(
    id_vars=id_vars,
    value_vars=value_vars,
    var_name='Original_Column',
    value_name='PulseRate'
)

df_melted['Sex'] = df_melted['Original_Column'].apply(lambda x: pulse_columns[x]['Sex'])
df_melted['Time'] = df_melted['Original_Column'].apply(lambda x: pulse_columns[x]['Time'])
df_melted['PulseRate'] = pd.to_numeric(df_melted['PulseRate'], errors='coerce')
df_melted = df_melted.drop(columns=['Original_Column'])

# Sắp xếp theo ID và Time để xử lý theo thứ tự
time_order = {'00-06': 0, '06-12': 1, '12-18': 2}
df_melted['Time_Order'] = df_melted['Time'].map(time_order)
df_melted = df_melted.sort_values(['ID', 'Sex', 'Time_Order']).reset_index(drop=True)

print("=== THỐNG KÊ MISSING PULSERATE ===")
total_rows = len(df_melted)
missing_rows = df_melted['PulseRate'].isna().sum()
print(f"Tổng số dòng: {total_rows}")
print(f"Số dòng thiếu PulseRate: {missing_rows}")
print(f"Tỷ lệ thiếu: {missing_rows/total_rows*100:.2f}%")
print()

# ============== XỬ LÝ MISSING PULSERATE ==============
# Giá trị huyết áp ổn định trong y học (normall resting heart rate)
NORMAL_HEART_RATE = 72

def fill_missing_pulserate(df):
    """
    Xử lý missing PulseRate theo thứ tự ưu tiên:
    1. Trung bình liền trước + liền sau của người đó
    2. Trung bình 2 giá trị liền trước của người đó
    3. Trung bình 2 giá trị liền sau của người đó
    4. Trung bình các giá trị huyết áp của người đó
    5. Trung bình của nhóm giới tính
    6. Trung bình toàn bộ dữ liệu hoặc giá trị y học chuẩn
    """
    df = df.copy()
    
    # Tính các giá trị trung bình cần thiết
    overall_mean = df['PulseRate'].mean()
    sex_means = df.groupby('Sex')['PulseRate'].mean().to_dict()
    
    for idx in df.index:
        if pd.isna(df.loc[idx, 'PulseRate']):
            person_id = df.loc[idx, 'ID']
            person_sex = df.loc[idx, 'Sex']
            
            # Lấy tất cả các dòng của người này với cùng giới tính
            person_mask = (df['ID'] == person_id) & (df['Sex'] == person_sex)
            person_data = df.loc[person_mask].copy()
            
            # Tìm vị trí trong danh sách của người này
            person_indices = person_data.index.tolist()
            pos = person_indices.index(idx)
            
            filled = False
            
            # Phương pháp 1: Trung bình liền trước + liền sau
            if pos > 0 and pos < len(person_indices) - 1:
                prev_idx = person_indices[pos - 1]
                next_idx = person_indices[pos + 1]
                prev_val = df.loc[prev_idx, 'PulseRate']
                next_val = df.loc[next_idx, 'PulseRate']
                if pd.notna(prev_val) and pd.notna(next_val):
                    df.loc[idx, 'PulseRate'] = (prev_val + next_val) / 2
                    filled = True
                    print(f"ID {person_id}: Điền bằng TB liền trước + sau = {df.loc[idx, 'PulseRate']:.2f}")
            
            # Phương pháp 2: Trung bình 2 giá trị liền trước
            if not filled and pos >= 2:
                prev1_idx = person_indices[pos - 1]
                prev2_idx = person_indices[pos - 2]
                prev1_val = df.loc[prev1_idx, 'PulseRate']
                prev2_val = df.loc[prev2_idx, 'PulseRate']
                if pd.notna(prev1_val) and pd.notna(prev2_val):
                    df.loc[idx, 'PulseRate'] = (prev1_val + prev2_val) / 2
                    filled = True
                    print(f"ID {person_id}: Điền bằng TB 2 giá trị liền trước = {df.loc[idx, 'PulseRate']:.2f}")
            
            # Phương pháp 3: Trung bình 2 giá trị liền sau
            if not filled and pos <= len(person_indices) - 3:
                next1_idx = person_indices[pos + 1]
                next2_idx = person_indices[pos + 2]
                next1_val = df.loc[next1_idx, 'PulseRate']
                next2_val = df.loc[next2_idx, 'PulseRate']
                if pd.notna(next1_val) and pd.notna(next2_val):
                    df.loc[idx, 'PulseRate'] = (next1_val + next2_val) / 2
                    filled = True
                    print(f"ID {person_id}: Điền bằng TB 2 giá trị liền sau = {df.loc[idx, 'PulseRate']:.2f}")
            
            # Phương pháp 4: Trung bình các giá trị của người đó
            if not filled:
                person_mean = person_data['PulseRate'].mean()
                if pd.notna(person_mean):
                    df.loc[idx, 'PulseRate'] = person_mean
                    filled = True
                    print(f"ID {person_id}: Điền bằng TB của người đó = {df.loc[idx, 'PulseRate']:.2f}")
            
            # Phương pháp 5: Trung bình của nhóm giới tính
            if not filled:
                if person_sex in sex_means and pd.notna(sex_means[person_sex]):
                    df.loc[idx, 'PulseRate'] = sex_means[person_sex]
                    filled = True
                    print(f"ID {person_id}: Điền bằng TB giới tính {person_sex} = {df.loc[idx, 'PulseRate']:.2f}")
            
            # Phương pháp 6: Trung bình toàn bộ hoặc giá trị y học
            if not filled:
                if pd.notna(overall_mean):
                    df.loc[idx, 'PulseRate'] = overall_mean
                    print(f"ID {person_id}: Điền bằng TB toàn bộ = {df.loc[idx, 'PulseRate']:.2f}")
                else:
                    df.loc[idx, 'PulseRate'] = NORMAL_HEART_RATE
                    print(f"ID {person_id}: Điền bằng giá trị y học = {NORMAL_HEART_RATE}")
    
    return df

print("=== XỬ LÝ MISSING PULSERATE ===")
df_filled = fill_missing_pulserate(df_melted)
print()

print("=== THỐNG KÊ SAU KHI XỬ LÝ ===")
missing_after = df_filled['PulseRate'].isna().sum()
print(f"Số dòng thiếu PulseRate: {missing_after}")
print()

print("=== DỮ LIỆU SAU KHI XỬ LÝ (10 dòng đầu) ===")
print(df_filled[['ID', 'Firstname', 'Lastname', 'Sex', 'Time', 'PulseRate']].head(10))
