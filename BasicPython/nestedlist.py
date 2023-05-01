def iteratordemo():
    global index, item
    names = ["Adam", ["Bob",
                      ["Chet", "Cat", ], "Barb", "Bert"], "Alex",
             ["Bea", "Bill"], "Ann"]
    for index, item in enumerate(names):
        print(index, item)


def comprehehsionDemo():
    oddnos = [no * 2 + 1 for no in range(1, 10)]
    print(oddnos)
    evenos = [no * 2 for no in range(1, 20)]
    print(evenos)
    squares = {n: n ** 2 for n in range(1, 12)}
    print(squares)
    cubes = {n: n ** 3 for n in range(1, 10)}
    print(cubes)
    nos = [cubes, squares]
    for n in nos:
        print(n)


def lambda_demos():
    s = lambda a, b: a + b
    print(s(100, 200))
    m = lambda x, y: x * y
    print(m(10, 20))
    print(m(12, 8))
    t = lambda x, y, z: (x + y) * z
    print(t(10, 20, 4))


#iteratordemo()
#comprehehsionDemo()
#lambda_demos()

