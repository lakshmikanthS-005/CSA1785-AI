#matrix Addition
r = int(input("Enter the rows: "))
c = int(input("Enter the columns: "))
print("Enter Matrix 1:")
m1 = [[int(input()) for i in range(c)] for i in range(r)]
print("Matrix 1 is: ")
for n in m1:
   print(n)
print("Enter Matrix 2:")
m2 = [[int(input()) for i in range(c)] for i in range(r)]
for n in m2:
   print(n)
r = [[0 for i in range(c)] for i in range(r)]
for i in range(len(r)):
   for j in range(c):
      r[i][j] = [m1[i][j] + m2[i][j]]
print("Add Matrix:")
for i in r:
   print(i)
   
   
   output:
   Enter the rows: 2
Enter the columns: 2
Enter Matrix 1:
5
8
7
4
Matrix 1 is: 
[5, 8]
[7, 4]
Enter Matrix 2:
5
5
7
1
[5, 5]
[7, 1]
Add Matrix:
[[10], [13]]
[[14], [5]]
   
