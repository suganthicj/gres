    
x11=input()
for p in x11:
	if p.isdigit():
		flag=0
	else:
		flag=1
		break
if flag==0:
	print("yes")
else:
	print("no")
