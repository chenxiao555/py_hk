#!/usr/bin/python3
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print('%s×%s=%s'%(i,j,i*j),end=' ')
    print()

for i in range(1,10):
    for j in range(1,10):
        print('%s×%s=%s'%(i,j,i*j),end=' ')
        if i<=j:
            break
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print('%s×%s=%s'%(i,j,i*j),end=' ')
    print()