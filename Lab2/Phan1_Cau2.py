# -*- coding: utf-8 -*-
"""
Phần 1 - Câu 2: Sắp xếp dữ liệu điểm DH2 tăng dần theo nhóm giới tính
"""

import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Sắp xếp dữ liệu theo GT (giới tính) và DH2 tăng dần trong mỗi nhóm
df_sorted = df.sort_values(by=['GT', 'DH2'], ascending=[True, True])

# Hiển thị kết quả
print("="*60)
print("DỮ LIỆU ĐIỂM DH2 TĂNG DẦN THEO NHÓM GIỚI TÍNH")
print("="*60)

# Hiển thị theo từng nhóm giới tính
for gender in df_sorted['GT'].unique():
    gender_name = "Nữ" if gender == 'F' else "Nam"
    print(f"\n--- Giới tính: {gender_name} ({gender}) ---")
    group_data = df_sorted[df_sorted['GT'] == gender][['STT', 'GT', 'DH2']]
    print(group_data.to_string(index=False))
    print(f"Số lượng: {len(group_data)}")

print("\n" + "="*60)
print(f"Tổng số bản ghi: {len(df_sorted)}")
