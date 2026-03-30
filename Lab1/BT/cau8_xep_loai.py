# -*- coding: utf-8 -*-
"""
CÂU 8: TẠO CÁC BIẾN XẾP LOẠI XL1, XL2, XL3
- Nhỏ hơn 5.0: Yếu (Y)
- Từ 5.0 đến dưới 6.5: Trung bình (TB)
- Từ 6.5 đến dưới 8.0: Khá (K)
- Từ 8.0 đến dưới 9.0: Giỏi (G)
- Từ 9.0 trở lên: Xuất sắc (XS)
"""

import pandas as pd

print("=" * 80)
print("CÂU 8: TẠO CÁC BIẾN XẾP LOẠI XL1, XL2, XL3")
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
Quy tắc xếp loại:
- Nhỏ hơn 5.0: Yếu (Y)
- Từ 5.0 đến dưới 6.5: Trung bình (TB)
- Từ 6.5 đến dưới 8.0: Khá (K)
- Từ 8.0 đến dưới 9.0: Giỏi (G)
- Từ 9.0 trở lên: Xuất sắc (XS)
""")

def xep_loai(diem):
    """Hàm xếp loại dựa trên điểm trung bình"""
    if diem < 5.0:
        return 'Y'
    elif diem < 6.5:
        return 'TB'
    elif diem < 8.0:
        return 'K'
    elif diem < 9.0:
        return 'G'
    else:
        return 'XS'

df['XL1'] = df['TBM1'].apply(xep_loai)
df['XL2'] = df['TBM2'].apply(xep_loai)
df['XL3'] = df['TBM3'].apply(xep_loai)

print("--- Phân bố xếp loại ---")
print("\nXếp loại lớp 10 (XL1):")
print(df['XL1'].value_counts().sort_index())

print("\nXếp loại lớp 11 (XL2):")
print(df['XL2'].value_counts().sort_index())

print("\nXếp loại lớp 12 (XL3):")
print(df['XL3'].value_counts().sort_index())

print("\n--- 10 dòng đầu tiên ---")
print(df[['STT', 'TBM1', 'XL1', 'TBM2', 'XL2', 'TBM3', 'XL3']].head(10))

# Lưu kết quả tạm
df.to_csv(r"DuLieu\temp_cau8.csv", index=False)
print("\nĐã lưu kết quả tạm vào temp_cau8.csv")
