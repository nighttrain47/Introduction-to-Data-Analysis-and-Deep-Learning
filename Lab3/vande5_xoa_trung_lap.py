# Vấn đề 5: Xóa dòng trùng lặp
# Có nhiều dòng dữ liệu bị trùng lắp thông tin hoàn toàn

import pandas as pd

# Đọc file CSV và thêm header
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')

# Tách Name thành Firstname và Lastname
name_split = df['Name'].str.split(' ', n=1, expand=True)
df['Firstname'] = name_split[0]
df['Lastname'] = name_split[1]

print("=== DỮ LIỆU BAN ĐẦU ===")
print(f"Số dòng: {len(df)}")
print(df[['ID', 'Firstname', 'Lastname', 'Age', 'Weight']])
print()

# Xác định các cột để kiểm tra trùng lặp (không tính ID vì ID khác nhau)
cols_to_check = ['Firstname', 'Lastname', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']

# Tìm các dòng trùng lặp
duplicates = df[df.duplicated(subset=cols_to_check, keep=False)]
print(f"=== CÁC DÒNG TRÙNG LẶP: {len(duplicates)} ===")
print(duplicates[['ID', 'Firstname', 'Lastname', 'Age', 'Weight']])
print()

# Xóa các dòng trùng lặp, giữ lại dòng đầu tiên
df_no_duplicates = df.drop_duplicates(subset=cols_to_check, keep='first')

print("=== DỮ LIỆU SAU KHI XÓA TRÙNG LẶP ===")
print(f"Số dòng còn lại: {len(df_no_duplicates)}")
print(df_no_duplicates[['ID', 'Firstname', 'Lastname', 'Age', 'Weight']])
print()

# Lưu ý: Việc xóa trùng lặp phải dựa trên nghiệp vụ
# Ví dụ: Huey McDuck (ID 6) và (ID 9) có dữ liệu giống nhau -> giữ lại 1
