#__author: Liu Zheng
#date:2018/6/24




shopping = {'coffee':32.,'iphone':5000,'bike':1000,'mac':9000,'python book':105}

def goods_list():
    for i,v in enumerate(shopping,1):
        print(i,v)

def add():
    pass


saving = input('input your money')
if saving.isdigit():
    saving = int(saving)

goods_list()