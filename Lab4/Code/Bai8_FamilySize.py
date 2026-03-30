# ==============================================================================
# BÀI 8: TÍNH FAMILY SIZE
# ==============================================================================
# Khai thác thêm thông tin số lượng thành viên đi theo nhóm thân quen
# (familySize) đối với mỗi hành khách:
#   familySize = 1 + SibSp + Parch
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
    print("BÀI 8: TÍNH FAMILY SIZE")
    print("=" * 80)

    # Tải dữ liệu từ bài 7
    df = pd.read_csv(os.path.join(OUTPUT_DIR, 'bai7_nameprefix.csv'))

    # ── Tính familySize ──
    df['familySize'] = 1 + df['SibSp'] + df['Parch']

    # ── Hiển thị kết quả ──
    print("\n📊 Phân bố familySize:")
    print(df['familySize'].value_counts().sort_index())

    print("\n📋 Mẫu dữ liệu (10 dòng đầu):")
    print(df[['PassengerId', 'SibSp', 'Parch', 'familySize']].head(10).to_string())

    # ── Trực quan hóa ──
    plt.figure(figsize=(10, 6))
    sns.countplot(x='familySize', data=df, palette='coolwarm',
                  hue='familySize', legend=False)
    plt.title('Phân bố kích thước gia đình (familySize)', fontsize=16, fontweight='bold')
    plt.xlabel('Family Size', fontsize=13)
    plt.ylabel('Số lượng', fontsize=13)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bai8_familysize.png'), dpi=150, bbox_inches='tight')
    plt.show()

    # ── Export kết quả ──
    output_file = os.path.join(OUTPUT_DIR, 'bai8_familysize.csv')
    df.to_csv(output_file, index=False)
    print(f"\n✅ Đã export kết quả ra: Output/bai8_familysize.csv")
    print(f"✅ Đã export biểu đồ ra: Output/bai8_familysize.png")
