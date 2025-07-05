#12. WAP to print Armstrong number within a given range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
for num in range(start, end+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if sum == num:
        print(num)