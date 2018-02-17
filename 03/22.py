# encoding: utf-8
import pycolor
import json
import base
import re

title = pycolor.GREEN
title += "22. カテゴリ名の抽出"
title += "\n"
title += "  記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．"
title += pycolor.END

print(title)

dic = base.extract_text()
lines = dic["text"].split("\n")

for line in dic["text"].split("\n"):
  m = re.search(r"\[\[Category:(?P<value>.*)\]\]", line)
  if m is not None:
    print(m.group("value"))
