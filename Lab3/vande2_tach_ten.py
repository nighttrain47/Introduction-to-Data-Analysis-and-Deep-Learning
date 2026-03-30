# Vấn đề 2: Tách cột Name thành Firstname và Lastname
# Cột Name chứa hỗn hợp Firstname và Lastname

import pandas as pd

# Đọc file CSV và thêm header
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df[['ID', 'Name']])
print()

# Tách cột Name thành Firstname và Lastname
# Sử dụng str.split() với expand=True để tạo DataFrame với 2 cột
name_split = df['Name'].str.split(' ', n=1, expand=True)
df['Firstname'] = name_split[0]
df['Lastname'] = name_split[1]

# Sắp xếp lại thứ tự cột
cols = ['ID', 'Firstname', 'Lastname'] + [col for col in df.columns if col not in ['ID', 'Name', 'Firstname', 'Lastname']]
df = df[cols]

print("=== DỮ LIỆU SAU KHI TÁCH TÊN ===")
print(df[['ID', 'Firstname', 'Lastname']])
print()

print("=== CẤU TRÚC DỮ LIỆU MỚI ===")
print(df.columns.tolist())
