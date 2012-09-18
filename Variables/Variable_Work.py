# I (Marty), started working on variables using the following 
# dotdict() method...

class dotdict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

dd = dotdict()
a = raw_input()
dd.a = raw_input()
print dd.a

# Tommy had tried just adding the following elif to the code,
# but obviously it didn't work, because you cannot define a 
# string as a variable.

elif member ('=', string):
	string[:string.index('=')] = string[string.index('=') + 1:]
    print string[:string.index('=')] + 'Defined'