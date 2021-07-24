def find_lcsubstr(str1, str2):
    m = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    # max表示最长字符串长度
    max = 0
    # p表示str1的最后一个元素
    p = 0
    for x in range(len(str1)):
        for y in range(len(str2)):
            if str1[x] == str2[y]:
                m[x + 1][y + 1] = m[x][y] + 1
                if m[x + 1][y + 1] > max:
                    max = m[x + 1][y + 1]
                    p = x + 1
    return str1[p - max:p], max


# def find_lcsubstr(s1, s2):
# 	m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  #生成0矩阵，为方便后续计算，比字符串长度多了一列
# 	mmax=0   #最长匹配的长度
# 	p=0  #最长匹配对应在s1中的最后一位
# 	for i in range(len(s1)):
# 		for j in range(len(s2)):
# 			if s1[i]==s2[j]:
# 				m[i+1][j+1]=m[i][j]+1
# 				if m[i+1][j+1]>mmax:
# 					mmax=m[i+1][j+1]
# 					p=i+1
# 	return s1[p-mmax:p],mmax   #返回最长子串及其长度

print(find_lcsubstr('abcdfges', 'abdfgse'))
