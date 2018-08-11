def median(numbers):
    numbers.sort() 
    a = int(len(numbers))
    if a % 2 == 0:
        b = int(a/2)
        middle_index2 = (numbers [b] + numbers [b - 1]) / 2 
        return middle_index2

    elif a % 2 == 1:
        middle_index = int(a/2)
        return numbers[middle_index]

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

test_self_created = median([53, 12, 65, 7, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test_self_created))
