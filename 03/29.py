# encoding: utf-8
import pycolor
import json
import base
import re
import urllib.parse
import urllib.request

title = pycolor.GREEN
title += "29. 国旗画像のURLを取得する"
title += "\n"
title += "  テンプレートの内容を利用し，国旗画像のURLを取得せよ．"
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
  # 箇条書きマークアップの削除
  line = re.sub(r"^\*+", "", line, count=1)
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
  # 二重括弧
  re_str = "\{\{(([\s\S]*)(\||\#))+([\s\S]*?)\}\}"
  m = re.search(re_str, value)
  while m is not None:
    # 前方一致のみ置換
    value = re.sub(re_str, m.group(4), value, count=1)
    m = re.search(re_str, value)
  # ファイルマークアップの削除
  m = re.search(r"\[\[(ファイル|File):([\s\S]*?)((\||\#)([\s\S]*?))?\]\]", value)
  if m is not None:
    value = m.group(2)
  # 外部リンクの削除
  value = re.sub(r"\[([\s\S]*?)\]", "", value)
  # 改行の変換
  value = value.replace("<br/>", "、")
  value = value.replace("<br />", "、")
  # 最後に辞書に代入
  info_dic[field] = value

# 国旗画像の取得
for index, value in info_dic.items():
  if index == "国旗画像":
    query = {
      "action": "query",
      "titles": "File:"+value,
      "prop": "imageinfo",
      "iiprop": "url",
      "iiurlwidth": "220",
      "format": "json"
    }
    url = "https://commons.wikimedia.org/w/api.php?"
    url += urllib.parse.urlencode(query)
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    jsonData = json.loads(res.read())
    print(jsonData["query"]["pages"]["347935"]["imageinfo"][0]["thumburl"])
    #print("%s: %s" % (index, value))
