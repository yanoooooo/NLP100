# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "00. 文字列の逆順"
title += "\n"
title += "  文字列\"stressed\"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．"
title += pycolor.END

print(title)

str = "stressed"

print(str)
print(str[::-1])