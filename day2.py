f = open ('2.dat')
lines = f.readlines()
f.close()

sum = 0
ribbonSum = 0
for i in lines:
	i = i.strip('\n')
	dimensions = i.split('x')
	l = int(dimensions[0])
	w = int(dimensions[1])
	h = int(dimensions[2])
	
	bow = l*w*h
	p1 = l+l+w+w
	p2 = l+l+h+h
	p3 = w+w+h+h
	
	d1 = l*w
	d2 = w*h
	d3 = h*l
	wrappingPaper = (2*d1) + (2*d2) + (2*d3)
	slack = 0
	ribbon = 0

	if p1 <= p2 and p1 <= p3:
	   ribbon = p1
	elif p2 <= p1 and p2 <= p3:
	   ribbon = p2
	else:
	   ribbon = p3

	if d1 <= d2 and d1 <= d3:
	   slack = d1
	elif d2 <= d1 and d2 <= d3:
	   slack = d2
	else:
	   slack = d3

	sum = sum + slack + wrappingPaper
	ribbonSum += ribbon + bow
print (sum)
print (ribbonSum)
