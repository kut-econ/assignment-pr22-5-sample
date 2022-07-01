# %%
from cycles import *
cy = cycles('My name is Taro.')
for i in range(20):
    print(next(cy))

# %%
from cljoin import *
cl = cljoin()
print(cl('My'))
print(cl('name'))
print(cl('is'))
print(cl('Taro.'))

