# -*- coding: utf-8 -*-
"""
CÂU 6: XỬ LÝ DỮ LIỆU THIẾU CHO TẤT CẢ CÁC BIẾN ĐIỂM SỐ
"""

import pandas as pd

print("=" * 80)
print("CÂU 6: XỬ LÝ DỮ LIỆU THIẾU CHO TẤT CẢ CÁC BIẾN ĐIỂM SỐ")
print("=" * 80)

df = pd.read_csv(r"DuLieu\dulieuxettuyendaihoc.csv")

# Xử lý DT (điền 0)
df['DT'] = df['DT'].fillna(0)

# Các cột điểm số (loại trừ STT, GT, DT, KV, KT)
non_score_cols = ['STT', 'GT', 'DT', 'KV', 'KT']
score_cols = [col for col in df.columns if col not in non_score_cols]

print("\n--- Thống kê dữ liệu thiếu trước khi xử lý ---")
print(df[score_cols].isna().sum())

# Thay thế dữ liệu thiếu bằng Mean
for col in score_cols:
    df[col] = df[col].fillna(df[col].mean())

print("\n--- Sau khi xử lý ---")
print(f"Tổng số giá trị thiếu còn lại: {df[score_cols].isna().sum().sum()}")

df.to_csv(r"DuLieu\temp_cau6.csv", index=False)
print("\nĐã lưu kết quả vào temp_cau6.csv")
