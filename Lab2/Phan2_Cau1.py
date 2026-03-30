# -*- coding: utf-8 -*-
"""
Phần 2 - Câu 1: Trình bày dữ liệu biến GT (Giới tính)
- Lập bảng tần số và tần suất
- Vẽ biểu đồ tần số (cột), biểu đồ tần suất (tròn)
"""

import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# 1. Lập bảng tần số và tần suất
print("="*60)
print("BẢNG TẦN SỐ VÀ TẦN SUẤT CỦA BIẾN GIỚI TÍNH (GT)")
print("="*60)

# Tần số
freq = df['GT'].value_counts()
# Tần suất (%)
freq_percent = df['GT'].value_counts(normalize=True) * 100

# Tạo bảng tổng hợp
freq_table = pd.DataFrame({
    'Giới tính': ['Nam (M)', 'Nữ (F)'],
    'Tần số': [freq.get('M', 0), freq.get('F', 0)],
    'Tần suất (%)': [freq_percent.get('M', 0), freq_percent.get('F', 0)]
})
freq_table['Tần suất (%)'] = freq_table['Tần suất (%)'].round(2)
print(freq_table.to_string(index=False))
print(f"\nTổng số: {freq.sum()}")

# 2. Vẽ biểu đồ
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 2.1 Biểu đồ cột (tần số)
colors = ['#3498db', '#e74c3c']
labels = ['Nữ (F)', 'Nam (M)']
values = [freq.get('F', 0), freq.get('M', 0)]

bars = axes[0].bar(labels, values, color=colors, edgecolor='black', linewidth=1.2)
axes[0].set_xlabel('Giới tính', fontsize=12)
axes[0].set_ylabel('Tần số (Số lượng)', fontsize=12)
axes[0].set_title('Biểu đồ cột - Tần số theo Giới tính', fontsize=14, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3)

# Thêm giá trị lên đầu cột
for bar, val in zip(bars, values):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                 str(val), ha='center', va='bottom', fontsize=12, fontweight='bold')

# 2.2 Biểu đồ tròn (tần suất)
explode = (0.05, 0.05)
wedges, texts, autotexts = axes[1].pie(
    values, 
    labels=labels, 
    autopct='%1.1f%%',
    explode=explode,
    colors=colors,
    startangle=90,
    shadow=True
)
axes[1].set_title('Biểu đồ tròn - Tần suất theo Giới tính', fontsize=14, fontweight='bold')

# Tùy chỉnh font
for text in autotexts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

plt.tight_layout()
plt.savefig('DuLieu/Phan2_Cau1_GT.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan2_Cau1_GT.png")
