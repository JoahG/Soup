from random import randint

import operator

operator_list = {"==": operator.eq,
                 "*": operator.mul,
                 "/": operator.div,
                 "+": operator.add,
                 "-": operator.sub,
                 "^": operator.pow,
                 ">": operator.gt,
                 "<": operator.lt,
                 ">=": operator.ge,
                 "<=": operator.le,
                 "%": operator.mod
                 }    
def member (item, plist):
    return (item) in plist

def memberNew (plist):
    for x in operator_list:
        if x in plist:
            return x
    
    return False
    
def mastHead():
    print "       Welcome to Soup v17!"
    print "  Use Soup to do simple commands,"
    print "    type 'cmd' to see them all."
    print "  Enter 'exit' at any time to quit."
    
def program():
    mastHead()
    error = 'Operator Error'
    i = 0
    var = {}
    while i == 0:
        try:
            string = raw_input('>> ').lower()
            if string.strip() == 'exit':
                i = 1
            elif member ('=', string) and (member('==',string)) == False:
                a = string.split("=")[0]
                b = string.split("=")[1]
                var[a] = b
                print a + " = " + b
            elif member ('var', string):
                string = string[string.index("var")+4:]
                defined = False
                for j in var:
                    if string == j:
                        print var[j]
                        defined = True
                if defined == False:
                    print "Undefined"
            elif member ('return', string):
                if member(';', string):
                    print '==>' + string[string.index('return') + 6: string.index(';')]
                else:
                    print 'Error: You need to have a semicolon after return statements'            
            elif member ('print', string):
                if member(';', string):
                    print string[string.index('print') + 5: string.index(';')] 
                else:
                    print 'Error: You need to have a semicolon after print statements'
            elif member ('rand', string):
                    a = int(string[(string.index("rand")+5):string.index(",")])
                    b = int(string[(string.index(",")+1):string.index(")")])
                    print randint(a,b)
            elif string.strip() == 'help':
                    mastHead()
            elif string.strip() == 'author':
                    print "      Soup Copyright (c) 2012"
                    print "        Codecademy Users:"
                    print "         @tommycopeland"
                    print "            @thebrit"
                    print "             @joahg"
            elif string.strip() == 'cmd':
                    print "return [string];"
                    print "print [string];"
                    print "[int] + [int]"
                    print "[int] - [int]"
                    print "[int] * [int]"
                    print "[int] / [int]"
                    print "[int] % [int]"
                    print "[int] == [int]"
                    print "[int] > [int]"
                    print "[int] >= [int]"
                    print "[int] < [int]"
                    print "[int] <= [int]"
                    print "[int] ^ [int]"
                    print "rand( s[int] , f[int] )"
                    print "[key]=[value]"
                    print "var [key]"
                    print "help"
                    print "cmd"
                    print "author"
                    print "exit"
            else:    
                print operator_list[memberNew(string)](int(string.split(memberNew(string))[0]), int(string.split(memberNew(string))[1]))
        except:
            print "Error: " + error
program()