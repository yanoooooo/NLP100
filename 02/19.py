# encoding: utf-8
import pycolor
import sys
import os

title = pycolor.GREEN
title += "19. 各行の1カラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる"
title += "\n"
title += "  各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．"
title += "\n"
title += "  確認にはcut, uniq, sortコマンドを用いよ．"
title += pycolor.END

print(title)

filename = "datas/hightemp.txt"
dic = {}

for line in open(filename):
  arr = line.split("\t")
  dic[arr[0]] = dic.get(arr[0], 0)+1

# valueのsort
for k, v in sorted(dic.items(), key=lambda x: -x[1]):
  print(str(k) + ": " + str(v))

print("[command]")
os.system("cut -f1 %s | sort | uniq -c | sort -nr" % (filename))
