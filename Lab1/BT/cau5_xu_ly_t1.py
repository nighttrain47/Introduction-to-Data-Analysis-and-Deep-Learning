# -*- coding: utf-8 -*-
"""
CÂU 5: THỐNG KÊ VÀ HIỆU CHỈNH DỮ LIỆU THIẾU CHO BIẾN T1
- Sử dụng phương pháp Mean
"""

import pandas as pd

print("=" * 80)
print("CÂU 5: XỬ LÝ DỮ LIỆU THIẾU CHO BIẾN T1 (PHƯƠNG PHÁP MEAN)")
print("=" * 80)

# Đọc dữ liệu
file_path = r"DuLieu\dulieuxettuyendaihoc.csv"
df = pd.read_csv(file_path)

print("\n--- Thống kê dữ liệu cột T1 trước khi xử lý ---")
print(f"Số giá trị thiếu (NaN): {df['T1'].isna().sum()}")
print(f"Giá trị trung bình (mean): {df['T1'].mean():.4f}")

# Bảng tần số
print("\n--- Bảng tần số cột T1 ---")
freq_t1 = df['T1'].value_counts(dropna=False).sort_index()
print(freq_t1)

# Tính giá trị trung bình
mean_t1 = df['T1'].mean()

# Thay thế dữ liệu thiếu bằng Mean
df['T1'] = df['T1'].fillna(mean_t1)

print("\n--- Sau khi thay thế dữ liệu thiếu bằng Mean ---")
print(f"Số giá trị thiếu (NaN): {df['T1'].isna().sum()}")

# Lưu kết quả tạm
df.to_csv(r"DuLieu\temp_cau5.csv", index=False)
print("\nĐã lưu kết quả tạm vào temp_cau5.csv")
