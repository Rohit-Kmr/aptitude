num=float(input("Enter a number :"))         # converted to float as it to check whether the user inputed integer or real number 
flag=0
if num<=1 or (not((num).is_integer())):
	flag=2
else:
	for i in range(2,int(num**0.5)+1):		# ** is power operator and here i will go from 2 to squareROOT(num)
		if num%i == 0:
			flag=1
			break
if flag==0:
	print("The number is Prime")
elif flag==1:
	print("The number is Not Prime")
elif flag==2 and num==1:
	print("The number is neither prime nor composite number")
else:
	print("The number is not Natural")
	
#this program is of complexity O(n^0.5) where n is the input number so it is a pesudo polynomial
