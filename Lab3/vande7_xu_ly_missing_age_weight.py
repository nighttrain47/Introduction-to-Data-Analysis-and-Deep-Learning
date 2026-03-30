# Vấn đề 7: Xử lý Missing Values cho Age và Weight
# Thống kê và xử lý dữ liệu thiếu

import pandas as pd
import re

# Đọc file CSV và thêm header
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')

# Chuẩn hóa Weight về kg
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

# Xóa dòng rỗng hoàn toàn
df = df.dropna(how='all')

print("=== THỐNG KÊ MISSING VALUES ===")
print(f"\nAge - Số lượng thiếu: {df['Age'].isna().sum()}")
print(f"Age - Tỷ lệ thiếu: {df['Age'].isna().sum() / len(df) * 100:.2f}%")
print(f"\nWeight - Số lượng thiếu: {df['Weight'].isna().sum()}")
print(f"Weight - Tỷ lệ thiếu: {df['Weight'].isna().sum() / len(df) * 100:.2f}%")
print()

print("=== DỮ LIỆU TRƯỚC KHI XỬ LÝ ===")
print(df[['ID', 'Name', 'Age', 'Weight']])
print()

# Tính giá trị trung bình của Age
age_mean = df['Age'].mean()
print(f"Giá trị trung bình Age: {age_mean:.2f}")

# Xử lý theo yêu cầu:
# - Nếu thiếu Age nhưng có Weight -> điền Age = mean
# - Nếu thiếu Weight nhưng có Age -> giữ nguyên Weight (hoặc có thể điền)
# - Nếu thiếu cả 2 -> xóa dòng

# Đánh dấu các dòng thiếu cả Age và Weight
both_missing = df['Age'].isna() & df['Weight'].isna()
print(f"\nSố dòng thiếu cả Age và Weight: {both_missing.sum()}")
print(df[both_missing][['ID', 'Name', 'Age', 'Weight']])

# Điền Age = mean cho các dòng thiếu Age nhưng có Weight
only_age_missing = df['Age'].isna() & df['Weight'].notna()
df.loc[only_age_missing, 'Age'] = round(age_mean, 0)
print(f"\nĐã điền Age = {round(age_mean, 0)} cho {only_age_missing.sum()} dòng")

# Xóa các dòng thiếu cả Age và Weight
df_cleaned = df[~both_missing].copy()

print("\n=== DỮ LIỆU SAU KHI XỬ LÝ ===")
print(f"Số dòng còn lại: {len(df_cleaned)}")
print(df_cleaned[['ID', 'Name', 'Age', 'Weight']])
print()

print("=== KIỂM TRA MISSING VALUES SAU XỬ LÝ ===")
print(f"Age - Số lượng thiếu: {df_cleaned['Age'].isna().sum()}")
print(f"Weight - Số lượng thiếu: {df_cleaned['Weight'].isna().sum()}")
