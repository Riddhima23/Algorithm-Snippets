rows = int(input("Please Enter the total Number of Rows  : "))
number = 1

print("Floyd's Triangle:")
i = 1
while(i <= rows):
    j = 1
    while(j <= i):        
        print(number, end = '  ')
        number = number + 1
        j = j + 1
    i = i + 1
    print()
