f = open ('2.dat')
lines = f.readlines()
f.close()

sum = 0
for i in lines:
	i = i.strip('\n')
	dimensions = i.split('x')
	l = int(dimensions[0])
	w = int(dimensions[1])
	h = int(dimensions[2])
	
	d1 = l*w
	d2 = w*h
	d3 = h*l
	wrappingPaper = (2*d1) + (2*d2) + (2*d3)
	slack = 0

	if d1 <= d2 and d1 <= d3:
	   slack = d1
	elif d2 <= d1 and d2 <= d3:
	   slack = d2
	else:
	   slack = d3

	sum = sum + slack + wrappingPaper
print (sum)
