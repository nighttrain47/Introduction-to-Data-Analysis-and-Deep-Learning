# -*- coding: utf-8 -*-
"""
CÂU 7: TẠO CÁC BIẾN TBM1, TBM2, TBM3
- Công thức: TBM = (T*2 + L + H + S + V*2 + X + D + N) / 10
"""

import pandas as pd

print("=" * 80)
print("CÂU 7: TẠO CÁC BIẾN TBM1, TBM2, TBM3")
print("=" * 80)

# Đọc dữ liệu đã xử lý missing values
file_path = r"DuLieu\dulieuxettuyendaihoc.csv"
df = pd.read_csv(file_path)

# Xử lý missing values trước
df['DT'] = df['DT'].fillna(0)
non_score_cols = ['STT', 'GT', 'DT', 'KV', 'KT']
score_cols = [col for col in df.columns if col not in non_score_cols]
for col in score_cols:
    df[col] = df[col].fillna(df[col].mean())

print("""
Công thức: TBM = (T*2 + L + H + S + V*2 + X + D + N) / 10
""")

# Lớp 10 (suffix 1)
df['TBM1'] = (df['T1']*2 + df['L1'] + df['H1'] + df['S1'] + 
              df['V1']*2 + df['X1'] + df['D1'] + df['N1']) / 10

# Lớp 11 (suffix 2)
df['TBM2'] = (df['T2']*2 + df['L2'] + df['H2'] + df['S2'] + 
              df['V2']*2 + df['X2'] + df['D2'] + df['N2']) / 10

# Lớp 12 (suffix 6 trong file dữ liệu)
df['TBM3'] = (df['T6']*2 + df['L6'] + df['H6'] + df['S6'] + 
              df['V6']*2 + df['X6'] + df['D6'] + df['N6']) / 10

print("--- Thống kê TBM1, TBM2, TBM3 ---")
print(df[['TBM1', 'TBM2', 'TBM3']].describe())

print("\n--- 10 dòng đầu tiên của TBM ---")
print(df[['STT', 'TBM1', 'TBM2', 'TBM3']].head(10))

# Lưu kết quả tạm
df.to_csv(r"DuLieu\temp_cau7.csv", index=False)
print("\nĐã lưu kết quả tạm vào temp_cau7.csv")
