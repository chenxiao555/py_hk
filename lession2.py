#!/usr/bin/python3
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

for i in range(1,10):
    for j in range(1,i+1):
        print('%s×%s=%-2d'%(i,j,i*j),end=' ')
    print()

i = 9
while i >= 1:
    j = 1
    while j <= i:
        print('%d×%d=%-2d'%(i,j,j*i),end=' ')
        j += 1
    print()
    i -= 1
