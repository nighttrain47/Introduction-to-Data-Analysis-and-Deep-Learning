"""
LAB 7 - BÀI TẬP ÁP DỤNG
PHÂN TÍCH DỮ LIỆU DẠNG VĂN BẢN VỚI NLTK
"""

import nltk
import random

# Download các gói cần thiết
nltk.download('gutenberg', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
nltk.download('names', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('tagsets', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('tagsets_json', quiet=True)

print("=" * 70)
print("LAB 7 - BÀI TẬP ÁP DỤNG")
print("PHÂN TÍCH DỮ LIỆU DẠNG VĂN BẢN VỚI NLTK")
print("=" * 70)

# =====================================================================
# Bài 1: Liệt kê các tên của corpus
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 1: Liệt kê các tên của corpus")
print("=" * 70)

from nltk.corpus import gutenberg

print("Các corpus trong Gutenberg:")
for i, fileid in enumerate(gutenberg.fileids(), 1):
    print(f"  {i}. {fileid}")

print(f"\nTổng số corpus: {len(gutenberg.fileids())}")

# =====================================================================
# Bài 2: Liệt kê danh sách các stopword bằng các ngôn ngữ khác nhau
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 2: Liệt kê danh sách các stopword bằng các ngôn ngữ khác nhau")
print("=" * 70)

from nltk.corpus import stopwords

languages = stopwords.fileids()
print(f"Số ngôn ngữ có stopword: {len(languages)}")
print("\nDanh sách các ngôn ngữ:")
for i, lang in enumerate(languages, 1):
    print(f"  {i}. {lang}")

# =====================================================================
# Bài 3: Kiểm tra danh sách các stopword bằng các ngôn ngữ khác nhau
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 3: Kiểm tra danh sách các stopword bằng các ngôn ngữ khác nhau")
print("=" * 70)

# Hiển thị 10 stopword đầu tiên của một số ngôn ngữ
sample_languages = ['english', 'french', 'german', 'spanish', 'italian']
for lang in sample_languages:
    sw = stopwords.words(lang)
    print(f"\n  Ngôn ngữ: {lang.upper()}")
    print(f"  Tổng số stopword: {len(sw)}")
    print(f"  10 stopword đầu tiên: {sw[:10]}")

# =====================================================================
# Bài 4: Loại bỏ các stopword từ một văn bản đã cho
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 4: Loại bỏ các stopword từ một văn bản đã cho")
print("=" * 70)

sample_text = "This is a sample sentence showing off the stop words filtration. " \
              "The quick brown fox jumps over the lazy dog."
print(f"Văn bản gốc:\n  {sample_text}")

# Tokenize văn bản
tokens = nltk.word_tokenize(sample_text)
print(f"\nCác từ sau khi tokenize ({len(tokens)} từ):\n  {tokens}")

# Loại bỏ stopword
sw_english = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in sw_english]
print(f"\nCác từ sau khi loại bỏ stopword ({len(filtered_tokens)} từ):\n  {filtered_tokens}")

filtered_sentence = ' '.join(filtered_tokens)
print(f"\nVăn bản sau khi loại bỏ stopword:\n  {filtered_sentence}")

# =====================================================================
# Bài 5: Bỏ qua các stopword từ danh sách các stopword
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 5: Bỏ qua các stopword từ danh sách các stopword")
print("=" * 70)

# Loại bỏ một số stopword ra khỏi danh sách stopword
words_to_ignore = {'not', 'no', 'nor', 'neither', 'never', 'nobody'}
print(f"Các stopword muốn bỏ qua (giữ lại trong văn bản): {words_to_ignore}")

custom_sw = sw_english - words_to_ignore
print(f"\nSố stopword ban đầu: {len(sw_english)}")
print(f"Số stopword sau khi bỏ qua: {len(custom_sw)}")

sample_text2 = "I do not like this movie. It is not good and nobody likes it."
print(f"\nVăn bản gốc:\n  {sample_text2}")

tokens2 = nltk.word_tokenize(sample_text2)

# Lọc với bộ stopword gốc
filtered_original = [w for w in tokens2 if w.lower() not in sw_english]
print(f"\nLọc với bộ stopword gốc:\n  {' '.join(filtered_original)}")

# Lọc với bộ stopword tùy chỉnh (giữ lại not, no, ...)
filtered_custom = [w for w in tokens2 if w.lower() not in custom_sw]
print(f"\nLọc với bộ stopword tùy chỉnh (giữ lại phủ định):\n  {' '.join(filtered_custom)}")

# =====================================================================
# Bài 6: Tìm định nghĩa và ví dụ của một từ bằng WordNet
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 6: Tìm định nghĩa và ví dụ của một từ bằng WordNet")
print("=" * 70)

from nltk.corpus import wordnet as wn

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

# =====================================================================
# Bài 7: Tìm tập hợp các từ đồng nghĩa và trái nghĩa
# =====================================================================
print("\n" + "=" * 70)
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

# =====================================================================
# Bài 8: Tổng quan về bộ tag, chi tiết tag và biểu thức chính quy
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 8: Tổng quan về bộ tag POS")
print("=" * 70)

import re

# Tổng quan về bộ tagset
print("\n  --- Tổng quan về bộ tagset ---")
try:
    nltk.help.upenn_tagset()
except Exception:
    # Fallback: hiển thị thủ công
    tagset_info = {
        'CC': 'Coordinating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'EX': 'Existential there',
        'FW': 'Foreign word',
        'IN': 'Preposition or subordinating conjunction',
        'JJ': 'Adjective',
        'JJR': 'Adjective, comparative',
        'JJS': 'Adjective, superlative',
        'LS': 'List item marker',
        'MD': 'Modal',
        'NN': 'Noun, singular or mass',
        'NNS': 'Noun, plural',
        'NNP': 'Proper noun, singular',
        'NNPS': 'Proper noun, plural',
        'PDT': 'Predeterminer',
        'POS': 'Possessive ending',
        'PRP': 'Personal pronoun',
        'PRP$': 'Possessive pronoun',
        'RB': 'Adverb',
        'RBR': 'Adverb, comparative',
        'RBS': 'Adverb, superlative',
        'RP': 'Particle',
        'TO': 'to',
        'UH': 'Interjection',
        'VB': 'Verb, base form',
        'VBD': 'Verb, past tense',
        'VBG': 'Verb, gerund or present participle',
        'VBN': 'Verb, past participle',
        'VBP': 'Verb, non-3rd person singular present',
        'VBZ': 'Verb, 3rd person singular present',
        'WDT': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WP$': 'Possessive wh-pronoun',
        'WRB': 'Wh-adverb',
    }
    for tag, desc in tagset_info.items():
        print(f"    {tag:6s} : {desc}")

# Chi tiết về một tag cụ thể
print("\n  --- Chi tiết về tag 'NN' (Noun, singular or mass) ---")
try:
    nltk.help.upenn_tagset('NN')
except Exception:
    print("    NN: Noun, singular or mass")
    print("    Ví dụ: dog, cat, house, tree")

# Sử dụng biểu thức chính quy để tìm các tag liên quan
print("\n  --- Các tag liên quan đến Noun (regex: ^NN) ---")
pattern = re.compile(r'^NN')
noun_tags = {tag: desc for tag, desc in tagset_info.items() if pattern.match(tag)}
for tag, desc in noun_tags.items():
    print(f"    {tag:6s} : {desc}")

print("\n  --- Các tag liên quan đến Verb (regex: ^VB) ---")
pattern = re.compile(r'^VB')
verb_tags = {tag: desc for tag, desc in tagset_info.items() if pattern.match(tag)}
for tag, desc in verb_tags.items():
    print(f"    {tag:6s} : {desc}")

print("\n  --- Các tag liên quan đến Adjective (regex: ^JJ) ---")
pattern = re.compile(r'^JJ')
adj_tags = {tag: desc for tag, desc in tagset_info.items() if pattern.match(tag)}
for tag, desc in adj_tags.items():
    print(f"    {tag:6s} : {desc}")

# =====================================================================
# Bài 9: So sánh sự giống nhau của hai danh từ đã cho
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 9: So sánh sự giống nhau của hai danh từ đã cho")
print("=" * 70)

noun_pairs = [('dog', 'cat'), ('car', 'bicycle'), ('book', 'library')]
for w1, w2 in noun_pairs:
    syn1 = wn.synsets(w1, pos=wn.NOUN)
    syn2 = wn.synsets(w2, pos=wn.NOUN)
    if syn1 and syn2:
        similarity = syn1[0].wup_similarity(syn2[0])
        path_sim = syn1[0].path_similarity(syn2[0])
        print(f"\n  So sánh: '{w1}' vs '{w2}'")
        print(f"    Synset 1: {syn1[0].name()} - {syn1[0].definition()}")
        print(f"    Synset 2: {syn2[0].name()} - {syn2[0].definition()}")
        print(f"    Wu-Palmer Similarity: {similarity:.4f}")
        print(f"    Path Similarity:      {path_sim:.4f}")

# =====================================================================
# Bài 10: So sánh sự giống nhau của hai động từ đã cho
# =====================================================================
print("\n" + "=" * 70)
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

# =====================================================================
# Bài 11: Tìm số lượng tên nam và nữ trong kho ngữ liệu names
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 11: Số lượng tên nam và nữ trong kho ngữ liệu names")
print("=" * 70)

from nltk.corpus import names

male_names = names.words('male.txt')
female_names = names.words('female.txt')

print(f"\n  Số lượng tên nam (male.txt):   {len(male_names)}")
print(f"  Số lượng tên nữ (female.txt):  {len(female_names)}")
print(f"  Tổng cộng:                     {len(male_names) + len(female_names)}")

print(f"\n  10 tên nam đầu tiên:  {male_names[:10]}")
print(f"  10 tên nữ đầu tiên:   {female_names[:10]}")

# =====================================================================
# Bài 12: In 15 kết hợp ngẫu nhiên đầu tiên tên nam và tên nữ
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 12: 15 kết hợp ngẫu nhiên tên nam và tên nữ từ kho tên")
print("=" * 70)

# Tạo danh sách tên có gắn nhãn
labeled_names = ([(name, 'male') for name in male_names] +
                 [(name, 'female') for name in female_names])

# Trộn ngẫu nhiên
random.shuffle(labeled_names)

print("\n  15 kết hợp ngẫu nhiên đầu tiên:")
print(f"  {'STT':>4s}  {'Tên':<20s}  {'Giới tính':<10s}")
print(f"  {'----':>4s}  {'----':<20s}  {'---------':<10s}")
for i, (name, label) in enumerate(labeled_names[:15], 1):
    print(f"  {i:>4d}  {name:<20s}  {label:<10s}")

# =====================================================================
# Bài 13: Trích xuất ký tự cuối cùng của tất cả các tên và tạo mảng mới
# =====================================================================
print("\n" + "=" * 70)
print("BÀI 13: Trích xuất ký tự cuối cùng của tất cả các tên")
print("=" * 70)

# Tạo mảng mới với chữ cái cuối cùng và nhãn
last_letter_data = [(name[-1].lower(), label) for name, label in labeled_names]

print("\n  20 mẫu đầu tiên (chữ cái cuối cùng, nhãn):")
print(f"  {'STT':>4s}  {'Tên gốc':<20s}  {'Chữ cái cuối':<14s}  {'Nhãn':<10s}")
print(f"  {'----':>4s}  {'--------':<20s}  {'------------':<14s}  {'----':<10s}")
for i in range(20):
    name, label = labeled_names[i]
    last_char = last_letter_data[i][0]
    print(f"  {i+1:>4d}  {name:<20s}  {last_char:^14s}  {label:<10s}")

# Thống kê phân bổ ký tự cuối cùng theo giới tính
print("\n  --- Thống kê phân bổ ký tự cuối cùng theo giới tính ---")

from collections import Counter

male_last = [name[-1].lower() for name in male_names]
female_last = [name[-1].lower() for name in female_names]

male_counter = Counter(male_last)
female_counter = Counter(female_last)

print(f"\n  {'Ký tự':>6s}  {'Nam':>6s}  {'Nữ':>6s}")
print(f"  {'-----':>6s}  {'---':>6s}  {'---':>6s}")

all_letters = sorted(set(male_last + female_last))
for letter in all_letters:
    m_count = male_counter.get(letter, 0)
    f_count = female_counter.get(letter, 0)
    print(f"  {letter:>6s}  {m_count:>6d}  {f_count:>6d}")

# Tìm các chữ cái phổ biến nhất theo giới tính
print(f"\n  Top 5 chữ cái cuối phổ biến nhất ở tên NAM:  {male_counter.most_common(5)}")
print(f"  Top 5 chữ cái cuối phổ biến nhất ở tên NỮ:   {female_counter.most_common(5)}")

print("\n" + "=" * 70)
print("HOÀN TẤT TẤT CẢ BÀI TẬP LAB 7!")
print("=" * 70)
