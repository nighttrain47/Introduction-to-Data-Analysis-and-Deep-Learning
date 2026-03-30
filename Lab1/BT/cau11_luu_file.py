# -*- coding: utf-8 -*-
"""
CÂU 11: LƯU TRỮ DỮ LIỆU XUỐNG Ổ ĐĨA
- File: processed_dulieuxettuyendaihoc.csv
- Thực hiện tất cả các bước xử lý từ câu 4-10
"""

import pandas as pd

print("=" * 80)
print("CÂU 11: LƯU DỮ LIỆU XUỐNG FILE")
print("=" * 80)

# Đọc dữ liệu gốc
file_path = r"DuLieu\dulieuxettuyendaihoc.csv"
df = pd.read_csv(file_path)

# ===== CÂU 4: Xử lý DT =====
df['DT'] = df['DT'].fillna(0)

# ===== CÂU 5 & 6: Xử lý missing values cho tất cả biến điểm =====
non_score_cols = ['STT', 'GT', 'DT', 'KV', 'KT']
score_cols = [col for col in df.columns if col not in non_score_cols]
for col in score_cols:
    df[col] = df[col].fillna(df[col].mean())

# ===== CÂU 7: Tạo TBM =====
df['TBM1'] = (df['T1']*2 + df['L1'] + df['H1'] + df['S1'] + 
              df['V1']*2 + df['X1'] + df['D1'] + df['N1']) / 10
df['TBM2'] = (df['T2']*2 + df['L2'] + df['H2'] + df['S2'] + 
              df['V2']*2 + df['X2'] + df['D2'] + df['N2']) / 10
df['TBM3'] = (df['T6']*2 + df['L6'] + df['H6'] + df['S6'] + 
              df['V6']*2 + df['X6'] + df['D6'] + df['N6']) / 10

# ===== CÂU 8: Tạo XL =====
def xep_loai(diem):
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

# ===== CÂU 9: Tạo US_TBM =====
def min_max_normalize(value, old_min=0, old_max=10, new_min=0, new_max=4):
    return (value - old_min) / (old_max - old_min) * (new_max - new_min) + new_min

df['US_TBM1'] = df['TBM1'].apply(min_max_normalize)
df['US_TBM2'] = df['TBM2'].apply(min_max_normalize)
df['US_TBM3'] = df['TBM3'].apply(min_max_normalize)

# ===== CÂU 10: Tạo KQXT =====
def ket_qua_xet_tuyen(row):
    dh1, dh2, dh3 = row['DH1'], row['DH2'], row['DH3']
    kt = row['KT']
    
    if kt in ['A', 'A1']:
        diem_xet = (dh1 * 2 + dh2 + dh3) / 4
    elif kt == 'B':
        diem_xet = (dh1 + dh2 * 2 + dh3) / 4
    else:
        diem_xet = (dh1 + dh2 + dh3) / 3
    
    return 1 if diem_xet >= 5.0 else 0

df['KQXT'] = df.apply(ket_qua_xet_tuyen, axis=1)

# ===== LƯU FILE =====
output_path = r"DuLieu\processed_dulieuxettuyendaihoc.csv"
df.to_csv(output_path, index=False, encoding='utf-8')

print(f"Đã lưu dữ liệu vào file: {output_path}")
print(f"Số dòng: {len(df)}")
print(f"Số cột: {len(df.columns)}")
print(f"\nDanh sách cột mới được thêm:")
print("- TBM1, TBM2, TBM3 (Điểm trung bình)")
print("- XL1, XL2, XL3 (Xếp loại)")
print("- US_TBM1, US_TBM2, US_TBM3 (Điểm thang 4 Mỹ)")
print("- KQXT (Kết quả xét tuyển)")

print("\n--- THÔNG TIN TỔNG QUAN CỦA DỮ LIỆU SAU KHI XỬ LÝ ---")
print(df.info())

print("\n" + "=" * 80)
print("HOÀN THÀNH LAB 1!")
print("=" * 80)
