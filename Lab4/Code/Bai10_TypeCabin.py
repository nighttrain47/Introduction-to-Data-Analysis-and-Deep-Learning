# ==============================================================================
# BÀI 10: TÁCH LOẠI CABIN (typeCabin)
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'Output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == '__main__':
    print("=" * 80)
    print("BÀI 10: TÁCH LOẠI CABIN (typeCabin)")
    print("=" * 80)

    df = pd.read_csv(os.path.join(OUTPUT_DIR, 'bai9_alone.csv'))
    print(f"\n⚠️  Cabin bị thiếu: {df['Cabin'].isnull().sum()} / {len(df)}")

    df['typeCabin'] = df['Cabin'].fillna('Unknown').apply(
        lambda x: x[0] if x != 'Unknown' else 'Unknown'
    )

    print("\n📊 Phân bố loại cabin:")
    print(df['typeCabin'].value_counts())

    print("\n📋 Mẫu dữ liệu có cabin:")
    print(df[df['Cabin'].notna()][['PassengerId', 'Cabin', 'typeCabin']].head(10).to_string())

    plt.figure(figsize=(12, 6))
    cabin_order = sorted(df['typeCabin'].unique())
    sns.countplot(x='typeCabin', data=df, order=cabin_order, palette='Set3',
                  hue='typeCabin', legend=False)
    plt.title('Phân bố loại cabin (typeCabin)', fontsize=16, fontweight='bold')
    plt.xlabel('Loại Cabin', fontsize=13)
    plt.ylabel('Số lượng', fontsize=13)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bai10_typecabin.png'), dpi=150, bbox_inches='tight')
    plt.show()

    df.to_csv(os.path.join(OUTPUT_DIR, 'bai10_typecabin.csv'), index=False)
    print(f"\n✅ Đã export: Output/bai10_typecabin.csv")
    print(f"✅ Đã export: Output/bai10_typecabin.png")
