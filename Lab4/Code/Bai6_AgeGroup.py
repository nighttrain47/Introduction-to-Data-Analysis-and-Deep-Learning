# ==============================================================================
# BÀI 6: XÂY DỰNG BIẾN SỐ Agegroup
# ==============================================================================
# Xây dựng biến số Agegroup có thang đo thứ tự:
#   age <= 12       → Kid
#   (12, 18]        → Teen
#   (18, 60]        → Adult
#   age > 60        → Older
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
    print("BÀI 6: XÂY DỰNG BIẾN SỐ Agegroup")
    print("=" * 80)

    # Tải dữ liệu từ bài 5
    df = pd.read_csv(os.path.join(OUTPUT_DIR, 'bai5_handle_age.csv'))

    # ── Phân nhóm tuổi ──
    def classify_age(age):
        if age <= 12:
            return 'Kid'
        elif age <= 18:
            return 'Teen'
        elif age <= 60:
            return 'Adult'
        else:
            return 'Older'

    df['Agegroup'] = df['Age'].apply(classify_age)

    # ── Hiển thị kết quả ──
    print("\n📊 Phân bố nhóm tuổi:")
    print(df['Agegroup'].value_counts())

    print("\n📋 Mẫu dữ liệu (10 dòng đầu):")
    print(df[['PassengerId', 'Age', 'Agegroup']].head(10).to_string())

    # ── Trực quan hóa ──
    plt.figure(figsize=(10, 6))
    order = ['Kid', 'Teen', 'Adult', 'Older']
    ax = sns.countplot(x='Agegroup', data=df, order=order, palette='Set2',
                       hue='Agegroup', legend=False)
    plt.title('Phân bố nhóm tuổi hành khách (Agegroup)', fontsize=16, fontweight='bold')
    plt.xlabel('Nhóm tuổi', fontsize=13)
    plt.ylabel('Số lượng', fontsize=13)

    # Thêm số lượng lên cột
    counts = df['Agegroup'].value_counts().reindex(order)
    for i, v in enumerate(counts):
        ax.text(i, v + 5, str(v), ha='center', fontweight='bold', fontsize=12)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bai6_agegroup.png'), dpi=150, bbox_inches='tight')
    plt.show()

    # ── Export kết quả ──
    output_file = os.path.join(OUTPUT_DIR, 'bai6_agegroup.csv')
    df.to_csv(output_file, index=False)
    print(f"\n✅ Đã export kết quả ra: Output/bai6_agegroup.csv")
    print(f"✅ Đã export biểu đồ ra: Output/bai6_agegroup.png")
