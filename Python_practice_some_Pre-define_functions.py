

l = [2,18,22,17,24,8,12,27]

print(list(filter(lambda x:x%3==0,l)))
[18, 24, 12, 27]

l
Out[19]: [2, 18, 22, 17, 24, 8, 12, 27]

def fil(x):
    for i in range(0,len(x)):
        if x[i]%3==0:
            print(x[i])
            

fil(l)
18
24
12
27

print(list(map(lambda x:x*2+10,l)))
[14, 46, 54, 44, 58, 26, 34, 64]

l
Out[23]: [2, 18, 22, 17, 24, 8, 12, 27]

print(list(reduce(lambda x,y:x+y,l)))
Traceback (most recent call last):

  File "<ipython-input-24-cd3a44fd6142>", line 1, in <module>
    print(list(reduce(lambda x,y:x+y,l)))

NameError: name 'reduce' is not defined




from functools import reduce

print(list(reduce(lambda x,y:x+y,l)))
Traceback (most recent call last):

  File "<ipython-input-26-cd3a44fd6142>", line 1, in <module>
    print(list(reduce(lambda x,y:x+y,l)))

TypeError: 'int' object is not iterable




print(reduce(lambda x,y:x+y,l))
130

a=[1,2,5,2,4,5,2,4,5,2]

b=[1,2,5,3,6,9,3,8,94,5,1]

a&b
Traceback (most recent call last):

  File "<ipython-input-30-c5273c79eea7>", line 1, in <module>
    a&b

TypeError: unsupported operand type(s) for &: 'list' and 'list'




a=set(a)

a
Out[32]: {1, 2, 4, 5}

a&set(b)
Out[33]: {1, 2, 5}

list(a&set(b))
Out[34]: [1, 2, 5]



def common(x,y):
    z=list(set(x)&set(y));
    return z


a=[4,5,6,5,4,6,8,4,5]

b=[4,5,0,2,1,3,5,4,8]

common(a,b)
Out[38]: [8, 4, 5]

dif fib(n):
  File "<ipython-input-39-370ddf9d3db9>", line 1
    dif fib(n):
          ^
SyntaxError: invalid syntax




def fib(n):
    a,b=2,3
    while a<n:
        print(b+1, end=" ")
        a,b = b, a+b
        

fib(50)
4 6 9 14 22 35 56 

a="Datasoft Systems Bangladesh Limited"

list(a)
Out[43]: 
['D',
 'a',
 't',
 'a',
 's',
 'o',
 'f',
 't',
 ' ',
 'S',
 'y',
 's',
 't',
 'e',
 'm',
 's',
 ' ',
 'B',
 'a',
 'n',
 'g',
 'l',
 'a',
 'd',
 'e',
 's',
 'h',
 ' ',
 'L',
 'i',
 'm',
 'i',
 't',
 'e',
 'd']

a
Out[44]: 'Datasoft Systems Bangladesh Limited'

split(a," ")
Traceback (most recent call last):

  File "<ipython-input-45-c6e78f6f47bd>", line 1, in <module>
    split(a," ")

NameError: name 'split' is not defined




a.split(" ")
Out[46]: ['Datasoft', 'Systems', 'Bangladesh', 'Limited']

b=a.split(" ")

b
Out[48]: ['Datasoft', 'Systems', 'Bangladesh', 'Limited']

c=list(map(lambda x:len(x),b))

c
Out[50]: <map at 0x1895a91a908>

c=map(lambda x:len(x),b)