# 以下にクロージャcljoinを定義してください。
# %%
def cljoin():
    s = ''
    def inner(w):
        nonlocal s
        if s == '':
            s = s + w
        else:
            s = s + ' ' + w
        return s
    return inner
'''
注: クロージャの名前空間で定義されている
文字列sが空文字（初期状態)のときと、それ
以外の場合で文字列連結の処理を分けるのが
ポイントです。
'''
