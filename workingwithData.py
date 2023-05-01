def demoNumpy():
    import numpy as np
    myarray = np.array([23, 34, 31, 12, 36])
    print(myarray)
    print(type(myarray))
    twoDarray = np.array([[1, 2, 3], [10, 20, 30], [22, 33, 44]])
    print(twoDarray)
    mystack = np.stack(["hello", "Fine", "Welcome"])
    print(mystack)
    threeDarray = np.array([[[10, 20, 30], [11, 12, 13]], [[21, 22, 23], [31, 34, 45]]])
    print(threeDarray)
    print("Dimension is", threeDarray.ndim)
    words=np.array(["Good","better", "best"])
    print(words)
    print(words.dtype)
# working with numpy
#demoNumpy()


def arrayShape():
    import numpy as np
    myarray = np.array([23, 34, 31, 12, 36])
    twoDarray = np.array([[1, 2, 3], [10, 20, 30], [22, 33, 44]])
    threeDarray = np.array([[[10, 20, 30], [11, 12, 13]], [[21, 22, 23],
                                                           [31, 34, 45]]])
    print(f'{myarray} , shape is {myarray.shape}')
    print(f'{twoDarray} , shape is {twoDarray.shape}')
    print(f'{threeDarray} , shape is {threeDarray.shape}')
    ar=np.array([11,12,13,14,15,34,53,24,56])
    rs=ar.reshape(3,3)
    print(ar)
    print(f'reshaped array\n{rs}')


arrayShape()