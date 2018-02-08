# encoding: utf-8
import pycolor
import os

title = pycolor.GREEN
title += "10. 行数のカウント"
title += "\n"
title += "  行数をカウントせよ．確認にはwcコマンドを用いよ．"
title += pycolor.END

print(title)

filename = "datas/hightemp.txt"

print(sum(1 for line in open(filename)))

os.system("wc -l %s" % filename)