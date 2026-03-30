# Vấn đề 12: Rút gọn dữ liệu, reindex và lưu file
# Tổng hợp tất cả các bước xử lý và lưu kết quả

import pandas as pd
import numpy as np
import re
import unicodedata

# ============== BƯỚC 1: ĐỌC DỮ LIỆU VÀ THÊM HEADER ==============
print("=" * 60)
print("BƯỚC 1: Đọc dữ liệu và thêm header")
print("=" * 60)

column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')
print(f"Số dòng ban đầu: {len(df)}")

# ============== BƯỚC 2: TÁCH TÊN ==============
print("\n" + "=" * 60)
print("BƯỚC 2: Tách Name thành Firstname và Lastname")
print("=" * 60)

name_split = df['Name'].str.split(' ', n=1, expand=True)
df['Firstname'] = name_split[0]
df['Lastname'] = name_split[1]

# ============== BƯỚC 3: CHUẨN HÓA WEIGHT ==============
print("\n" + "=" * 60)
print("BƯỚC 3: Chuẩn hóa Weight về kg")
print("=" * 60)

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

# ============== BƯỚC 4: XÓA DÒNG RỖNG ==============
print("\n" + "=" * 60)
print("BƯỚC 4: Xóa dòng rỗng")
print("=" * 60)

before_count = len(df)
df = df.dropna(how='all')
print(f"Đã xóa {before_count - len(df)} dòng rỗng")

# ============== BƯỚC 5: XÓA DÒNG TRÙNG LẶP ==============
print("\n" + "=" * 60)
print("BƯỚC 5: Xóa dòng trùng lặp")
print("=" * 60)

