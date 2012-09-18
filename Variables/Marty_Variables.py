class dotdict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

dd = dotdict()
var = []
string = raw_input(">>")
a = string[:string.index("=")]
dd.a = string[string.index("=")+1:len(string)]
var.append({a:dd.a})
print dd.a
print a
print var

b = raw_input()
for i in var:
	if b == i:
		print var.i