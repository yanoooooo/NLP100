# encoding: utf-8
import pycolor

title = pycolor.GREEN
title += "07. テンプレートによる文生成"
title += "\n"
title += "  引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．"
title += "\n"
title += "  さらに，x=12, y=\"気温\", z=22.4として，実行結果を確認せよ．"
title += pycolor.END

print(title)

def making_str(x, y, z):
    s = str(x)+"時の"+y+"は"+str(z)
    #s = "%s時の%sは%s" % (x, y, z)
    return s

print(making_str(12, "気温", 22.4))