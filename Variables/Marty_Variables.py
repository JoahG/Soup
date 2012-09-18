class dotdict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

dd = dotdict()
var = array([])
a = raw_input()
var.append(a)
dd.a = raw_input()
print dd.a
print a

b = raw_input()
for i in var:
	if b == i:
		print dd.a