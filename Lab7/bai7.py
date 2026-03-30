"""
BÀI 7: Tìm tập hợp các từ đồng nghĩa và trái nghĩa
"""

import nltk
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

from nltk.corpus import wordnet as wn

print("=" * 70)
print("BÀI 7: Tìm tập hợp các từ đồng nghĩa và trái nghĩa")
print("=" * 70)

words_to_check = ['good', 'happy', 'fast']
for word in words_to_check:
    synonyms = set()
    antonyms = set()

    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                for ant in lemma.antonyms():
                    antonyms.add(ant.name())

    print(f"\n  Từ: '{word}'")
    print(f"  Từ đồng nghĩa: {sorted(synonyms)}")
    print(f"  Từ trái nghĩa: {sorted(antonyms)}")
