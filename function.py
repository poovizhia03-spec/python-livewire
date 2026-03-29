#function

def add ():
    a=10
    b=20
    print(a+b)
add()


a=20#global
def add ():
    a=50#local
    b=20
    print(a+b)
add()

def add(v1,v2):#parameter
    print(v1+v2)
add(10,90)#argument

def cal(n1,n2):
    print("add:",n1+n2)
    print("sub:",n1-n2)
    print("mul:",n1*n2)
    print("div:",n1/n2)
n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
cal(n1,n2)

def palindrome(s):
    if s==s[ : : -1]:
        print("palindrome")
    else:
        print("not palindrome")
s=input("enter the number")
palindrome(s)

#return type
def add(a,b):
    return a+b
s=add(20,30)
print(s)
#with return with parameter
def function(a,b,c):
    return a+b+c
f=function(10,30,40)
print(f)
#without return with parameter
def fun(m,n,o):
    print(m+n+o)
fun(1,5,3)
#with return without parameter
def sum():
    k,l,m=2,4,6
    return k+l+m
u=sum()
print(u)
#without return without parameter
def run():
    print(10+110+10)
run()
#postional argument
def sub(s,m):
    print("sub=",s-m)
sub(15,10)
#default argument
def greet(name="guest"):
    print("welcome",name)
greet("poovi")
greet()
#key word argument
def student(name,age):
    print("name:",name)
    print("age:",age)
student("poovi",20)

def employee(name,age,role,salary):
    print("name:",name)
    print("age:",age)
    print("role:",role)
    print("salary:",salary)
employee(name="poovi",salary=20000,role="it",age=20)

#variable argumentt
def even (*n):
    for i in n:
        if i %2==0:
            print(i)
even(1,2,3,4,5,6,7,8,9,10)
def even (*n):
    for i in n:
        if i %2!=0:
            print(i)
even(1,2,3,4,5,6,7,8,9,10)
#for key and value
def employee_list(**emp):
    for i in emp:
        print(i,":",emp[i])
employee_list(id="poovi",id="kavi",id="doctor")

