"""test.py
    Created by Aaron at 09-Apr-20"""
a='a##c'
s=a[:0]+a[2:]
print(s)
print(s[0])
t=s[:-1]+a[2:]
print(t)

s='123'
print(s)
x=1
s=s[x:]+s[:x]
print(s)
y=2
s=s[-y:]+s[:-y]
print(s)
a=[1,2,3,4,5]
for x in reversed(range(len(a))):
    print(a[x])