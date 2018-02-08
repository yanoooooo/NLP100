# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "02. 「パトカー」＋「タクシー」＝「パタトクカシーー」"
title += "\n"
title += "  「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．"
title += pycolor.END

print(title)


str1 = u"パトカー"
str2 = u"タクシー"
result = u""

for i,j in zip(str1, str2): # zipを使うことで複数の変数を同時にループ可能
    result += i+j

print(result)