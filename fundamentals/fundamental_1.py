#multiples of three

for i in range(-300, -6):
    if i % 3 == 0:
        print(i)

#print integers with WHILE
i = 2000
while i <= 5281:
    i = i+1
    print(i)

#Counting, the Dojo Way
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")

#flexible countdowm

low_num = 2
high_num = 9
mult = 3

for count in reversed(range(low_num, high_num + 1)):
    if count % mult == 0:
        print(count)