cols_to_check = ['Firstname', 'Lastname', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
before_count = len(df)
df = df.drop_duplicates(subset=cols_to_check, keep='first')
print(f"Đã xóa {before_count - len(df)} dòng trùng lặp")

# ============== BƯỚC 6: XỬ LÝ NON-ASCII ==============
print("\n" + "=" * 60)
print("BƯỚC 6: Xử lý ký tự non-ASCII")
print("=" * 60)

def normalize_ascii(text):
    if pd.isna(text):
        return text
    normalized = unicodedata.normalize('NFD', str(text))
    return ''.join(char for char in normalized if unicodedata.category(char) != 'Mn')

df['Firstname'] = df['Firstname'].apply(normalize_ascii)
df['Lastname'] = df['Lastname'].apply(normalize_ascii)
print("Đã chuẩn hóa ký tự non-ASCII")

# ============== BƯỚC 7: XỬ LÝ MISSING AGE/WEIGHT ==============
print("\n" + "=" * 60)
print("BƯỚC 7: Xử lý Missing Age và Weight")
print("=" * 60)

age_mean = df['Age'].mean()
print(f"Trung bình Age: {age_mean:.2f}")

# Điền Age = mean nếu thiếu Age nhưng có Weight
only_age_missing = df['Age'].isna() & df['Weight'].notna()
df.loc[only_age_missing, 'Age'] = round(age_mean, 0)
print(f"Đã điền Age cho {only_age_missing.sum()} dòng")

# Xóa dòng thiếu cả Age và Weight
both_missing = df['Age'].isna() & df['Weight'].isna()
before_count = len(df)
df = df[~both_missing]
print(f"Đã xóa {before_count - len(df)} dòng thiếu cả Age và Weight")

# ============== BƯỚC 8: PHÂN RÃ CỘT ==============
print("\n" + "=" * 60)
print("BƯỚC 8: Phân rã cột huyết áp")
print("=" * 60)

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

print(f"Số dòng sau khi melt: {len(df_melted)}")

# ============== BƯỚC 11: XỬ LÝ MISSING PULSERATE ==============
print("\n" + "=" * 60)
print("BƯỚC 11: Xử lý Missing PulseRate")
print("=" * 60)

NORMAL_HEART_RATE = 72
time_order = {'00-06': 0, '06-12': 1, '12-18': 2}
df_melted['Time_Order'] = df_melted['Time'].map(time_order)
df_melted = df_melted.sort_values(['ID', 'Sex', 'Time_Order']).reset_index(drop=True)

overall_mean = df_melted['PulseRate'].mean()
sex_means = df_melted.groupby('Sex')['PulseRate'].mean().to_dict()

missing_before = df_melted['PulseRate'].isna().sum()
print(f"Số dòng thiếu PulseRate trước xử lý: {missing_before}")

for idx in df_melted.index:
    if pd.isna(df_melted.loc[idx, 'PulseRate']):
        person_id = df_melted.loc[idx, 'ID']
        person_sex = df_melted.loc[idx, 'Sex']
        
        person_mask = (df_melted['ID'] == person_id) & (df_melted['Sex'] == person_sex)
        person_data = df_melted.loc[person_mask].copy()
        person_indices = person_data.index.tolist()
        pos = person_indices.index(idx)
        
        filled = False
        
        # Phương pháp 1-3: Trung bình xung quanh
        if not filled and pos > 0 and pos < len(person_indices) - 1:
            prev_val = df_melted.loc[person_indices[pos - 1], 'PulseRate']
            next_val = df_melted.loc[person_indices[pos + 1], 'PulseRate']
            if pd.notna(prev_val) and pd.notna(next_val):
                df_melted.loc[idx, 'PulseRate'] = (prev_val + next_val) / 2
                filled = True
        
        if not filled and pos >= 2:
            prev1 = df_melted.loc[person_indices[pos - 1], 'PulseRate']
            prev2 = df_melted.loc[person_indices[pos - 2], 'PulseRate']
            if pd.notna(prev1) and pd.notna(prev2):
                df_melted.loc[idx, 'PulseRate'] = (prev1 + prev2) / 2
                filled = True
        
        if not filled and pos <= len(person_indices) - 3:
            next1 = df_melted.loc[person_indices[pos + 1], 'PulseRate']
            next2 = df_melted.loc[person_indices[pos + 2], 'PulseRate']
            if pd.notna(next1) and pd.notna(next2):
                df_melted.loc[idx, 'PulseRate'] = (next1 + next2) / 2
                filled = True
        
        # Phương pháp 4: Trung bình của người đó
        if not filled:
            person_mean = person_data['PulseRate'].mean()
            if pd.notna(person_mean):
                df_melted.loc[idx, 'PulseRate'] = person_mean
                filled = True
        
        # Phương pháp 5: Trung bình giới tính
        if not filled and person_sex in sex_means:
            df_melted.loc[idx, 'PulseRate'] = sex_means[person_sex]
            filled = True
        
        # Phương pháp 6: Trung bình toàn bộ hoặc giá trị y học
        if not filled:
            df_melted.loc[idx, 'PulseRate'] = overall_mean if pd.notna(overall_mean) else NORMAL_HEART_RATE

missing_after = df_melted['PulseRate'].isna().sum()
print(f"Số dòng thiếu PulseRate sau xử lý: {missing_after}")

# ============== BƯỚC 12: RÚT GỌN VÀ LƯU FILE ==============
print("\n" + "=" * 60)
print("BƯỚC 12: Rút gọn và lưu file")
print("=" * 60)

# Lọc bỏ các dòng không có thông tin hữu ích
# (các dòng mà người đó không có dữ liệu đo tại giới tính/thời gian đó)
# Giữ lại các dòng có PulseRate
df_final = df_melted[df_melted['PulseRate'].notna()].copy()

# Xóa cột Time_Order (dùng để sắp xếp)
df_final = df_final.drop(columns=['Time_Order'])

# Reset index
df_final = df_final.reset_index(drop=True)

# Sắp xếp lại cột
df_final = df_final[['ID', 'Firstname', 'Lastname', 'Age', 'Weight', 'Sex', 'Time', 'PulseRate']]

# Làm tròn PulseRate
df_final['PulseRate'] = df_final['PulseRate'].round(2)

print(f"Số dòng cuối cùng: {len(df_final)}")
print()

print("=== DỮ LIỆU ĐÃ LÀM SẠCH ===")
print(df_final)
print()

# Lưu file
output_path = 'DuLieu/patient_heart_rate_clean.csv'
df_final.to_csv(output_path, index=False, encoding='utf-8')
print(f"Đã lưu file: {output_path}")

print("\n" + "=" * 60)
print("HOÀN THÀNH XỬ LÝ DỮ LIỆU!")
print("=" * 60)
