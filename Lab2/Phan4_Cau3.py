# -*- coding: utf-8 -*-
"""
Phần 4 - Câu 3: Lập bảng tần số cho biến phanloai1
"""

import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Tạo biến phanloai1
def phan_loai_t1(diem):
    if diem < 5:
        return 'L'      # Kém
    elif diem < 7:
        return 'B'      # Trung bình
    elif diem < 9:
        return 'K'      # Khá
    else:
        return 'G'      # Giỏi

df['phanloai1'] = df['T1'].apply(phan_loai_t1)

print("="*60)
print("BẢNG TẦN SỐ CHO BIẾN phanloai1")
print("="*60)

# Tần số theo thứ tự: L, B, K, G
order = ['L', 'B', 'K', 'G']
freq = df['phanloai1'].value_counts().reindex(order, fill_value=0)

# Tần suất
freq_percent = (freq / freq.sum() * 100).round(2)

# Tần số tích lũy
freq_cumsum = freq.cumsum()

# Tần suất tích lũy
freq_percent_cumsum = freq_percent.cumsum()

# Tạo bảng
freq_table = pd.DataFrame({
    'Phân loại': order,
    'Mô tả': ['Kém (0-5)', 'Trung bình (5-7)', 'Khá (7-9)', 'Giỏi (9+)'],
    'Tần số': freq.values,
    'Tần suất (%)': freq_percent.values,
    'Tần số tích lũy': freq_cumsum.values,
    'Tần suất tích lũy (%)': freq_percent_cumsum.values
})

print(freq_table.to_string(index=False))
print(f"\nTổng số: {freq.sum()}")
