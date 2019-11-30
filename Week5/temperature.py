ftoc=[]
ctof=[]
def tofarenheit(c):
	F=(9/5)*c+32
	ctof.append((c,F))
	return(F)
def tocelsius(f):
	
	C=(f-32)*(5/9)
	ftoc.append((f,C))
	return(C)
while(True):
	ch=int(input("1.Celsius to Farenheit\n2.Farenheit to Celsius \n3.Past conversions\n4.Exit\n"))
	if ch==1:
		c=float(input("Enter the temperature in celcius degree \n"))
		print("The temperature in Farenheit is: ",tofarenheit(c))
	elif ch==2:
		f=float(input("Enter the temperature in farenheit degree \n"))
		print("The temperature in Celsius is: ",tocelsius(f))
	elif ch ==3:	
		print("Farenheit to Celsius: ",ftoc," \nCelsius to Farenheit: ",ctof)
	elif ch==4:
		exit()
