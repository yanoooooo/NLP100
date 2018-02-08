# encoding: utf-8
import pycolor
import os

title = pycolor.GREEN
title += "13. col1.txtとcol2.txtをマージ"
title += "\n"
title += "  12で作ったcol1.txtとcol2.txtを結合し，"
title += "\n"
title += "  元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．"
title += "\n"
title += "  確認にはpasteコマンドを用いよ．"
title += pycolor.END

print(title)

col1 = "datas/col1.txt"
col2 = "datas/col2.txt"
result = "datas/col1_col2.txt"

f_col1 = open(col1)
f_col2 = open(col2)
f_result = open(result, "w")

for i,j in zip(f_col1, f_col2):
    i = i.strip()
    f_result.write(i+"\t"+j)

f_col1.close()
f_col2.close()
f_result.close()

os.system("paste %s %s" % (col1, col2))