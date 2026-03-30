# Vấn đề 8: Phân rã cột huyết áp
# Các cột m0006, m0612, m1218, f0006, f0612, f1218 chứa thông tin:
# - Giới tính (m: male, f: female)
# - Thời gian (00-06, 06-12, 12-18)
# - Giá trị huyết áp

import pandas as pd
import re

# Đọc file CSV và thêm header
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')

# Tách Name thành Firstname và Lastname
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

# Xóa dòng rỗng
df = df.dropna(how='all')

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df[['ID', 'Firstname', 'Lastname', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']])
print()

# Định nghĩa các cột huyết áp và thông tin tương ứng
pulse_columns = {
    'm0006': {'Sex': 'Male', 'Time': '00-06'},
    'm0612': {'Sex': 'Male', 'Time': '06-12'},
    'm1218': {'Sex': 'Male', 'Time': '12-18'},
    'f0006': {'Sex': 'Female', 'Time': '00-06'},
    'f0612': {'Sex': 'Female', 'Time': '06-12'},
    'f1218': {'Sex': 'Female', 'Time': '12-18'}
}

# Sử dụng melt để chuyển đổi từ wide format sang long format
id_vars = ['ID', 'Firstname', 'Lastname', 'Age', 'Weight']
value_vars = list(pulse_columns.keys())

df_melted = df.melt(
    id_vars=id_vars,
    value_vars=value_vars,
    var_name='Original_Column',
    value_name='PulseRate'
)

# Thêm cột Sex và Time dựa trên Original_Column
def extract_sex(col_name):
    return pulse_columns[col_name]['Sex']

def extract_time(col_name):
    return pulse_columns[col_name]['Time']

df_melted['Sex'] = df_melted['Original_Column'].apply(extract_sex)
df_melted['Time'] = df_melted['Original_Column'].apply(extract_time)

# Chuyển đổi PulseRate thành số, thay '-' bằng NaN
df_melted['PulseRate'] = pd.to_numeric(df_melted['PulseRate'], errors='coerce')

# Xóa cột Original_Column vì không cần nữa
df_melted = df_melted.drop(columns=['Original_Column'])

# Sắp xếp lại cột
df_melted = df_melted[['ID', 'Firstname', 'Lastname', 'Age', 'Weight', 'Sex', 'Time', 'PulseRate']]

# Lọc bỏ các dòng có PulseRate là NaN (nếu cần giữ thì comment dòng dưới)
# df_melted = df_melted.dropna(subset=['PulseRate'])

print("=== DỮ LIỆU SAU KHI PHÂN RÃ ===")
print(df_melted.head(20))
print()

print(f"=== THỐNG KÊ ===")
print(f"Số dòng: {len(df_melted)}")
print(f"Số dòng có PulseRate: {df_melted['PulseRate'].notna().sum()}")
print(f"Số dòng thiếu PulseRate: {df_melted['PulseRate'].isna().sum()}")
print()

print("=== PHÂN BỐ THEO GIỚI TÍNH ===")
print(df_melted.groupby('Sex')['PulseRate'].describe())
