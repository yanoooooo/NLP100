# encoding: utf-8
import pycolor
import json
import base
import re

title = pycolor.GREEN
title += "25. テンプレートの抽出"
title += "\n"
title += "  記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．"
title += pycolor.END

print(title)

dic = base.extract_text()
lines = dic["text"].split("\n")
bracket_level = 0
info = ""

# 基礎情報のみを抜き出す
for line in dic["text"].split("\n"):
  if bracket_level > 0:
    info += line+"\n"
    if "{{" in line:
      bracket_level += 1
    if "}}" in line:
      bracket_level -= 1
    if bracket_level == 0:
      break
  m = re.search(r"^{{基礎情報", line)
  if m is not None:
    bracket_level = 1
    info += line

# 辞書型に整形
info_arr = info.split("\n")
info_dic = {}
field = ""
value = ""
for line in info_arr:
  m = re.search(r"\|(.*?)=(.*)", line)
  if m is not None: # 1:1
    field = m.group(1).strip()
    value = m.group(2).strip()
  else: # 1:n
    m = re.search(r"{{(.*)}}", line)
    if m is not None:
      value += line
  info_dic[field] = value

for index, value in info_dic.items():
  print("%s: %s" % (index, value))
