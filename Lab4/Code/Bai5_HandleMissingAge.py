# ==============================================================================
# BÀI 5: XỬ LÝ DỮ LIỆU THIẾU TRÊN BIẾN AGE
# ==============================================================================
# a. Vẽ Box plot phân phối tuổi theo từng hạng hành khách (Pclass).
#    Nhận xét về tuổi trung bình giữa các nhóm. Đưa ra quyết định thay thế.
# b. Thay thế giá trị Age bị thiếu. Hiển thị kết quả và Heat map.
# ==============================================================================

import pandas as pd
import numpy as np
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
    print("BÀI 5: XỬ LÝ DỮ LIỆU THIẾU TRÊN BIẾN AGE")
    print("=" * 80)

    # Tải dữ liệu từ bài 4
    df = pd.read_csv(os.path.join(OUTPUT_DIR, 'bai4_shorten_sex.csv'))

    # ══════════════════════════════════════════════════════════════════════════
    # 5a: Box plot phân phối tuổi theo hạng hành khách
    # ══════════════════════════════════════════════════════════════════════════
    print("\n" + "─" * 60)
    print("5a: Box plot phân phối tuổi trên từng hạng hành khách")
    print("─" * 60)

    plt.figure(figsize=(12, 7))
    sns.boxplot(x='Pclass', y='Age', data=df, palette='Set2',
                hue='Pclass', legend=False)
    plt.title('Box Plot - Phân phối tuổi theo hạng hành khách (Pclass)',
              fontsize=16, fontweight='bold')
    plt.xlabel('Hạng hành khách (Pclass)', fontsize=13)
    plt.ylabel('Tuổi (Age)', fontsize=13)

    # Thêm giá trị trung bình lên biểu đồ
    for pclass in [1, 2, 3]:
        mean_age = df[df['Pclass'] == pclass]['Age'].mean()
        plt.text(pclass - 1, mean_age + 1, f'Mean: {mean_age:.1f}',
                 ha='center', fontsize=11, color='red', fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bai5a_boxplot_age_pclass.png'), dpi=150, bbox_inches='tight')
    plt.show()

    # Thống kê tuổi theo từng hạng
    print("\n📊 Tuổi trung bình theo từng hạng hành khách:")
    age_stats = df.groupby('Pclass')['Age'].agg(['mean', 'median', 'std', 'count'])
    print(age_stats.round(2))
    print(f"\n📊 Tuổi trung bình toàn bộ hành khách: {df['Age'].mean():.2f}")

    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              NHẬN XÉT                                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  - Hạng 1 (Pclass=1): Tuổi TB cao nhất (~38.2), hành khách thường là      ║
║    người trưởng thành có điều kiện kinh tế.                                 ║
║  - Hạng 2 (Pclass=2): Tuổi TB vừa phải (~29.9), tầng lớp trung lưu.      ║
║  - Hạng 3 (Pclass=3): Tuổi TB thấp nhất (~25.1), nhiều người trẻ.        ║
║                                                                              ║
║  → QUYẾT ĐỊNH: Tuổi trung bình khác biệt RÕ RÀNG giữa các hạng vé.       ║
║    Do đó, thay thế Age bị thiếu bằng TUỔI TRUNG BÌNH THEO TỪNG NHÓM      ║
║    HẠNG VÉ (Pclass) để bảo toàn đặc điểm phân bố tuổi.                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")

    # ══════════════════════════════════════════════════════════════════════════
    # 5b: Thay thế giá trị Age bị thiếu
    # ══════════════════════════════════════════════════════════════════════════
    print("─" * 60)
    print("5b: Thay thế giá trị Age bị thiếu theo nhóm Pclass")
    print("─" * 60)

    print(f"\n⚠️  Số lượng Age bị thiếu TRƯỚC khi xử lý: {df['Age'].isnull().sum()}")

    # Tính trung bình tuổi theo từng hạng
    mean_age_by_pclass = df.groupby('Pclass')['Age'].mean()
    print(f"\nTuổi trung bình theo hạng vé:")
    for pclass, mean_age in mean_age_by_pclass.items():
        print(f"  Pclass {pclass}: {mean_age:.2f}")

    # Hàm thay thế
    def impute_age(row):
        if pd.isnull(row['Age']):
            return round(mean_age_by_pclass[row['Pclass']], 2)
        return row['Age']

    df['Age'] = df.apply(impute_age, axis=1)

    print(f"\n✅ Số lượng Age bị thiếu SAU khi xử lý: {df['Age'].isnull().sum()}")

    # Hiển thị kết quả dạng bảng
    print("\n📋 Kết quả sau khi xử lý (10 dòng đầu):")
    print(df[['PassengerId', 'Pclass', 'Age', 'Sex']].head(10).to_string())

    # Heat map sau khi xử lý
    plt.figure(figsize=(14, 8))
    sns.heatmap(df.isnull(), yticklabels=False, cbar=True, cmap='viridis')
    plt.title("Heat Map - Dữ liệu thiếu SAU KHI xử lý cột 'Age'",
              fontsize=16, fontweight='bold')
    plt.xlabel('Các cột dữ liệu', fontsize=12)
    plt.ylabel('Các dòng dữ liệu', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bai5b_heatmap_after_age.png'), dpi=150, bbox_inches='tight')
    plt.show()

    print("\n→ Sau khi xử lý, cột Age không còn giá trị thiếu trên Heat map.")

    # ── Export kết quả ──
    output_file = os.path.join(OUTPUT_DIR, 'bai5_handle_age.csv')
    df.to_csv(output_file, index=False)
    print(f"\n✅ Đã export kết quả ra: Output/bai5_handle_age.csv")
    print(f"✅ Đã export Box plot ra: Output/bai5a_boxplot_age_pclass.png")
    print(f"✅ Đã export Heat map ra: Output/bai5b_heatmap_after_age.png")
