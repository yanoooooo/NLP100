# encoding: utf-8
import pycolor
import sys
import os

title = pycolor.GREEN
title += "18. 各行を3カラム目の数値の降順にソート"
title += "\n"
title += "  各行を3カラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．"
title += "\n"
title += "  確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．"
title += pycolor.END

print(title)

filename = "datas/hightemp.txt"
arr = []

for line in open(filename):
  arr.append(line.split("\t"))

arr = sorted(arr, key=lambda x:x[2], reverse=False)

for a, b, c, d in arr:
  print("%s %s %s %s" % (a, b, c, d), end='')

print("[command]")
os.system("sort -k3,3n %s" % (filename))