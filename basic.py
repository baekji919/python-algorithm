a = []
for n in range(1, 10+1):
    if n % 2 == 1:
        a.append(n * 2)
print(a)

multiline = "Hello World \nLife is beautiful"
print(multiline)

b = "Life is beautiful"
print(len(b))

c = "Hello World Life is beautiful"
print(len(c))
print(c[0])
print(c[4])
print(c[-1])

print(c[0:4])
print(c[-2:])

d = "There is %d apples" % 2
print(d)

d = "There is %s apples" % "two"
print(d)

number = 2
d = "There is %d apples" % number
print(d)

d = "There id %d apples and %s peaches" % (3, "five")
print(d)

number = 3
string = "five"
d = "There id %d apples and %s peaches" % (number, string)
print(d)