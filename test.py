# import re
# import sys
# sudoCommands = 'ls /proc/net/bonding,uname,lsb_release,user/bin/ls /proc/net/bonding,hello'
# # sudoCommandPattern = '.*ls\\b'
# sudoCommandPattern = '.*ls\s'
# if sudoCommands:
#     splitCommands = sudoCommands.split(',')
#     for command in splitCommands:
#         if command.strip():
#             print 'command: %s' % command
#
#         if re.match(sudoCommandPattern.lstrip(), command.strip()):
#             print "Match %s is matched by privileged command pattern %s" % (command, sudoCommandPattern)
#
#         print '1111111111111111111111'

# successful_ins_n = []
# cred_args = ()
# args=()
# print "args[1]"
# if (args and (args[1] not in successful_ins_n)) or not args:
#         print "1"
#         for args in cred_args:
#             successful_ins_n.append(args[1])
#             print "2"
# x = set('spamm')
# y = set(['h','a','m'])
# print  x,y
# a=[1,23,4,5,33,1,1,4,5,33]
# b=set(a)
# c=[i for i in b]
# print b,c

# name = "whole global name"
# class Person:
#     name = "class global name"
#     def __init__(self,newPersonName):
#         self.name=newPersonName;
#     def sayYouname(self):
#         print "My name is %s"%self.name
# def selfAndInitDemo():
#     persionInstance =Person("molidong")
#     persionInstance.sayYouname();
#     pp=Person("dss")
#     pp.sayYouname()
#
#
# if __name__== '__main__':
#     selfAndInitDemo()


# class C(object):
#     def __init__(self):
#         self._x=None;
#     def getx(self):
#         return self._x
#     def setx(self,value):
#         self._x=value
#     def delx(self):
#         del self._x
#     x=property(getx,setx,delx,"I am the 'x'")
# a=C()
# print C.x.__doc__
# print a.x
# a.x=100
# print a.x
# try:
#     del a.x
#     print 1111
#     print a.x
#     print 2222
# except Exception,e:
#     print 3333
#     print e



# class Parrot(object):
#     def __init__(self):
#         self.voltage1= 100000
#
#     @property
#     def voltage(self):
#         return self.voltage1
# if __name__=="__main__":
#     a = Parrot()
#     print a.voltage1
#     try:
#         print a.voltage()
#     except Exception, e:
#         print e


# class Networkerror(RuntimeError):
#     def __init__(self,arg):
#         self.args=arg
# try:
#     raise Networkerror("Bad hostname")
# except Networkerror,e:
#     print e.args

import os
f = open('data.txt', 'w')
f.write('1 2 3 4\n')
f.write('2 3 4 6\n')
f.close()
f = open('data.txt','r')
data=[]
for line in f:
    data.append([int(x) for x in line.split()])
f.close()
print(data)
for row in data:
    print(row)

os.remove('data.txt')
print(os.getpid())
print(os.sep)