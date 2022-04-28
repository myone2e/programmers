a = [n for n in range(5)]
b = [5-n for n in range(5)]

for x in zip(a, b):
    print(x)
#(0, 5)
#(1, 4)
#(2, 3)
#(3, 2)
#(4, 1)