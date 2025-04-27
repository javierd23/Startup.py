largest = None
smallest = None

while True:
    num = input('enter a number: ')
    if num == 'done':
        break
    try:
        nums = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = nums
    elif nums > largest:
        largest = nums

    if smallest is None:
        smallest = nums
    elif nums < smallest:
        smallest = nums





print('Maximun is', largest)
print('Minimum is', smallest)














