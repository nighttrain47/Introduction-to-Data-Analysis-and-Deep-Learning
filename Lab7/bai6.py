"""
BÀI 6: Tìm định nghĩa và ví dụ của một từ bằng WordNet
"""

import nltk
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

from nltk.corpus import wordnet as wn

print("=" * 70)
print("BÀI 6: Tìm định nghĩa và ví dụ của một từ bằng WordNet")
print("=" * 70)

words_to_define = ['dog', 'computer', 'happy']
for word in words_to_define:
    synsets = wn.synsets(word)
    print(f"\n  Từ: '{word}'")
    print(f"  Số synset tìm thấy: {len(synsets)}")
    for i, syn in enumerate(synsets[:3], 1):  # Chỉ hiển thị 3 synset đầu
        print(f"\n    Synset {i}: {syn.name()}")
        print(f"    Định nghĩa: {syn.definition()}")
        examples = syn.examples()
        if examples:
            print(f"    Ví dụ: {examples}")
        else:
            print(f"    Ví dụ: (không có)")
