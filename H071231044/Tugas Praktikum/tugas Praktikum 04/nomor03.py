def maximum(*Tertinggi):
    max = Tertinggi[0]
    for num in Tertinggi:
        if num > max:
            max = num

    return max

print(maximum(1,2,4,6,9,3,11,9,10))