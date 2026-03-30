"""
BÀI 10: So sánh sự giống nhau của hai động từ đã cho
"""

import nltk
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

from nltk.corpus import wordnet as wn

print("=" * 70)
print("BÀI 10: So sánh sự giống nhau của hai động từ đã cho")
print("=" * 70)

verb_pairs = [('run', 'walk'), ('eat', 'drink'), ('write', 'read')]
for w1, w2 in verb_pairs:
    syn1 = wn.synsets(w1, pos=wn.VERB)
    syn2 = wn.synsets(w2, pos=wn.VERB)
    if syn1 and syn2:
        similarity = syn1[0].wup_similarity(syn2[0])
        path_sim = syn1[0].path_similarity(syn2[0])
        print(f"\n  So sánh: '{w1}' vs '{w2}'")
        print(f"    Synset 1: {syn1[0].name()} - {syn1[0].definition()}")
        print(f"    Synset 2: {syn2[0].name()} - {syn2[0].definition()}")
        print(f"    Wu-Palmer Similarity: {similarity:.4f}")
        print(f"    Path Similarity:      {path_sim:.4f}")
