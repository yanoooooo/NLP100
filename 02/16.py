# encoding: utf-8
import pycolor
import sys
import os

title = pycolor.GREEN
title += "16. ファイルをN分割する"
title += "\n"
title += "  自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．"
title += "\n"
title += "  同様の処理をsplitコマンドで実現せよ．"
title += pycolor.END

print(title)

argvs = sys.argv
filename = "datas/hightemp.txt"
output = "datas/split."
os.system("rm %s*" % output)

if len(argvs) != 2:
  print("Please input integer.")

num = 0
wf = open(output+str(num)+".txt", "w")
try:
  n = int(argvs[1])
  ef = open(filename)
  lines = ef.readlines()

  for i in range(0, len(lines)):
    if i%n == 0 and i != 0:
      wf.close()
      num = num+1
      wf = wf = open(output+str(num)+".txt", "w")
    wf.write(lines[i])
  wf.close()
except:
  print("Invalid Error.")

print("[command]")
os.system("split -l %s %s %s" % (n, filename, output))