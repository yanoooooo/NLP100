# encoding: utf-8
import pycolor
import sys
import os

title = pycolor.GREEN
title += "17. １列目の文字列の異なり"
title += "\n"
title += "  1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．"
title += pycolor.END

print(title)

filename = "datas/hightemp.txt"
li = []

for line in open(filename):
  arr = line.split("\t")
  li.append(arr[0])

li = set(li)
li = sorted(li)

for x in li:
  print(x)

print("[command]")
os.system("cut -f1 %s | sort | uniq" % (filename))
