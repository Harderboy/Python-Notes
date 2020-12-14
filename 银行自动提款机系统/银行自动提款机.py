# 银行自动提款机系统

# 人
# 类名：Person
# 属性：姓名、身份证、电话号、卡
# 行为：

# 卡
# 类名：Card
# 属性：卡号、密码、余额
# 行为：

# 银行
# 类名：bank
# 属性：用户列表、提款机

# 提款机
# 类名：ATM
# 属性：用户字典
# 行为：开户、查询、存款、取款、改密、解锁、锁定、补卡、销户、退出

# 管理员
# 类名：Admin
# 属性
# 行为：管理员界面、管理员验证、系统功能界面

from admin import Admin
from atm import ATM
import time


def main():
    # 界面对象
    admin = Admin()
    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():  # view.printAdminView()返回值为-1则进入函数，返回-1，返回值为0则继续向下进行
        return -1

    # 提款机对象
    atm = ATM()

    while True:
        admin.printSysFunctionView()
        # 等待用户的操作
        option = input("请输入您的操作：")
        if option == "1":
            # 开户
            atm.createUser()
        elif option == "2":
            # 查询
            atm.searchUserInfo()
        elif option == "3":
            # 取款
            pass
        elif option == "4":
            # 存储
            pass
        elif option == "5":
            # 转账
            pass
        elif option == "6":
            # 改密
            pass
        elif option == "7":
            # 锁定
            atm.lockUser()
        elif option == "8":
            # 解锁l
            atm.unlockUser()
        elif option == "9":
            # 补卡
            pass
        elif option == "0":
            # 销户
            pass
        elif option == "t":
            # 退出
            if not admin.adminOption():
                return -1

        time.sleep(1)


if __name__ == "__main__":
    main()