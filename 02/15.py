# encoding: utf-8
import pycolor
import sys
import os

title = pycolor.GREEN
title += "15. 末尾のN行を出力"
title += "\n"
title += "  自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．"
title += "\n"
title += "  確認にはtailコマンドを用いよ．"
title += pycolor.END

print(title)

argvs = sys.argv

if len(argvs) != 2:
  print("Please input integer.")

try:
  n = int(argvs[1])
  filename = "datas/hightemp.txt"
  f = open(filename)
  lines = f.readlines()
  l = len(lines)

  for i in range(l-n, l):
    print(lines[i], end='')
  f.close()
except:
  print("Invalid Error.")

print("[command]")
os.system("tail -n %s %s" % (n, filename))