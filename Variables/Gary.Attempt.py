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
    print "       Welcome to Soup v13.2!"
    print "  Use Soup to do simple commands,"
    print "    type 'cmd' to see them all."
    print "  Enter 'exit' at any time to quit."

def variables():
    j = 0
    memory = {}
    while j ==0:
        varString = raw_input('>>##').lower()
        if varString.strip() == 'exit':
            j = 1
        #need to get variable and its value
        elif member ('=', varString):
            #we have variable=number
            values = varString.split('=')
            key = values[0]
            value = values[1]
            memory[key] = value
        #    print memory

        elif member ('print', varString):
            if member(';', varString):
                #print string[string.index('print') + 5: string.index(';')] 
                for item in memory:
                    print item, '=', memory[item]
            else:
                print 'Error: You need to have a semicolon after print statements'
        else:
                operator = memberNew(varString)
                string = varString.split(operator)
                operator_func = operator_list[operator]
                print operator_func(int(memory[string[0]]), int(memory[string[1]]))
            

def program():
    mastHead()
    error = 'Operator Error'
    i = 0
    while i == 0:
        try:
            string = raw_input('>> ').lower()
            if string.strip() == 'exit':
                i = 1
            
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
            elif string.strip() == 'var':
                    variables()        
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
                    print "help"
                    print "cmd"
                    print "author"
                    print "exit"
            else: 
                #modified to reduce calls to membersNew
                #operatorFunc = memberNew(string)
                #print operator_list[memberNew(string)](int(string.split(memberNew(string))[0]), int(string.split(memberNew(string))[1]))
                operator = memberNew(string)
                string = string.split(operator)
                operator_func = operator_list[operator]
                print operator_func(int(string[0]), int(string[1]))
        except:
            print "Error: " + error
program()