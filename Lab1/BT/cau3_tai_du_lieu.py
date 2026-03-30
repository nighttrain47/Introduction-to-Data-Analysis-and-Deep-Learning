# -*- coding: utf-8 -*-
"""
CÂU 3: TẢI DỮ LIỆU VÀ IN 10 DÒNG ĐẦU/CUỐI
"""

import pandas as pd

print("=" * 80)
print("CÂU 3: TẢI DỮ LIỆU VÀ IN 10 DÒNG ĐẦU/CUỐI")
print("=" * 80)

# Đọc dữ liệu từ file CSV
file_path = r"DuLieu\dulieuxettuyendaihoc.csv"
df = pd.read_csv(file_path)

print(f"\nThông tin dữ liệu: {len(df)} dòng x {len(df.columns)} cột")

print("\n--- 10 DÒNG ĐẦU TIÊN ---")
print(df.head(10))

print("\n--- 10 DÒNG CUỐI CÙNG ---")
print(df.tail(10))
