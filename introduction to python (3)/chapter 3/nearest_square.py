def nearest_square(limit):
    var = 1
    while (var**2) < limit:
        var= var + 1
    return (var-1)**2    # var - 1 becuase we have to find nearest complete square below input integer 


test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
    