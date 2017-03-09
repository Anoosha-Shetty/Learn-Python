isd_codes = {'India': 91, 'US': 1, 'UK' : 44, 'UAE' : 971 }
print(isd_codes)

print(isd_codes['UAE'])

isd_codes['Uruguay'] = 498
print(isd_codes)

print("France in ISD codes : " , 'France' in isd_codes)

print("India in ISD codes : " , 'India' in isd_codes)

isd_codes1 = {'Switzerland': 41, 'Sri Lanka': 94, 'Singapore': 65}

isd_codes.update(isd_codes1)
print(isd_codes)

del isd_codes['Sri Lanka']
print(isd_codes)

for key in isd_codes:
    print("key : " ,key , ", Value: " ,isd_codes[key])


for ky in isd_codes.keys():
    print("key : " ,ky)

for val in isd_codes.values():
    print("val : " ,val)


for ky, val in isd_codes.items():
    print(ky,val)
