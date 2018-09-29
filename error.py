# try:
#     f=open('e.txt','r')
#     f.write('hi world')
# except IOError:  #only except for any kind of error as 'except:'
#     print('errrrrror')
# else:
#     print('ok')
try:
    f=open('e.txt','r')
    f.write('hi world')
except IOError:  #only except for any kind of error as 'except:'
    print('errrrrror')
finally:
    print('ok')
