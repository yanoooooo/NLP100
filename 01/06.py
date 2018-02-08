# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "06. 集合"
title += "\n"
title += "  \"paraparaparadise\"と\"paragraph\"に含まれる文字bi-gramの集合を，それぞれ,"
title += "\n"
title += "  XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．"
title += pycolor.END

print(title)

def n_gram(s, n):
  # リストだと、集合演算ができない
  #result = [tuple(s[i:i+n]) for i in range(len(s)-n+1)]
  result = {tuple(s[i:i+n]) for i in range(len(s)-n+1)}
  return result

X = n_gram("paraparaparadise", 2)
Y = n_gram("paragraph", 2)

print("X: %s" % X)
print("Y: %s" % Y)

# 和集合
print("union: %s" % X.union(Y))
print("union: %s" % str(X|Y))

#積集合
print("intersection: %s" % X.intersection(Y))
print("intersection: %s" % str(X&Y))

#差集合
print("difference: %s" % X.difference(Y))
print("difference: %s" % str(X-Y))

#seが含まれるか
#タプルの比較には、比較演算子を使う！！！！
print("'se' is included in X: " + str(n_gram("se", 2) <= X))
print("'se' is included in Y: " + str(n_gram("se", 2) <= Y))

if n_gram("se", 2) <= X: print("'se' is included in X.")
if n_gram("se", 2) <= Y: print("'se' is included in Y.")