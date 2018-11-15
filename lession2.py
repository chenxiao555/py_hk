#!/usr/bin/python3
#练习
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print('%s×%s=%-2d'%(i,j,i*j),end=' ')
    print()

for i in range(1,10):
    for j in range(1,10):
        print('%s×%s=%-2d'%(i,j,i*j),end=' ')
        if i<=j:
            break
    print()

#方法1
for i in range(1,10):
    for j in range(1,i+1):
        print('%s×%s=%-2d'%(i,j,i*j),end=' ')
    print()

for i in range(1,10):
    for j in range(1,11-i):
        print('%s×%s=%-2d'%(10-i,j,(10-i)*j),end=' ')
    print()

#方法2
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d×%d=%-2d'%(i,j,j*i),end=' ')
        j += 1
    print()
    i += 1

i = 9
while i >= 1:
    j = 1
    while j <= i:
        print('%d×%d=%-2d'%(i,j,j*i),end=' ')
        j += 1
    print()
    i -= 1
