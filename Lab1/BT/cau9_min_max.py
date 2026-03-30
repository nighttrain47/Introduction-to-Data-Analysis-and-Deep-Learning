# -*- coding: utf-8 -*-
"""
CÂU 9: TẠO CÁC BIẾN US_TBM1, US_TBM2, US_TBM3
- Chuyển đổi điểm từ thang 10 VN sang thang 4 Mỹ
- Sử dụng phương pháp Min-Max Normalization
"""

import pandas as pd

print("=" * 80)
print("CÂU 9: CHUYỂN ĐỔI ĐIỂM SANG THANG 4 (MIN-MAX NORMALIZATION)")
print("=" * 80)

# Đọc dữ liệu đã xử lý
file_path = r"DuLieu\dulieuxettuyendaihoc.csv"
df = pd.read_csv(file_path)

# Xử lý missing values
df['DT'] = df['DT'].fillna(0)
non_score_cols = ['STT', 'GT', 'DT', 'KV', 'KT']
score_cols = [col for col in df.columns if col not in non_score_cols]
for col in score_cols:
    df[col] = df[col].fillna(df[col].mean())

# Tạo TBM
df['TBM1'] = (df['T1']*2 + df['L1'] + df['H1'] + df['S1'] + 
              df['V1']*2 + df['X1'] + df['D1'] + df['N1']) / 10
df['TBM2'] = (df['T2']*2 + df['L2'] + df['H2'] + df['S2'] + 
              df['V2']*2 + df['X2'] + df['D2'] + df['N2']) / 10
df['TBM3'] = (df['T6']*2 + df['L6'] + df['H6'] + df['S6'] + 
              df['V6']*2 + df['X6'] + df['D6'] + df['N6']) / 10

print("""
Công thức Min-Max Normalization:
US_TBM = (TBM - min) / (max - min) * (new_max - new_min) + new_min

Với thang điểm 10 VN (0-10) sang thang điểm 4 Mỹ (0-4):
US_TBM = (TBM - 0) / (10 - 0) * (4 - 0) + 0 = TBM * 4 / 10 = TBM * 0.4
""")

# Min-Max Normalization từ thang 10 sang thang 4
def min_max_normalize(value, old_min=0, old_max=10, new_min=0, new_max=4):
    return (value - old_min) / (old_max - old_min) * (new_max - new_min) + new_min

df['US_TBM1'] = df['TBM1'].apply(min_max_normalize)
df['US_TBM2'] = df['TBM2'].apply(min_max_normalize)
df['US_TBM3'] = df['TBM3'].apply(min_max_normalize)

print("--- Thống kê US_TBM1, US_TBM2, US_TBM3 (thang điểm 4) ---")
print(df[['US_TBM1', 'US_TBM2', 'US_TBM3']].describe())

# Lưu kết quả tạm
df.to_csv(r"DuLieu\temp_cau9.csv", index=False)
print("\nĐã lưu kết quả tạm vào temp_cau9.csv")
