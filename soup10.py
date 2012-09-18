def member (item, list):
    return (item) in list

def program():
    print "       Welcome to Soup v10!"
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
            elif member ('*', string):
                print(int(string.split("*")[0])*int(string.split("*")[1]))
            elif member ('+', string):
                print(int(string.split("+")[0])+int(string.split("+")[1]))

            elif member ('-', string):
                print(int(string.split("-")[0])-int(string.split("-")[1]))

            elif member ('/', string):
                print(int(string.split("/")[0])/int(string.split("/")[1]))

            elif member ('^', string):
                print(int(string.split("^")[0])**int(string.split("^")[1]))

            elif member ('==', string):
                string = string.split("==")
                if int(string[0]) == int(string[1]):
                    print "true"
                else:
                    print "false"
            elif member ('>=', string):
                string = string.split(">=")
                if int(string[0]) >= int(string[1]):
                    print "true"
                else:
                    print "false"
            elif member ('<=', string):
                string = string.split("<=")
                if int(string[0]) <= int(string[1]):
                    print "true"
                else:
                    print "false"
            elif member ('>', string):
                string = string.split(">")
                if int(string[0]) > int(string[1]):
                    print "true"
                else:
                    print "false"
            elif member ('<', string):
                string = string.split("<")
                if int(string[0]) < int(string[1]):
                    print "true"
                else:
                    print "false"
            elif string != "":
                print "==> " + string
        except:
            print "Error"

program()