def sum_range(start, end):
    sum = 0
    if int(start) > int(end):
        end, start = int(start), int(end)
    for num in range(int(start), int(end) + 1):
            sum += num
    return sum
print(sum_range(1, 10))