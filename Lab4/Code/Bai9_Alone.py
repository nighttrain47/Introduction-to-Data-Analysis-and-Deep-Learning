# ==============================================================================
# BÀI 9: TẠO ĐẶC TRƯNG 'Alone'
# ==============================================================================
# Tạo thêm đặc trưng 'Alone' để xác định hành khách đi theo nhóm hay cá nhân:
#   Nếu familySize == 1 (đi 1 mình) → Alone = 1
#   Ngược lại                        → Alone = 0
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# Đường dẫn
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'Output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == '__main__':
    print("=" * 80)
    print("BÀI 9: TẠO ĐẶC TRƯNG 'Alone'")
    print("=" * 80)

    # Tải dữ liệu từ bài 8
    df = pd.read_csv(os.path.join(OUTPUT_DIR, 'bai8_familysize.csv'))

    # ── Tạo cột Alone ──
    # familySize = 1 + SibSp + Parch → min = 1 (đi 1 mình)
    df['Alone'] = (df['familySize'] == 1).astype(int)

    # ── Hiển thị kết quả ──
    print("\n📊 Phân bố Alone:")
    print(df['Alone'].value_counts())
    print(f"\n  Số hành khách đi một mình (Alone=1): {df['Alone'].sum()}")
    print(f"  Số hành khách đi theo nhóm (Alone=0): {(df['Alone'] == 0).sum()}")

    print("\n📋 Mẫu dữ liệu (10 dòng đầu):")
    print(df[['PassengerId', 'SibSp', 'Parch', 'familySize', 'Alone']].head(10).to_string())

    # ── Trực quan hóa ──
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Pie chart
    labels = ['Đi theo nhóm (Alone=0)', 'Đi một mình (Alone=1)']
    sizes = [df['Alone'].value_counts()[0], df['Alone'].value_counts()[1]]
    colors = ['#66b3ff', '#ff9999']
    axes[0].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                startangle=90, textprops={'fontsize': 12})
    axes[0].set_title('Tỷ lệ hành khách đi một mình', fontsize=14, fontweight='bold')

    # Bar chart: Survived vs Alone
    sns.countplot(x='Alone', hue='Survived', data=df, palette='Set2', ax=axes[1])
    axes[1].set_title('Tỷ lệ sống sót theo Alone', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Alone', fontsize=12)
    axes[1].set_ylabel('Số lượng', fontsize=12)
    axes[1].set_xticklabels(['Đi theo nhóm', 'Đi một mình'])

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bai9_alone.png'), dpi=150, bbox_inches='tight')
    plt.show()

    # ── Export kết quả ──
    output_file = os.path.join(OUTPUT_DIR, 'bai9_alone.csv')
    df.to_csv(output_file, index=False)
    print(f"\n✅ Đã export kết quả ra: Output/bai9_alone.csv")
    print(f"✅ Đã export biểu đồ ra: Output/bai9_alone.png")
