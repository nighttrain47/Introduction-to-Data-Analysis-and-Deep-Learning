# -*- coding: utf-8 -*-
"""
Phần 5 - Câu 4: Khảo sát tương quan giữa biến DH1 theo biến T1 trên từng nhóm khu vực
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

print("="*80)
print("KHẢO SÁT TƯƠNG QUAN GIỮA DH1 VÀ T1 TRÊN TỪNG NHÓM KHU VỰC")
print("="*80)

# Danh sách khu vực
kv_list = ['1', '2', '2NT']
colors = {'1': '#3498db', '2': '#e74c3c', '2NT': '#2ecc71'}

# Thống kê tương quan theo từng khu vực
print("\n--- Tương quan DH1 vs T1 theo Khu vực ---")

correlation_data = []
for kv in kv_list:
    kv_data = df[df['KV'] == kv]
    if len(kv_data) > 2:
        T1 = kv_data['T1']
        DH1 = kv_data['DH1']
        
        covariance = np.cov(T1, DH1)[0, 1]
        correlation, p_value = stats.pearsonr(T1, DH1)
        
        print(f"\nKhu vực {kv}:")
        print(f"  Số quan sát: {len(kv_data)}")
        print(f"  Covariance: {covariance:.4f}")
        print(f"  Correlation (r): {correlation:.4f}")
        print(f"  P-value: {p_value:.6f}")
        
        if abs(correlation) < 0.3:
            strength = "yếu"
        elif abs(correlation) < 0.7:
            strength = "trung bình"
        else:
            strength = "mạnh"
        
        direction = "thuận" if correlation > 0 else "nghịch"
        sig = "có" if p_value < 0.05 else "không có"
        
        print(f"  => Tương quan {strength}, {direction}, {sig} ý nghĩa thống kê (α=0.05)")
        
        correlation_data.append({
            'KV': kv,
            'n': len(kv_data),
            'Covariance': covariance,
            'Correlation': correlation,
            'P-value': p_value
        })

# Bảng tổng hợp
print("\n--- Bảng tổng hợp ---")
summary_df = pd.DataFrame(correlation_data)
print(summary_df.round(4).to_string(index=False))

# Vẽ biểu đồ
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, kv in enumerate(kv_list):
    kv_data = df[df['KV'] == kv]
    if len(kv_data) > 2:
        T1 = kv_data['T1']
        DH1 = kv_data['DH1']
        correlation, p_value = stats.pearsonr(T1, DH1)
        
        axes[i].scatter(T1, DH1, alpha=0.6, c=colors[kv], edgecolors='black', linewidth=0.5)
        
        # Đường hồi quy
        z = np.polyfit(T1, DH1, 1)
        p = np.poly1d(z)
        x_line = np.linspace(T1.min(), T1.max(), 100)
        axes[i].plot(x_line, p(x_line), "r--", linewidth=2, 
                     label=f'y = {z[0]:.2f}x + {z[1]:.2f}')
        
        axes[i].set_xlabel('T1 (Điểm Toán)', fontsize=11)
        axes[i].set_ylabel('DH1 (Điểm ĐH)', fontsize=11)
        axes[i].set_title(f'Khu vực {kv}\nr = {correlation:.3f}, p = {p_value:.4f}', 
                          fontsize=12, fontweight='bold')
        axes[i].legend(fontsize=9)
        axes[i].grid(True, alpha=0.3)
    else:
        axes[i].text(0.5, 0.5, 'Không đủ dữ liệu', ha='center', va='center')
        axes[i].set_title(f'Khu vực {kv}', fontsize=12)

plt.tight_layout()
plt.savefig('DuLieu/Phan5_Cau4_Correlation_by_KV.png', dpi=300, bbox_inches='tight')
plt.show()

# Biểu đồ tổng hợp
fig2, ax2 = plt.subplots(figsize=(10, 7))

for kv in kv_list:
    kv_data = df[df['KV'] == kv]
    if len(kv_data) > 0:
        ax2.scatter(kv_data['T1'], kv_data['DH1'], alpha=0.6, c=colors[kv], 
                    edgecolors='black', linewidth=0.5, label=f'KV {kv}', s=60)

ax2.set_xlabel('T1 (Điểm Toán lần 1)', fontsize=12)
ax2.set_ylabel('DH1 (Điểm ĐH lần 1)', fontsize=12)
ax2.set_title('Tương quan DH1 vs T1 theo Khu vực', fontsize=14, fontweight='bold')
ax2.legend(title='Khu vực', fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('DuLieu/Phan5_Cau4_Correlation_Combined.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan5_Cau4_Correlation_by_KV.png")
print("Đã lưu biểu đồ: DuLieu/Phan5_Cau4_Correlation_Combined.png")
