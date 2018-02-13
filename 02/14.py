# encoding: utf-8
import pycolor
import sys
import os

title = pycolor.GREEN
title += "14. 先頭からN行を出力"
title += "\n"
title += "  自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．"
title += "\n"
title += "  確認にはheadコマンドを用いよ．"
title += pycolor.END

print(title)

argvs = sys.argv

if len(argvs) != 2:
  print("Please input integer.")

try:
  n = int(argvs[1])
  filename = "datas/hightemp.txt"
  f = open(filename)
  for i in range(0, n):
    print(f.readline(), end='')
  f.close()
except:
  print("Invalid Error.")

print("[command]")
os.system("head -n %s %s" % (n, filename))