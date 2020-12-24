import os

print("主（父）进程启动-%d" % (os.getpid()))
print("主（父）进程启动-%s" % (os.getpid()))
print(type(os.getpid()))
