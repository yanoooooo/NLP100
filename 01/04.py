# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "04. 元素記号"
title += "\n"
title += "  \"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.\"という文を単語に分解し、"
title += "\n"
title += "  1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，"
title += "\n"
title += "  取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．"
title += pycolor.END

print(title)

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

arr = [i.strip(",.") for i in s.split()]
l = [1,5,6,7,8,9,15,16,19]
d = {}
# enumerateでindexつきでループする
for i, w in enumerate(arr):
  if i+1 in l:
    d[w[0]] = i+1
    #print(w[0])
  else:
    d[w[:2]] = i+1
    #print(w[:2])
print(d)

# その他の方法
arr = [i.strip(",.") for i in s.split()]
d = {w[:2-((i+1) in (1,5,6,7,8,9,15,16,19))]:i+1 for i, w in enumerate(arr)}
print(d)

dic = {word[:2-(i in (1,5,6,7,8,9,15,16,19))]:i for i, word in enumerate(s.replace(".", "").split(), 1)}
print(dic)