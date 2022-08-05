# %%
from cycles import *
cy = cycles('My name is Taro.')
for i in range(20):
    print(next(cy))

# %%
from cljoin import cljoin
cl = cljoin()
print(cl('My'))
print(cl('name'))
print(cl('is'))
print(cl('Taro.'))


# %%
from cljoin import cljoin2
cl2 = cljoin2()
print(cl2('My'))
print(cl2('name'))
print(cl2('is'))
print(cl2('Taro.'))


# %%
