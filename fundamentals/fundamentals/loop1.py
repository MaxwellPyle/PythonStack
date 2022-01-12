#exercise 1
for x in range(0,151):
    print(x)
#exercise 2
for y in range(0,1001,5):
    print(y)
#exercise 3
for z in range(0,101):
    if z % 10 == 0:
        print("Coding Dojo")
        continue
    elif z % 5 == 0:
        print("Coding")
        continue
    print(z)
#exercise 4
sum = 0
for n in range(0,500000):
    if n % 2 != 0:
        sum = sum + n
print(sum)
#exercise 5
for m in range(2018,0,-4):
    print(m)
#exercise 6
lowNum = 1
highNum = 100
mult = 7
for t in range(lowNum,highNum):
    if t % mult == 0:
        print(t)