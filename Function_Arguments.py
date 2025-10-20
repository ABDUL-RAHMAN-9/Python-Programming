# ACTUAL ARGUMENTS

# Positional actual argument
def greeting(phno, msg):
    print("number:", phno)       # number: 1234567890
    print("message:", msg)       # message: dear customer your bill is 7500.55

greeting(1234567890, "dear customer your bill is 7500.55")


# Keyword actual argument
def message(to, msg):
    print("this email is for:", to)   # this email is for: example@gmail.com
    print("message:", msg)            # message: hello

message(msg="hello", to="example@gmail.com")
message("example123@yahoo.com", msg="hello")


# Default actual argument
def message(to="example@gmail.com", msg="hi user"):
    print("this email is for:", to)   # this email is for: example@gmail.com
    print("message:", msg)            # message: hi user

message()
message(msg="hello")


# var-len actual argument
def sum(*num):
    print(num)
    print(type(num))

sum(1, 2)
sum()
sum(1, 2, 3, 4)


# *arg (tuple type)
def sum(a, b, *arg):
    print(a, type(a))     # 1 <class 'int'>
    print(b, type(b))     # 2 <class 'int'>
    print(arg, type(arg)) # () <class 'tuple'>

sum(1, 2)
sum(1, 2, 3, 4, 5, 6, 7, 8, 9)


# **kwarg (dictionary type)
def sum(**arg):
    print(arg)
    print(type(arg))

sum(arg=(1, 2, 3, 4, 5, 6))
