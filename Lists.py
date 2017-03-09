fruits = ["Apple", "Banana", "Orange"]
print("fruits[0]: " , fruits[0])
print("fruits[1]: " , fruits[1])
print("fruits[2]: " , fruits[2])
print("Length of the list: " , len(fruits))
for i in range(len(fruits)):
    pos = i + 1
    pos = str(pos)
    fruits[i] = pos + "." + " " + fruits[i] + "**"
print(fruits)

fruits.append("r74385742")
print(fruits)

fruits.insert(2, "Strawberry")
print(fruits)

fruits.extend(["4t2u9tghwign", "nruwg59tu", (4,5,7), "nruwg59tu"])
print(fruits)

del fruits[5]
print(fruits)

fruits.remove("nruwg59tu")
print(fruits)

del fruits[5]
print(fruits)

fruits.sort()
print("sorted list: " , fruits)
#note: if the list contains a tuple then we cannot use the sort command

squares = [0,1,4,9,16,25,36,49,64,81,100]
print(squares)

print("squares(0:3) - " , squares[0:3])
print("squares(:5) - " , squares[:5])
print("squares(:) - " , squares[:])
print("squares(-1) - " , squares[-1])
print("squares(2:7) - " , squares[2:7])

#below command will delete 2 elements from the end
del squares[-2:]
print(squares)

for i in range(len(squares)):
    print("Element : " , squares[i])


for i,j in enumerate(squares):
    print("Element", i, " --> ", j)
    

