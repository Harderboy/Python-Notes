import itertools
import time

# mylist = list(itertools.product("0123456789", repeat=3))
passwd = ("".join(x) for x in itertools.product("0123745689", repeat=3))

# print(mylist)
# print(len(mylist))

while True:
    try:
        str = next(passwd)
        time.sleep(0.5)
        print(str)
    except StopIteration:
        break
