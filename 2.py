# count = 1
# while count <= 10:
#     print(count)
#     count += 1

'''#wap to ask user with name of student and store it in list'''
# std=[]
# n="y"

# while (n == "y" or n=="Y"):
#     name=input("enter the name of student :")
#     std.append(name)
#     n=input("do you want to continue? (y/n): ")
# print("the list of student \n")
# print(f"{std}")


'''#wap to ask user with the name of students until the last letter of name "a/A"'''
# std=[]
# while True:
#     name=input("enter the name of student :")
#     if (name[-1]=='a' or name[-1]=='A'):
#         break
#     std.append(name)
# print(std)

# name=[]
# stu='dummy'
# while (stu[-1]!="a"):
#     stu=input("enter the name of student :")
#     name.append(stu)
# print(name)


"""type"""

# x=[1,2,3,4,5,6]
# print(type(x))

# y={1,2,3,4,5}
# print(type(y))

# z=1,
# print(type(z))

# a={}
# print(type(a))

# b=()
# print(type(b))


'''function'''

# def add(a,b):
#     sum=a+b
#     return sum
# print(add(45,2))

'''wap to ask user with 3 number and choose operator (+-*/)'''
def calc():

    num1=int(input("enter the 1st number: "))
    num2=int(input("enter the 2nd number: "))
    num3=int(input("enter the 2nd number: "))

    op=input("enter the operator (+,-,*,/): ")


    if (op=='+'):
        result=num1+num2+num3
    elif (op=='-'):
        result=num1-num2-num3
    elif (op=='*'):
        result=num1*num2*num3
    elif (op=='/'):
        if num2!=0 and num3!=0:
            result=num1/num2/num3
        else:
            print("Error: Division by zero")
            return 
    else:
        print("Error: Invalid operator")
        return
    print(f"the result is: {result}")

calc()