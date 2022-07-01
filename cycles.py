# 以下にジェネレータ関数cyclesを定義してください。
# %%
def cycles(s):
    word_list = s.split(' ')
    while True:
        for w in word_list:
            yield w
            