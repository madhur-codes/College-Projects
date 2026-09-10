# python code to print following pattern    


# A

#  *
#  * *
#  * * *
#  * * * *       

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()


# B

# 1
# 1 2   
# 1 2 3
# 1 2 3 4       

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()



# C

# 1
# 2 2
# 3 3 3 
# 4 4 4 4

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print()


# D

# 1
# 2 3
# 4 5 6
# 7 8 9 10

k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k += 1
    print()
print()