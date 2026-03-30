# -*- coding: utf-8 -*-
"""
Phần 1 - Câu 3: Tạo pivot-table để thống kê các giá trị count, sum, mean, median, 
min, max, std, Q1, Q2 và Q3 của DH1 theo KT (Khối thi)
"""

import pandas as pd
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Định nghĩa hàm tính Q1 (25th percentile)
def q1(x):
    return x.quantile(0.25)

# Định nghĩa hàm tính Q2 (50th percentile - median)
def q2(x):
    return x.quantile(0.50)

# Định nghĩa hàm tính Q3 (75th percentile)
def q3(x):
    return x.quantile(0.75)

# Tạo pivot table
pivot_table = df.pivot_table(
    values='DH1',
    index='KT',
    aggfunc={
        'DH1': ['count', 'sum', 'mean', 'median', 'min', 'max', 'std', q1, q2, q3]
    }
)

# Làm phẳng tên cột
pivot_table.columns = ['Count', 'Max', 'Mean', 'Median', 'Min', 'Q1', 'Q2', 'Q3', 'Std', 'Sum']

# Sắp xếp lại thứ tự cột
pivot_table = pivot_table[['Count', 'Sum', 'Mean', 'Median', 'Min', 'Max', 'Std', 'Q1', 'Q2', 'Q3']]

# Hiển thị kết quả
print("="*100)
print("PIVOT TABLE: THỐNG KÊ DH1 THEO KHỐI THI (KT)")
print("="*100)
print(pivot_table.round(4).to_string())
print("\n" + "="*100)

# Cách 2: Sử dụng groupby với agg
print("\n--- Cách 2: Sử dụng groupby ---")
stats = df.groupby('KT')['DH1'].agg([
    ('Count', 'count'),
    ('Sum', 'sum'),
    ('Mean', 'mean'),
    ('Median', 'median'),
    ('Min', 'min'),
    ('Max', 'max'),
    ('Std', 'std'),
    ('Q1', lambda x: x.quantile(0.25)),
    ('Q2', lambda x: x.quantile(0.50)),
    ('Q3', lambda x: x.quantile(0.75))
])
print(stats.round(4).to_string())
