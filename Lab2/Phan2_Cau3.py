# -*- coding: utf-8 -*-
"""
Phần 2 - Câu 3: Trình bày dữ liệu biến DT với các học sinh là nam
- Lọc dữ liệu học sinh nam (GT = 'M')
- Trình bày dữ liệu biến DT (Dân tộc)
"""

import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Lọc học sinh nam
df_male = df[df['GT'] == 'M']

print("="*60)
print("TRÌNH BÀY DỮ LIỆU BIẾN DÂN TỘC (DT) VỚI HỌC SINH NAM")
print("="*60)
print(f"Tổng số học sinh nam: {len(df_male)}")

# Tần số và tần suất
freq = df_male['DT'].value_counts().sort_index()
freq_percent = df_male['DT'].value_counts(normalize=True).sort_index() * 100

# Ánh xạ mã dân tộc sang tên
dt_labels = {
    0.0: 'Kinh (0)',
    1.0: 'Dân tộc khác (1)',
    6.0: 'Dân tộc khác (6)'
}

print("\n--- Bảng tần số và tần suất ---")
freq_table = pd.DataFrame({
    'Mã DT': freq.index,
    'Tên dân tộc': [dt_labels.get(x, f'Mã {x}') for x in freq.index],
    'Tần số': freq.values,
    'Tần suất (%)': freq_percent.values.round(2)
})
print(freq_table.to_string(index=False))

# Vẽ biểu đồ
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

labels = [dt_labels.get(x, f'Mã {x}') for x in freq.index]
colors = ['#3498db', '#e74c3c', '#2ecc71'][:len(labels)]

# Biểu đồ cột
bars = axes[0].bar(labels, freq.values, color=colors, edgecolor='black', linewidth=1.2)
axes[0].set_xlabel('Dân tộc', fontsize=12)
axes[0].set_ylabel('Tần số (Số lượng)', fontsize=12)
axes[0].set_title('Biểu đồ cột - Tần số DT (Học sinh Nam)', fontsize=14, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3)

# Thêm giá trị lên đầu cột
for bar, val in zip(bars, freq.values):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                 str(val), ha='center', va='bottom', fontsize=12, fontweight='bold')

# Biểu đồ tròn
explode = [0.05] * len(labels)
wedges, texts, autotexts = axes[1].pie(
    freq.values, 
    labels=labels, 
    autopct='%1.1f%%',
    explode=explode,
    colors=colors,
    startangle=90,
    shadow=True
)
axes[1].set_title('Biểu đồ tròn - Tần suất DT (Học sinh Nam)', fontsize=14, fontweight='bold')

for text in autotexts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

plt.tight_layout()
plt.savefig('DuLieu/Phan2_Cau3_DT_Male.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan2_Cau3_DT_Male.png")
