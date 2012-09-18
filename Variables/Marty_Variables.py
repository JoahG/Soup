class dotdict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

dd = dotdict()
var = {}
string = raw_input(">>")
a = string.split("=")[0]
b = string.split("=")[1]
var[a] = b
print a + " = " + b
print var

c = raw_input(">>>")
for i in var:
	if c == i:
		print var[i]