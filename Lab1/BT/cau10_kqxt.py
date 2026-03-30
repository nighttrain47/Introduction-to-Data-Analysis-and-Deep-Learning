# -*- coding: utf-8 -*-
"""
CÂU 10: TẠO BIẾN KẾT QUẢ XÉT TUYỂN (KQXT)
- Khối A, A1: (DH1*2 + DH2 + DH3) / 4 >= 5.0 -> Đậu (1)
- Khối B: (DH1 + DH2*2 + DH3) / 4 >= 5.0 -> Đậu (1)
- Khối khác: (DH1 + DH2 + DH3) / 3 >= 5.0 -> Đậu (1)
"""

import pandas as pd

print("=" * 80)
print("CÂU 10: TẠO BIẾN KẾT QUẢ XÉT TUYỂN (KQXT)")
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

def ket_qua_xet_tuyen(row):
    """Hàm tính kết quả xét tuyển dựa trên khối thi và điểm"""
    dh1, dh2, dh3 = row['DH1'], row['DH2'], row['DH3']
    kt = row['KT']
    
    if kt in ['A', 'A1']:
        diem_xet = (dh1 * 2 + dh2 + dh3) / 4
    elif kt == 'B':
        diem_xet = (dh1 + dh2 * 2 + dh3) / 4
    else:  # C, D1 và các khối khác
        diem_xet = (dh1 + dh2 + dh3) / 3
    
    return 1 if diem_xet >= 5.0 else 0

df['KQXT'] = df.apply(ket_qua_xet_tuyen, axis=1)

print("--- Thống kê kết quả xét tuyển ---")
print(f"Số học sinh đậu: {(df['KQXT'] == 1).sum()}")
print(f"Số học sinh rớt: {(df['KQXT'] == 0).sum()}")
print(f"Tỉ lệ đậu: {(df['KQXT'] == 1).sum() / len(df) * 100:.2f}%")

print("\n--- Kết quả theo khối thi ---")
print(df.groupby('KT')['KQXT'].agg(['sum', 'count', 'mean']).rename(
    columns={'sum': 'Đậu', 'count': 'Tổng', 'mean': 'Tỉ lệ đậu'}
))

# Lưu kết quả tạm
df.to_csv(r"DuLieu\temp_cau10.csv", index=False)
print("\nĐã lưu kết quả tạm vào temp_cau10.csv")
