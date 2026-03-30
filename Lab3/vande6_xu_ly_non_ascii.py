# Vấn đề 6: Xử lý ký tự non-ASCII
# Xuất hiện dữ liệu bị ảnh hưởng bởi lỗi non-ASCII (ví dụ: Mickéy Mousé, Scööpy Doo)

import pandas as pd
import unicodedata

# Đọc file CSV và thêm header
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')

# Tách Name thành Firstname và Lastname
name_split = df['Name'].str.split(' ', n=1, expand=True)
df['Firstname'] = name_split[0]
df['Lastname'] = name_split[1]

print("=== TÊN BAN ĐẦU ===")
print(df[['ID', 'Firstname', 'Lastname']])
print()

def check_non_ascii(text):
    """Kiểm tra xem chuỗi có chứa ký tự non-ASCII không"""
    if pd.isna(text):
        return False
    return any(ord(char) > 127 for char in str(text))

def normalize_ascii(text):
    """
    Chuyển đổi ký tự non-ASCII sang ASCII
    Ví dụ: é -> e, ö -> o
    """
    if pd.isna(text):
        return text
    # NFD: phân tách ký tự có dấu thành ký tự gốc + dấu
    # Sau đó loại bỏ các dấu (category 'Mn' = Mark, Nonspacing)
    normalized = unicodedata.normalize('NFD', str(text))
    return ''.join(char for char in normalized if unicodedata.category(char) != 'Mn')

# Phát hiện các dòng có ký tự non-ASCII
print("=== PHÁT HIỆN KÝ TỰ NON-ASCII ===")
for idx, row in df.iterrows():
    if check_non_ascii(row['Firstname']) or check_non_ascii(row['Lastname']):
        print(f"ID {row['ID']}: {row['Firstname']} {row['Lastname']}")

print()

# Áp dụng chuẩn hóa
df['Firstname'] = df['Firstname'].apply(normalize_ascii)
df['Lastname'] = df['Lastname'].apply(normalize_ascii)

print("=== TÊN SAU KHI CHUẨN HÓA ===")
print(df[['ID', 'Firstname', 'Lastname']])
print()

# Kiểm tra lại
print("=== KIỂM TRA SAU KHI XỬ LÝ ===")
non_ascii_count = 0
for idx, row in df.iterrows():
    if check_non_ascii(row['Firstname']) or check_non_ascii(row['Lastname']):
        non_ascii_count += 1
        print(f"Còn non-ASCII: ID {row['ID']}: {row['Firstname']} {row['Lastname']}")

if non_ascii_count == 0:
    print("Không còn ký tự non-ASCII trong tên!")
