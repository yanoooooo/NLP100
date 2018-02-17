# encoding: utf-8
import pycolor
import json
import base

title = pycolor.GREEN
title += "21. カテゴリ名を含む行を抽出"
title += "\n"
title += "  記事中でカテゴリ名を宣言している行を抽出せよ．"
title += pycolor.END

print(title)

dic = base.extract_text()
lines = dic["text"].split("\n")

for line in dic["text"].split("\n"):
  if("Category" in line):
    print(line)
