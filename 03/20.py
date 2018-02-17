# encoding: utf-8
import pycolor
import json

title = pycolor.GREEN
title += "20. JSONデータの読み込み"
title += "\n"
title += "  Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．"
title += "\n"
title += "  問題21-29では，ここで抽出した記事本文に対して実行せよ．"
title += pycolor.END

print(title)

filename = "datas/jawiki-country.json"
f = open(filename, "r")
dic = {}
for line in f:
  jsonData = json.loads(line)
  if("イギリス" in jsonData["title"]):
    dic["title"] = jsonData["title"]
    dic["text"] = jsonData["text"]

print(dic)
f.close()
