from random import randint

import operator

variable_list = {}
name_count = []

function_list = {}
func_names = []

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
    print "       Welcome to Soup v18.1!"
    print "  Use Soup to do simple commands,"
    print "    type 'cmd' to see them all."
    print "  Enter 'exit' at any time to quit."

def program():
    mastHead()
    error = 'Operator Error'
    i = 0
    while i == 0:
        try:
            string = raw_input('>> ').lower()
            if string.strip() == 'exit':
                i = 1
            elif member('get', string):
                 #if member(string[string.index('get') + 4:],name_count):
                     #print variable_list[string[string.index('get') + 4:]]
                 #    print variable_list
                 #else:
                 #   print 'Undefined'
                 #above does not work
                for item in variable_list:
                    print item, '=', variable_list[item]
                 
            elif member('=', string):
                #variable_list[string[:string.index('=') - 1]] = string[string.index('=') + 2:]
                #print string[:string.index('=') - 1].capitalize() + ' defined'
                #name_count.append(string[:string.index('=') - 1])
                
                #above does not work
                var = string.split('=')
                key = var[0]
                value = var[1]
                variable_list[key] = value
                print key + ' defined'
                                
            elif member('def',string):
                function_list[string[string.index('def') + 4: string.index('[')]] = string[string.index('[') + 1: string.index(']')]
                print string[string.index('def') + 4: string.index('[')].capitalize() + 'defined'
                func_names.append(string[string.index('def') + 4: string.index('[')])
            elif member('run',string):
                if member(string[string.index('run') + 4:],func_names):
                     string = function_list(string[string.index('run') + 4:])
                     func_program(string)
                else:
                    print 'Undefined'
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
            elif string.strip() == 'cmd': #commands
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
                    print "[var] = [var]"
                    print "get [var]"
                    print "help"
                    print "cmd"
                    print "author"
                    print "exit"
            else:    
                print operator_list[memberNew(string)](int(string.split(memberNew(string))[0]), int(string.split(memberNew(string))[1]))
        except:
            print "Error: " + error
program()