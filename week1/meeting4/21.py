"""numbers=[]
for i in range(4):
    num=int(input('enter number'))
    numbers.append(num)
    largenum=num
numbers.sort()
print(numbers[2])"""
#####################
"""list_col=[]
even_num=[]
odd_num=[]
for num in range(10):
    num=int(input("enter number  "))
    list_col.append(num)
    
for i in list_col:
    if i%2==0:
        even_num.append(i)
        
    else:
        odd_num.append(i)

print(list_col)
print(even_num)
print(odd_num)"""
#####################
numbers = [2, 5, 3, 2, 8, 2, 5, 3, 2, 9]

max_count = 0
most_repeated = numbers[0]

for number in numbers:
    count = 0

    for x in numbers:
        if number == x:
            count += 1

    if count > max_count:
        max_count = count
        most_repeated = number

print(most_repeated)
        



