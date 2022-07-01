# 課題5

## 5-1

次のようなジェネレータcycles関数を定義したスクリプトcycles.pyを作成してください。このジェネレータ関数はジェネレータオブジェクト作成のさいに文字列(英文)を一つだけ引数にとります。作成したジェネレータオブジェクトは、`next`を作用させるたびに、最初にジェネレータ関数に渡した英文の内容を1単語ずつ返してくれます。ただし、**ここでの単語とは、空白(もしくは文頭)と空白(もしくは文末)で囲まれた部分文字列を指すこととします**。文字列の最後まで到達すると、最初の単語に戻ります。

このジェネレータは例えば次のように使います。

```python
from cycles import *
cy = cycles('My name is Taro.')
for i in range(20):
    print(next(cy))
```

出力は以下のようになります。

```bash
#出力
My
name
is
Taro.
My
name
is
Taro.
My
name
is
Taro.
My
name
is
Taro.
My
name
is
Taro.
```

## 5-2

クロージャに関する課題です。英単語を一つ引数にとり、これまで引数に渡した全ての単語を繋いだ文字列を返すクロージャcljoinを定義したスクリプトcljoin.pyを作成しなさい。ただし単語をつなぐさいは間に空白文字を一文字挟むこととします。このスクリプトは次のように使います。

```python
# %%
from cljoin import *
cl = cljoin()
print(cl('My'))
print(cl('name'))
print(cl('is'))
print(cl('Taro.'))
```

```bash
#出力
My
My name
My name is
My name is Taro.
```
