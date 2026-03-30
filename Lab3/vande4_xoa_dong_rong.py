# Vấn đề 4: Xóa dòng dữ liệu rỗng
# Xuất hiện các dòng không có giá trị (NaN)

import pandas as pd

# Đọc file CSV và thêm header
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')

print("=== DỮ LIỆU BAN ĐẦU ===")
print(f"Số dòng: {len(df)}")
print(df)
print()

# Đếm số dòng rỗng hoàn toàn
empty_rows = df[df.isna().all(axis=1)]
print(f"=== SỐ DÒNG RỖNG HOÀN TOÀN: {len(empty_rows)} ===")
print(empty_rows)
print()

# Xác định các dòng gần như rỗng (chỉ có 1-2 giá trị)
mostly_empty = df[df.isna().sum(axis=1) >= len(df.columns) - 2]
print(f"=== CÁC DÒNG GẦN NHƯ RỖNG (>=8 NaN): {len(mostly_empty)} ===")
print(mostly_empty)
print()

# Xóa các dòng rỗng hoàn toàn
df_cleaned = df.dropna(how='all')

print("=== DỮ LIỆU SAU KHI XÓA DÒNG RỖNG ===")
print(f"Số dòng còn lại: {len(df_cleaned)}")
print(df_cleaned)
print()

# Có thể xóa thêm các dòng gần như rỗng (tùy theo yêu cầu nghiệp vụ)
# df_cleaned = df.dropna(thresh=3)  # Giữ lại dòng có ít nhất 3 giá trị không null
