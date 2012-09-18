var = {}
string = raw_input(">>")
a = string.split("=")[0]
b = string.split("=")[1]
var[a] = b
print a + " = " + b

c = raw_input(">>>")
for i in var:
	if c == i:
		print var[i]