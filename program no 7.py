string=input("Enter elements:")
a=string.split()
print("The List is :",a)
string=input("Enter elements:")
b=string.split()
print("The List is :",b)
print("operations")
c=list(set(a)|set(b))
print("union operation  ",c)
d=list(set(a)&set(b))
print("intersection operation  ",d)
e=list(set(a)-set(b))
print("difference operation  ",e)
f=list(set(a)^set(b))
print("symmetric operation  ",f)

output:
  Enter elements:1 2 3 4 5 6
The List is : ['1', '2', '3', '4', '5', '6']
Enter elements: 4 5 6 7 8 
The List is : ['4', '5', '6', '7', '8']
operations
union operation   ['8', '2', '1', '5', '4', '3', '7', '6']
intersection operation   ['4', '6', '5']
difference operation   ['1', '2', '3']
symmetric operation   ['8', '7', '2', '3', '1']
