import random
from card import Card
from user import User


class ATM(object):
    def __init__(self):
        self.allUsers = {}  # 卡号-用户

    # 开户
    def createUser(self):
        # 向用户字段中添加一对键值对（卡号-用户）
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号：")
        phone = input("请输入您的电话密码：")

        prestoreMoney = int(input("请输入您的预存款："))
        if prestoreMoney < 0:
            print("预存款输入有误！！！开户失败……")
            return -1

        onePasswd = input("请设置密码：")
        # 验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！！开户失败……")
            return -1

        cardId = self.randomCardId()
        # print(cardId)

        # 用户所有需要的信息就全了
        cardStr = self.randomCardId()

        card = Card(cardStr, onePasswd, prestoreMoney)
        user = User(name, idCard, phone, card)

        # 存到字典
        self.allUsers[cardStr] = user
        print("开户成功！！请牢记卡号{}".format(cardStr))

    # 查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")

        # 验证是否存在卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！查询失败……")
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡号已被锁定！！请解锁后再使用其他功能……")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作……")
            user.card.cardLock = True
            return -1
        print("账号：{}  余额：{}".format(user.card.cardId, user.card.cardMoney))

    # 取款
    def getMoney(self):
        pass

    # 存款
    def saveMoney(self):
        pass

    # 转账
    def transferMoney(self):
        pass

    # 改密码
    def changePasswd(self):
        pass

    # 锁定
    def lockUser(self):
        cardNum = input("请输入您的卡号：")

        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！锁定失败……")
            return -1

        if user.card.cardLock:
            print("该卡号已被锁定！！请解锁后再使用其他功能……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！锁定失败……")
            return -1

        tmpIdCard = input("请输入您的身份证号：")
        if tmpIdCard != user.idCard:
            print("身份证有误！！锁定失败……")
            return -1

        # 锁定
        user.card.cardLock = True
        print("锁定成功……")

    # 解锁
    def unlockUser(self):
        cardNum = input("请输入您的卡号：")

        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！锁定失败……")
            return -1

        if not user.card.cardLock:
            print("该卡号没有被锁定！！无需解锁……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！解锁失败……")
            return -1

        tmpIdCard = input("请输入您的身份证号：")
        if tmpIdCard != user.idCard:
            print("身份证有误！！解锁失败……")
            return -1

        # 解锁
        user.card.cardLock = False
        print("解锁成功……")

    # 补卡
    def newCard(self):
        pass

    # 销户
    def killUser(self):
        pass

    # 验证密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                print("密码输入正确！")
                return True
            # print("输入密码有误，请重新输入……")
        # print("输入密码错误次数超过三次，操作失败")
        return False

    # 生成卡号
    def randomCardId(self):

        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch

            # 判断卡号是否重复
            if not self.allUsers.get(str):
                return str
