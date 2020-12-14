import time


class Admin(object):
    '''
    def __init__(self, admin):
        self.__admin = admin
    '''

    admin = '1'
    passwd = '1'

    def printAdminView(self):
        print("****************************************")
        print("*                                      *")
        print("*                                      *")
        print("*          欢迎登陆tomato银行          *")
        print("*                                      *")
        print("*                                      *")
        print("****************************************")

    def printSysFunctionView(self):
        print("******************************************")
        print("*      开户（1）          查询（2）      *")
        print("*      取款（3）          存款（4）      *")
        print("*      转帐（5）          改密（6）      *")
        print("*      锁定（7）          解锁（8）      *")
        print("*      补卡（1）          销户（10）     *")
        print("*                退出（t）               *")
        print("******************************************")

    def adminOption(self):
        inputAdmin = input("请输入管理员帐号：")
        if self.admin != inputAdmin:
            print("输入账号有误！")
            return -1

        inputPasswd = input("请输入管理员账号：")
        if self.passwd != inputPasswd:
            print("输入密码有误！")
            return -1

        print("操作成功！请稍后......")
        time.sleep(1)
        return 0
