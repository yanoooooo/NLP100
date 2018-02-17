# encoding: utf-8
import pycolor
import json
import base
import re

title = pycolor.GREEN
title += "23. セクション構造"
title += "\n"
title += "  記事中に含まれるセクション名とそのレベル（例えば\"== セクション名 ==\"なら1）を表示せよ．"
title += pycolor.END

print(title)

dic = base.extract_text()
lines = dic["text"].split("\n")

for line in dic["text"].split("\n"):
  m = re.search(r"^(=+)(.*[^=])", line)
  if m is not None:
    print("%s, %s, %d" % (m.group(1), m.group(2).strip(), len(m.group(1))-1))
