# encoding: utf-8

# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def making_str(x, y, z):
    s = str(x)+"時の"+y+"は"+str(z)
    #s = "%s時の%sは%s" % (x, y, z)
    return s

print making_str(12, "気温", 22.4)