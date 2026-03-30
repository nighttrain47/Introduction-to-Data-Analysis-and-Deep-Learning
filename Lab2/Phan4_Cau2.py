# -*- coding: utf-8 -*-
"""
Phần 4 - Câu 2: Tạo biến phân loại (phanloai1) cho môn toán (T1)
- Từ 0 đến dưới 5 = kém (ký hiệu "L")
- Từ 5 đến dưới 7 = trung bình (ký hiệu "B")  
- Từ 7 đến dưới 9 = khá (ký hiệu "K")
- Từ 9 trở lên = giỏi (ký hiệu "G")
"""

import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

print("="*60)
print("TẠO BIẾN PHÂN LOẠI phanloai1 CHO MÔN TOÁN (T1)")
print("="*60)

# Tạo hàm phân loại theo đề bài
def phan_loai_t1(diem):
    if diem < 5:
        return 'L'      # Kém (Low)
    elif diem < 7:
        return 'B'      # Trung bình (Below average/Basic)
    elif diem < 9:
        return 'K'      # Khá
    else:
        return 'G'      # Giỏi (Good)

# Áp dụng hàm phân loại
df['phanloai1'] = df['T1'].apply(phan_loai_t1)

# Hiển thị kết quả
print("\n--- Phân loại T1 ---")
print("Điểm T1 -> Phân loại:")
print("  0 - dưới 5: Kém (L)")
print("  5 - dưới 7: Trung bình (B)")
print("  7 - dưới 9: Khá (K)")
print("  9 trở lên: Giỏi (G)")

print("\n--- Dữ liệu với biến phanloai1 ---")
print(df[['STT', 'T1', 'phanloai1']].head(20).to_string(index=False))

print("\n--- Tần số phân loại T1 ---")
order = ['L', 'B', 'K', 'G']
freq = df['phanloai1'].value_counts().reindex(order, fill_value=0)
print(freq)

# Lưu dữ liệu với biến mới
df.to_csv('DuLieu/processed_dulieuxettuyendaihoc_phanloai1.csv', index=False)
print("\nĐã lưu dữ liệu với biến phanloai1: DuLieu/processed_dulieuxettuyendaihoc_phanloai1.csv")
