string=input("Enter elements:")
a=string.split()
print("The List is :",a)
a[0]=1
print(a)
a.append(7)
print(a)
a.extend([5,6,7])
print(a)
del a[5]
print(a)

output:
  Enter elements:1 2 3 4 5
The List is : ['1', '2', '3', '4', '5']
[1, '2', '3', '4', '5']
[1, '2', '3', '4', '5', 7]
[1, '2', '3', '4', '5', 7, 5, 6, 7]
[1, '2', '3', '4', '5', 5, 6, 7]
