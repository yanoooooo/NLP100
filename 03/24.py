# encoding: utf-8
import pycolor
import json
import base
import re

title = pycolor.GREEN
title += "24. ファイル参照の抽出"
title += "\n"
title += "  記事から参照されているメディアファイルをすべて抜き出せ．"
title += pycolor.END

print(title)

dic = base.extract_text()
lines = dic["text"].split("\n")

for line in dic["text"].split("\n"):
  m = re.search(r"(File|ファイル):(.*?)\|", line)
  if m is not None:
    print(m.group(2))
