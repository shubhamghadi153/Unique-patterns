n = 5

for i in range(1,n+1):
    for j in range(n):
        print(i, end=' ')
    print()
print('----'*10)
for i in range(1,n+1):
    for j in range(n-i):
        print(' ', end='')
    for j in range(i):
        print(i,end=' ')
    print()
print('----'*10)
for i in range(1,n):
    for j in range(1,n+1):
        print(j,end=' ')
    print()
print('----'*10)

print('----'*10)
n = 5+1
for i in range(1,n):
    for j in range(i,n):
        print(j,end=' ')
    print()
print('----'*10)

for i in range(1,n):
    for j in range(n-i):
        print(' ', end=' ')
    for j in range(i):
        print(n-i,end=' ')
    print()

print('----'*10)
n= 6
for i in range(1,n):
    for j in range(1,n):
        if i == j :
            print(i,end=' ')
        else:
            print('-',end=' ')
            
    for k in range(1,n-1):
        if k==i:
            print(i, end=' ')
        else:
            print('-', end=' ')

    print()
print('----'*10)
n = 5

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(i,end=' ')
        else:
            print(' ',end=' ')
    for k in range(i,n-1):
        print(' ',end=' ')
    for l in range(i,n):
        if l==i:
            print(i,end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(1,n):
    for j in range(1,n-i):
        print(' ', end=' ')
    for k in range(n):
        if k==i:
            print(n-i,end=' ')
    for j in range(i):
        print(' ', end=' ')
    for j in range(1,n+1):
        if i==j:
            print(n-i,end=' ')
        else:
            print(' ', end=' ')
    print()
print('+++++'*15)   
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('m',end=' ')
        else:
            print(' ',end=' ')
    for k in range(i,n-1):
        print(' ',end=' ')
    for l in range(i,n):
        if l==i:
            print('1',end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(1,n):
    for j in range(1,n-i):
        print(' ', end=' ')
    for k in range(n):
        if k==i:
            print('k',end=' ')
    for j in range(i):
        print(' ', end=' ')
    for j in range(1,n+1):
        if i==j:
            print('l',end=' ')
        else:
            print(' ', end=' ')
    print()
print('+++++'*15)
n= 10

for i in range(n):
    for j in range(n):
        if i==j or i==n-1 or i==0 or j==n:
            print('$', end=' ')
        else:
            print('-', end=' ')
    print()
print('----'*15)
for i in range(n):
    for j in range(n):
        if i ==0 or j ==0 or j==n-1 or i==n-1 or i==3 or j ==3 or i==n-4 or j==n-4 :
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()

print('----'*15)
n = 7
for i in range(n):
    for j in range(n):
        if i ==0 or j ==0 or j==n-1 or i==n-1 :
            print('$', end=' ')
        elif i==3 or j ==3 or i==1 and j ==1 or j==n-2 and i==1 or i==n-2 and j==1 or i==n-2 and j==n-2 :
            print(' ', end=' ')
        else:
            print('*', end=' ')
        
    print()
print('@-'*10)

n = 6

for i in range(1,n):
    for j in range(1,n):
        if i%2==0 or j%2==0:
            print(2,end=' ')
        else:
            print(1,end=' ')
    print()

print('@-'*10)

n =7
m=int(7/2)

print(type(m))
print(m)
for i in range(n):
    for j in range(n): 
        if i==1 and j==1 or i==1 and j==n-2 or j==1 and i == n-2 or j==n-2 and i==n-2  or i==m or j==m:
            print(' ', end=' ')
        else:
            print('*',end=' ')
    print()




        