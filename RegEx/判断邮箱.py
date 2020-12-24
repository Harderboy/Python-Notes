import re

r'''
liuhengcs@gmail.com
l53002@email.swu.edu.cn
201944085211043@cuc.edu.cn
liuheng_19@cuc.edu.cn
liuhengcsc@163.com

gaozihang-001@gmail.com 只允许英文字母、数字、下划线、英文句号、以及中划线组成:
^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$

高子航001Abc@bowbee.com.cn 名称允许汉字、字母、数字，域名只允许英文域名:
^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$
'''
