SOME_CONSTANT = 5
SOME_DATA = "a"

def someFn():
    print("hello")

#this
for i in range(3):
    print(i)
#and this
for i in range(3):
    someFn()
#become this:
for i in range(3):
    print(i)
    someFn()


someArr = []
for i in range(SOME_CONSTANT):
    someArr.append(SOME_DATA)

for i in range(SOME_CONSTANT):
    print(someArr[i])

#become
for i in range(SOME_CONSTANT):
    someArr.append(SOME_DATA)
    print(someArr[i])




