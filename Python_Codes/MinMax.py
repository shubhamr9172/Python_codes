class solution:
    numbers =[2,1,3,5,6]
    min = numbers[0]
    max = numbers[0]

    for i in numbers:
        if min>i:
            min=i
        if max<i:
            max = i

    print(min,max) 
