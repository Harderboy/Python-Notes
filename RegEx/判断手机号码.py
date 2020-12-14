def checkPhoneNumber(str):
    if len(str) != 11:
        return False
    elif str[0] != '1':
        return False
    # 省略列举其他条件
    elif str[1:3] != "30":
        return False

    for i in range(3, 11):
        if str[i] < '0' or str[i] > '9':
            return False
    return True


if __name__ == "__main__":
    str = "13022364644"
    res = checkPhoneNumber(str)
    print(res)