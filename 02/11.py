# encoding: utf-8
import pycolor
import os

title = pycolor.GREEN
title += "11. タブをスペースに置換"
title += "\n"
title += "  タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，"
title += "\n"
title += "  trコマンド，もしくはexpandコマンドを用いよ．"
title += pycolor.END

print(title)

filename = "datas/hightemp.txt"
new_file = "datas/hightemp_space.txt"

f = open(new_file, 'w')

for line in open(filename):
    l = line.replace("\t", " ")
    f.write(l)

f.close()

os.system("cat %s | sed -e 's/\t/ /g'" % filename)