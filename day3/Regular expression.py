#__author: Liu Zheng
#date:2018/7/7

import re
str = 'hello world'
# print(str.find('ll'))

#string 提供的方法是完全匹配
#引入正则：模糊匹配

#print(re.findall('l',str))

# 元字符： .  ^  $  ?  *

#.通配符：只能代指一个任意字符  换行符除外

# # ^  只匹配开头
# ret = re.findall('^h...o','hfasddasdhello')
# print(ret)
#
# #$ 只匹配结尾
# ret = re.findall('h...o$','hfasddasdhello')
# # #* 重复匹配  重复前面的匹配 0 ~ 无穷
#
# ret = re.findall('ba*','fasfafdasbaaaaaaaaaaaa')
# print(ret)
#
# ret = re.findall('.*','fasfafdasbaaaaaaaaaaaa')
# print(ret)
# #['fasfafdasbaaaaaaaaaaaa', '']
# ret = re.findall('.*?','fasfafdasbaaaaaaaaaaaa')
# print(ret)
# + 重复匹配 1 ~ 无穷
# ret = re.findall('a+','fsdfsdgsdffsdfafaa')
# print(ret)

#? [0,1]
# ret = re.findall('a?b','fsdfsdgsdffsdfafb')     #0~1 个a
# print(ret)

#{n}重复n次匹配

#ret = re.findall('a{5}b','aaaaaaabbbbbbb')
# ret = re.findall('a{1,3}','aaabbbbbbb')
# print(ret)

# *等于{0~无穷} + 等于{1~无穷} ?等于{0，1}

#[] 字符集
# re.findall()

# ^放在[]意味着取反

# \