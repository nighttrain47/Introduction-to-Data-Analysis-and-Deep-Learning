"""
BÀI 8: Tổng quan về bộ tag, chi tiết tag và biểu thức chính quy
"""

import nltk
import re

nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('tagsets', quiet=True)
nltk.download('tagsets_json', quiet=True)

print("=" * 70)
print("BÀI 8: Tổng quan về bộ tag POS")
print("=" * 70)

# Định nghĩa tagset_info luôn (dùng cho cả hiển thị và regex bên dưới)
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

# Tổng quan về bộ tagset
print("\n  --- Tổng quan về bộ tagset ---")
try:
    nltk.help.upenn_tagset()
except Exception:
    # Fallback: hiển thị thủ công
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
