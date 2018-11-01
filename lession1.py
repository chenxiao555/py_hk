#!/usr/bin/python3
aa=input("hahaha:")
print("aa="+aa)
bb="横：{}；竖：{}".format(aa,20)
print("bb="+bb)
cc="{:.2f}".format(7.3363)
print("cc="+cc)
dd="{:b}".format(100)
ee="{:x}".format(100)
ff="{:8}:{:8}".format(aa,cc)
gg="{:>8}:{:>8}".format(aa,cc)
print("dd:",dd,";ee:",ee,";ff:",ff,";gg:",gg)
print("="*20)
#注释111
a=b=c=1
d,e,f=1,2,"demo"
print("a:",a,"b:",b,"c:",c,"d:",d,"e:",e,"f:",f)

if aa==1:
    print("true")
else:
    print("false",aa)


