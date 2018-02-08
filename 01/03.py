# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "03. 円周率"
title += "\n"
title += "  \"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.\""
title += "  という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．"
title += pycolor.END

print(title)

sen = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 複数行で
sen = sen.strip(",.")
word = sen.split()
result = []
for i in word:
  result.append(len(i))

print(result)

# 1行で可能
count = [len(i.strip(",.")) for i in sen.split()]
print(count)