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

error = ''

def member (item, plist):
    return (item) in plist

def memberNew (plist):
    for x in operator_list:
        if x in plist:
            return x

    return False

def program():
    print "       Welcome to Soup v12!"
    print "  Use Soup to do simple commands,"
    print "      such as 5+5, or 123^3."
    print "   You need to have a semicolon"
    print "  after print/return statements."
    print "  Enter 'exit' at any time to quit."
    error = 'Unknown Error'
    i = 0
    while i == 0:
        try:
            string = raw_input('>> ').lower()
            if member('exit', string):
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
            else:    
                print operator_list[memberNew(string)](int(string.split(memberNew(string))[0]), int(string.split(memberNew(string))[1]))
        except:
            print "Error: " + error
            error = ''

program()