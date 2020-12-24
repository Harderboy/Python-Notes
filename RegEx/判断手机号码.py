import re


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


def checkPhoneNumber2(str):
    # 13022364644
    # pat = r'^1[34578]\d{9}$'
    pat = r'^1(3|4|5|6|7|8|9)\d{9}$'
    res = re.match(pat, str)
    return res


def checkPhoneNumber3(str):
    # pat = r'1(3|4|5|6|7|8|9)\d{9}'
    pat = r'1[3456789]\d{9}'
    res = re.findall(pat, str)
    return res


if __name__ == "__main__":
    str1 = "13022364644"
    str2 = "13912345678"
    str3 = "23912345678"
    # res1 = checkPhoneNumber(str1)
    # print(res1)
    res2 = checkPhoneNumber2(str2)
    print(res2)
    res3 = checkPhoneNumber2(str3)
    print(res3)
    res4 = checkPhoneNumber2(str1)
    print(res4)
    str4 = "adfkjakdf13022364644ajdfka15236512486dkfjakfjl"
    res5 = checkPhoneNumber3(str4)
    print(res5)
