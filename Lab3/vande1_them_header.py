# Vấn đề 1: Thêm Header cho file CSV
# File CSV ban đầu không có dòng tiêu đề

import pandas as pd

# Đọc file CSV không có header
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, on_bad_lines='warn')

print("=== DỮ LIỆU BAN ĐẦU (không có header) ===")
print(df)
print()

# Định nghĩa tên cột
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']

# Gán header cho DataFrame
df.columns = column_names

print("=== DỮ LIỆU SAU KHI THÊM HEADER ===")
print(df)
print()

print("=== THÔNG TIN CỘT ===")
print(df.dtypes)
