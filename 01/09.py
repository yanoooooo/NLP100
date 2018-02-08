# encoding: utf-8
import pycolor
import random

title = pycolor.GREEN
title += "09. Typoglycemia"
title += "\n"
title += "  スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，"
title += "\n"
title += "  それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．"
title += "\n"
title += "  ただし，長さが４以下の単語は並び替えないこととする．"
title += "\n"
title += "  適当な英語の文（例えば\"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .\"）を与え，その実行結果を確認せよ．"
title += pycolor.END

print(title)

def f(s):
    result = []
    arr = s.split()
    for w in arr:
        if len(w) > 4:
            ex = list(w[1:-1])
            random.shuffle(ex)
            result.append(w[0] + "".join(ex) + w[-1])
        else:
            result.append(w)

    return " ".join(result)

#typo = lambda s: " ".join(t[0]+"".join(sorted(t[1:-1], key=lambda k:random()))+t[-1] if len(t) > 4 else t for t in s.split())

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(s)
print(f(s))