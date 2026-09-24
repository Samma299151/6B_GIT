# 消費税の計算

# 金額は整数、税率は少数10%=0.1
def add_tax(price, tax_rate):
    return int(price + price * tax_rate)

# ↓mainに関数を呼び出されても動かない＝このファイルの呼び出しのみ動く
if __name__ == "__main__": 
    assert add_tax(1000, 0.1) == 1100 #一般
    print(add_tax(1000, 0.08)) #税減税率

    # assert == 計算結果　間違っているときのみエラーがでる
    # print 計算結果が出るためあっているかどうかを確認する必要がある