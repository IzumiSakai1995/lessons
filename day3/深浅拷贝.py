#__author: Liu Zheng
#date:2018/7/6

#浅拷贝
#修改不可变对象
# s = [1,'liuzheng','Joe']
# s1 = s.copy()
# s1[0] = 2
# print(s,s1)
# result :[1, 'liuzheng', 'Joe'] [2, 'liuzheng', 'Joe']
#
#修改可变对象
# a = [[1,2],3,4]
# b = a.copy()
# b[0][0] = 3
# print(a,b)
# result : [[3, 2], 3, 4] [[3, 2], 3, 4]

#深拷贝
# import copy
# a = [[1,2],3,4]
# b = copy.copy(a)
# c = copy.deepcopy(a)


