f = open ('2.dat')
lines = f.readlines()
f.close()

sum = 0
for i in lines:
	i = i.strip('\n')
	dimensions = i.split('x')
	print (dimensions)
	l = int(dimensions[0])
	w = int(dimensions[1])
	h = int(dimensions[2])
	wrappingPaper = 2*l*w + 2*w*h + 2*h*l
	if l < w and l < h:   #if length is least
	   if w < h:
	      slack = l*w
	      print ("l*w")
	   else:
	      slack = l*h
	      print ("l*h")
	elif w < l and w < h: #if width is least
	   if l < h:
	      slack = w*l
	      print ("w*l")
	   else:
	      slack = w*h
	      print ("w*h")
	else:                 #height is least
	   if l < w:
	      slack = h*l
	      print ("h*l")
	   else:
	      slack = h*w
	      print ("h*w")
	sum = sum + slack + wrappingPaper
	print(sum)
print (sum)
