#__author: Liu Zheng
#date:2018/6/20


name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit(): #判断是否为数字
	salary = int(salary)

# else:
# 	age=input("must input digit Salary=")

msg = '''

----- info of %s------
Name : %s
Age : %s
Job : %s
Salary : %s
You will be retierd in %s years
------- End ----------
''' % (name,name,age,job,salary,65-age)

print(msg)