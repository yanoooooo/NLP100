# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "05. n-gram"
title += "\n"
title += "  与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．"
title += "\n"
title += "  この関数を用い，\"I am an NLPer\"という文から単語bi-gram，文字bi-gramを得よ．"
title += pycolor.END

print(title)

s = "I am an NLPer"

def n_gram(s, n):
    result = [tuple(s[i:i+n]) for i in range(len(s)-n+1)]
    return result

print(n_gram(s, 2))
print(n_gram(s.split(),2))