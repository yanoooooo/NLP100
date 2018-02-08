# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "01.「パタトクカシーー」"
title += "\n"
title += "  「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．"
title += pycolor.END

print(title)

str = u"パタトクカシーー"

print(str[0]+str[2]+str[4]+str[6])

print(str[::2])