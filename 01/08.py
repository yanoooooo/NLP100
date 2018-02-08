# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "08. 暗号文"
title += "\n"
title += "  与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．"
title += "\n"
title += "  ・英小文字ならば(219 - 文字コード)の文字に置換"
title += "\n"
title += "  ・その他の文字はそのまま出力"
title += "\n"
title += "  この関数を用い，英語のメッセージを暗号化・復号化せよ．"
title += pycolor.END

print(title)

def cipher(s):
  result = ""
  for c in s:
    if c.islower():
      result += chr(219-ord(c))
    else:
      result += c
  return result


#def cipher(s): return "".join(chr(219-ord(c)) if c.islower() else c for c in s)

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine."
print(cipher(s))
print(cipher(cipher(s)))