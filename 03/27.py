# encoding: utf-8
import pycolor
import json
import base
import re

title = pycolor.GREEN
title += "27. 内部リンクの除去"
title += "\n"
title += "  26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ"
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
  # 強調マークアップの削除（2個以上のシングルクオーテーション）
  if "''" in value:
    value = value.replace("'", "")
  # 内部リンクマークアップの削除（1行内に複数ある）
  re_str = "\[\[(?!.*ファイル|File)([\s\S]*?)((\||\#)([\s\S]*?))?\]\]"
  m = re.search(re_str, value)
  while m is not None:
    # 前方一致のみ置換
    value = re.sub(re_str, m.group(1), value, count=1)
    m = re.search(re_str, value)
  info_dic[field] = value

for index, value in info_dic.items():
  print("%s: %s" % (index, value))
