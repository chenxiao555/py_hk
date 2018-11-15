#!/usr/bin/python3
#练习
stu1={'sid':'1','name':'zhangsan','age':'20','classid':'python01'}
stu2={'sid':'2','name':'lisi','age':'21','classid':'python02'}
stu3={'sid':'3','name':'zhaowu','age':'22','classid':'python03'}

stu=[]
stu.append(stu1)
stu.append(stu2)
stu.append(stu3)



top="============ 学员管理系统 ============\n   1.查看学员信息      2.添加学生信息\n   3.删除学员信息      4.退出系统"
top1="============ 学员信息浏览 ============"
top2="|{:4}|{:12}|{:4}|{:10}|".format('sid','name','age','classid')
top3="------------------------------------"
top4="============ 添加学员信息 ============"
top5="============ 删除学员信息 ============"
foot="============== 再见！ =============="


def prstu():
    a = 0
    while a < len(stu):
        print(" |{:4}|{:12}|{:4}|{:10}|".format(stu[a].get('sid'), stu[a].get('name'), stu[a].get('age'),
                                                stu[a].get('classid')))
        a += 1

def df(j):
    while 1>=0:
        if j.strip() == '':
            break
        else:
            print("请不要输入字符！")
            j = input("按回车键继续：")

def ag(age):
    while 1>0:
        if age.isdigit():
            return age
            break
        else:
            age = input("学员年龄只能输入数字，请输入学员年龄：")
            return age




i='0'
while 1 >= 0 :
    if i.strip()=='0':
        print(top)
        i=input("====================================\n请输入对应的选择：")
    if i.strip()=='1':
        print(top1,"\n",top2,"\n",top3)
        prstu()
        j = input("按回车键继续：")
        df(j)
        i = '0'
    if i.strip()=='2':
        print(top4)
        name=input("请输入学员姓名：")
        age=input("请输入学员年龄：")
        age=ag(age)
        classid=input("请输入学员班级号：")
        stuu={'sid':str(len(stu)+1),'name':name,'age':age,'classid':classid}
        stu.append(stuu)
        j = input("学员信息添加成功，按回车键继续：")
        df(j)
        i = '0'
    if i.strip()=='3':
        print(top5,"\n",top2,"\n",top3)
        prstu()
        sid1=input("请输入要删除学员信息的需要sid：")
        del (stu[int(sid1.strip())-1])
        print(" ",top2, "\n", top3)
        prstu()
        j = input("学员信息删除成功，按回车键继续：")
        df(j)
        i = '0'
    if i.strip() == '4':
        print(foot)
        break
    if i.strip() == '':
        i = input("请输入对应的选择：")







