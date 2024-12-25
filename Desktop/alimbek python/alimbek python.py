number = int(input("Enter a number: "))
if number >= 7:
    print("Hello")

name = input("Enter a name: ")
if name == "John":
    print("Hello, John")
else:
    print("There is no such name")

array = list(map(int, input("Enter a numeric array separated by a space: ").split(' ')))
print("multiples of a 3:")
for i in array:
    if i % 3 == 0:
        print(i)