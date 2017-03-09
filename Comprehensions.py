#Comprehensions

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)

squares1 = [i**2 for i in range(10)]

print(squares1)


squares2 = [i**2 for i in range(10) if i%3 == 0]

print(squares2)

squares_dict = {i: i**2 for i in range (10) if i%3 == 0}

print(squares_dict)

print(sum([i**2 for i in range(10)]))

isd_codes = {'India': 91, 'US': 1, 'UK' : 44, 'UAE' : 971 }

isd_codes_1 = {isd_codes[key]:key for key in isd_codes}

print(isd_codes_1)
