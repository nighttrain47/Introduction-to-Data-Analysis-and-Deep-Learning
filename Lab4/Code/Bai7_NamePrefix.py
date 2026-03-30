# ==============================================================================
# BÀI 7: TÁCH DANH XƯNG (namePrefix) TỪ secondName
# ==============================================================================
# Tiến hành thêm đặc trưng về danh xưng (namePrefix) trong xã hội
# bằng cách tách Mr, Mrs, Miss, Master ra khỏi "secondName".
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
    print("BÀI 7: TÁCH DANH XƯNG (namePrefix) TỪ secondName")
    print("=" * 80)

    # Tải dữ liệu từ bài 6
    df = pd.read_csv(os.path.join(OUTPUT_DIR, 'bai6_agegroup.csv'))

    # ── Tách danh xưng ──
    # secondName có dạng: "Mr. Owen Harris", "Mrs. John Bradley (...)"
    # → Lấy phần trước dấu chấm đầu tiên làm namePrefix
    df['namePrefix'] = df['secondName'].str.split('.').str[0].str.strip()

    # ── Hiển thị kết quả ──
    print("\n📊 Các danh xưng và số lượng:")
    print(df['namePrefix'].value_counts())

    print("\n📋 Mẫu dữ liệu (10 dòng đầu):")
    print(df[['PassengerId', 'secondName', 'namePrefix']].head(10).to_string())

    # ── Trực quan hóa ──
    plt.figure(figsize=(14, 6))
    prefix_counts = df['namePrefix'].value_counts()
    sns.barplot(x=prefix_counts.index, y=prefix_counts.values, palette='viridis',
                hue=prefix_counts.index, legend=False)
    plt.title('Phân bố danh xưng (namePrefix)', fontsize=16, fontweight='bold')
    plt.xlabel('Danh xưng', fontsize=13)
    plt.ylabel('Số lượng', fontsize=13)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bai7_nameprefix.png'), dpi=150, bbox_inches='tight')
    plt.show()

    # ── Export kết quả ──
    output_file = os.path.join(OUTPUT_DIR, 'bai7_nameprefix.csv')
    df.to_csv(output_file, index=False)
    print(f"\n✅ Đã export kết quả ra: Output/bai7_nameprefix.csv")
    print(f"✅ Đã export biểu đồ ra: Output/bai7_nameprefix.png")
