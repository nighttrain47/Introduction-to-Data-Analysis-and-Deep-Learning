# -*- coding: utf-8 -*-
"""
Phần 1 - Câu 1: Sắp xếp dữ liệu điểm DH1 theo thứ tự tăng dần
"""

import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Sắp xếp dữ liệu theo DH1 tăng dần
df_sorted = df.sort_values(by='DH1', ascending=True)

# Hiển thị kết quả
print("="*60)
print("DỮ LIỆU ĐIỂM DH1 ĐƯỢC SẮP XẾP TĂNG DẦN")
print("="*60)
print(df_sorted[['STT', 'DH1']].to_string(index=False))
print("\n" + "="*60)
print(f"Tổng số bản ghi: {len(df_sorted)}")
print(f"Giá trị DH1 nhỏ nhất: {df_sorted['DH1'].min()}")
print(f"Giá trị DH1 lớn nhất: {df_sorted['DH1'].max()}")
