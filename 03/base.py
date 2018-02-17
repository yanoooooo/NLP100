# encoding: utf-8
import json

def extract_text():
  filename = "datas/jawiki-country.json"
  f = open(filename, "r")
  dic = {}
  for line in f:
    jsonData = json.loads(line)
    if("イギリス" in jsonData["title"]):
      dic["title"] = jsonData["title"]
      dic["text"] = jsonData["text"]
  f.close()
  return dic
