# Vấn đề 3: Chuẩn hóa đơn vị Weight về kg
# Weight có lẫn lộn đơn vị kgs và lbs

import pandas as pd
import re

# Đọc file CSV và thêm header
column_names = ['ID', 'Name', 'Age', 'Weight', 'm0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218']
df = pd.read_csv('DuLieu/patient_heart_rate.csv', header=None, names=column_names, on_bad_lines='warn')

print("=== WEIGHT BAN ĐẦU ===")
print(df[['ID', 'Name', 'Weight']])
print()

def convert_weight_to_kg(weight_str):
    """
    Chuyển đổi Weight về đơn vị kg
    - Nếu là lbs: chuyển sang kg (1 lbs = 0.453592 kg)
    - Nếu là kgs: giữ nguyên giá trị
    - Nếu là NaN hoặc rỗng: trả về NaN
    """
    if pd.isna(weight_str) or weight_str == '':
        return None
    
    weight_str = str(weight_str).strip().lower()
    
    # Tìm số trong chuỗi
    number_match = re.search(r'[\d.]+', weight_str)
    if not number_match:
        return None
    
    value = float(number_match.group())
    
    # Kiểm tra đơn vị
    if 'lbs' in weight_str or 'lb' in weight_str:
        # Chuyển từ lbs sang kg
        return round(value * 0.453592, 2)
    elif 'kgs' in weight_str or 'kg' in weight_str:
        # Đã là kg
        return round(value, 2)
    else:
        # Không có đơn vị, giả định là kg
        return round(value, 2)

# Áp dụng hàm chuyển đổi
df['Weight'] = df['Weight'].apply(convert_weight_to_kg)

print("=== WEIGHT SAU KHI CHUẨN HÓA (kg) ===")
print(df[['ID', 'Name', 'Weight']])
print()

print("=== THỐNG KÊ WEIGHT ===")
print(df['Weight'].describe())
