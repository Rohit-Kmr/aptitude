num=int(input("Enter a number :"))
flag=0
for i in range(2,int(num**0.5)+1):		# ** is power operator and here i will go from 2 to squareROOT(num)
	if num%i == 0:
		flag=1
		break
if flag==0:
	print("The number is Prime")
else:
	print("The number is Not Prime")