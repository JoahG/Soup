import operator

operatord_list = {"==": operator.eq,
                 "*": operator.mul,
                 "/d": operator.div,
                 "+": operator.add,
                 "-": operator.sub,
                 "^": operator.pow,
                 ">d": operator.gt,
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

def program():
    print "       Welcome to Soup v11!"
    print "  Use Soup to do simple commands,"
    print "      such as 5+5, or 123^3."
    print " You can also use 'print' and 'return,'"
    print "  but remember to end those commands"
    print "      with a semicolon (;)!"
    print "  Enter 'exit' at any time to quit."
    i = 0
    while i == 0:
        try:
            string = raw_input('>> ').lower()
            if member ('exit', string):
                i = 1
            elif member ('return', string):
                print '==>' + string[string.index('return') + 6: string.index(';')]
            elif member ('print', string):
                print string[string.index('print') + 5: string.index(';')] 
#            elif string != "":
#                print "==> " + string
            else:    
                print operator_list[memberNew(string)](int(string.split(memberNew(string))[0]), int(string.split(memberNew(string))[1]))

        except:
            print "Error with calculation, check operator used!"

program()