# -*- coding: utf-8 -*-
# Created by yoshiaki at 2022/01/30

from thefuzz import fuzz, process

# レーベンシュタイン距離
# Simple Ratio 類似度を計算
print(fuzz.ratio("this is a test", "this is a test!"))

# Partial Ratio 類似度を計算(部分一致)
print(fuzz.partial_ratio("this is a test", "this is a test!"))

# Token Sort Ratio(単語並べ替え、単語数考慮)
print(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))
print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))

# Token Set Ratio(単語並べ替え、単語数考慮しない)
print(fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
print(fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))

# あいまい検索
titles = [
    "ハリー・ポッターと賢者の石",
    "ハリー・ポッターと秘密の部屋",
    "ハリー・ポッターとアズカバンの囚人",
    "ハリー・ポッターと炎のゴブレット",
    "ハリー・ポッターと不死鳥の騎士団",
    "ハリー・ポッターと謎のプリンス",
    "ハリー・ポッターと死の秘宝 PART 1",
    "ハリー・ポッターと死の秘宝 PART 2",
]
# 単語として別れていない->rateを使用。"石"というワードから検索=部分一致->fuzz.partial_ratio
print(process.extract("石", titles, limit=1, scorer=fuzz.partial_ratio))
