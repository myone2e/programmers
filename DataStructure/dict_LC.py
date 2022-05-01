lst = [6,7,8,9,10]

hi = {k : v for v, k in enumerate(lst)}

print(hi)


hi2 = {k:0 for k in lst}

for i in [6,7]:
    hi2[i] += 1

print(hi2)

