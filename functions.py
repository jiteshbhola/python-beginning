# def MyFunc():
#     print('my first function')
# MyFunc()
# def my(param='world'):
#     '''
#     Lorem ipsum dolor sit amet
#     '''
#     print('hello {}'.format(param))
# my()

# print('\n')
# print('print vs return')
# def add(num1,num2):
#     if type(num1)==type(num2)==type(10):
#         return num1+num2
#     else:
#         print('integers required')
# r=add(2,2)
# print(r)
# print('\n')
# print('lamba expr')
# alist=[1,2,3,4,5,6,7,8,9]
# def func(num):
#     return num%2==0
# a=filter(func,alist)
# print(list(a))
# print('\n')
print('------------------------FUNCTIONS EXERCISE----------------------------------------')
print('\n')
print('-----------------------------PROBLEM 1-------------------------------------------')
# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
#             return True
#     return False
# a=arrayCheck([1,2,3,3,4,5,6,7,5])
# print(a)
print('\n')
print('-----------------------------PROBLEM 2-------------------------------------------')
# def stringBits(stringg):
#     result=""
#     for i in range(len(stringg)):
#       if i % 2 == 0:
#         result = result + stringg[i]
#     return result
# a=stringBits('Heeololeo')
# print(a)
print('\n')
print('-----------------------------PROBLEM 3-------------------------------------------')
# def end_other(a, b):
#     a=a.lower()
#     b=b.lower()
#     if (b.endswith(a) or a.endswith(b))==True:
#         return True
#     else:
#         return False
# q=end_other('hiabaa','abaa')
# print(q)
print('\n')
print('-----------------------------PROBLEM 4-------------------------------------------')
# def doubleChar(mystr):
#     r=''
#     for char in mystr:
#         r += char * 2
#     return r
# q=doubleChar('hihi')
# print(q)
print('\n')
print('-----------------------------PROBLEM 5-------------------------------------------')
# def no_teen_sum(a,b,c):
#         return fix_teen(a) + fix_teen(b) + fix_teen(c)
# def fix_teen(n):
#      if n in [13,14,17,18,19]:
#             return 0
#      return n
# q= no_teen_sum(18,17,3)
# print(q)
print('\n')
print('-----------------------------PROBLEM 6-------------------------------------------')
