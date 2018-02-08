# encoding: utf-8
import pycolor
import os

title = pycolor.GREEN
title += "12. 1列目をcol1.txtに，2列目をcol2.txtに保存"
title += "\n"
title += "  各行の1列目だけを抜き出したものをcol1.txtに，"
title += "\n"
title += "  2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．"
title += "\n"
title += "  確認にはcutコマンドを用いよ．"
title += pycolor.END

print(title)

filename = "datas/hightemp.txt"
col1 = "datas/col1.txt"
col2 = "datas/col2.txt"

f_col1 = open(col1, 'w')
f_col2 = open(col2, 'w')

for line in open(filename):
    arr = line.split("\t")
    f_col1.write(arr[0]+"\n")
    f_col2.write(arr[1]+"\n")

f_col1.close()
f_col2.close()

#os.system("cut -f1,2 %s" % filename)
print("【1列目】")
os.system("cut -f1 %s" % filename)
print("【2列目】")
os.system("cut -f2 %s" % filename)