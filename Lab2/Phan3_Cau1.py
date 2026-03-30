# -*- coding: utf-8 -*-
"""
Phần 3 - Câu 1: Trực quan dữ liệu học sinh nữ trên các nhóm XL1, XL2, XL3 dạng unstacked
- Lọc dữ liệu giới tính là nữ
- Oy: Chiều cao biểu đồ cột thể hiện số lượng học sinh theo xếp loại
- Màu sắc thể hiện giá trị xếp loại: [Y, TB, K, G, XS]
- Ox: thể hiện nhóm XL1, XL2 và XL3
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Lọc học sinh nữ
df_female = df[df['GT'] == 'F']

print("="*70)
print("TRỰC QUAN DỮ LIỆU HỌC SINH NỮ TRÊN CÁC NHÓM XL1, XL2, XL3")
print("="*70)
print(f"Tổng số học sinh nữ: {len(df_female)}")

# Thống kê tần số cho từng biến XL
xl_vars = ['XL1', 'XL2', 'XL3']
xl_categories = ['Y', 'TB', 'K', 'G', 'XS']

# Tạo bảng đếm
count_data = {}
for xl in xl_vars:
    count_data[xl] = df_female[xl].value_counts()

print("\n--- Bảng tần số ---")
freq_df = pd.DataFrame(count_data).fillna(0).astype(int)
# Đảm bảo có đầy đủ các xếp loại
for cat in xl_categories:
    if cat not in freq_df.index:
        freq_df.loc[cat] = 0
freq_df = freq_df.loc[[cat for cat in xl_categories if cat in freq_df.index]]
print(freq_df)

# Vẽ biểu đồ unstacked (grouped bar chart)
fig, ax = plt.subplots(figsize=(12, 6))

# Chuẩn bị dữ liệu
x = np.arange(len(xl_vars))  # vị trí của các nhóm XL
width = 0.15  # độ rộng mỗi cột

# Màu sắc cho từng xếp loại
colors = {
    'Y': '#e74c3c',    # Đỏ - Yếu
    'TB': '#f39c12',   # Cam - Trung bình
    'K': '#3498db',    # Xanh dương - Khá
    'G': '#2ecc71',    # Xanh lá - Giỏi
    'XS': '#9b59b6'    # Tím - Xuất sắc
}

# Vẽ từng nhóm xếp loại
bars_list = []
labels_used = []
for i, cat in enumerate(xl_categories):
    values = []
    for xl in xl_vars:
        if cat in count_data[xl].index:
            values.append(count_data[xl][cat])
        else:
            values.append(0)
    
    if sum(values) > 0:  # Chỉ vẽ nếu có dữ liệu
        offset = (i - len(xl_categories)/2 + 0.5) * width
        bars = ax.bar(x + offset, values, width, label=cat, color=colors.get(cat, '#95a5a6'), 
                      edgecolor='black', linewidth=0.8)
        bars_list.append(bars)
        labels_used.append(cat)
        
        # Thêm giá trị lên đầu cột
        for bar, val in zip(bars, values):
            if val > 0:
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, 
                        str(int(val)), ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xlabel('Biến Xếp loại', fontsize=12)
ax.set_ylabel('Số lượng học sinh nữ', fontsize=12)
ax.set_title('Biểu đồ cột Unstacked - Phân bố xếp loại học sinh Nữ\n(XL1, XL2, XL3)', 
             fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(xl_vars, fontsize=12)
ax.legend(title='Xếp loại', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Thêm ghi chú
ax.text(0.02, 0.98, 'Y=Yếu, TB=Trung bình, K=Khá, G=Giỏi, XS=Xuất sắc', 
        transform=ax.transAxes, fontsize=9, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('DuLieu/Phan3_Cau1_XL_Female.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan3_Cau1_XL_Female.png")
