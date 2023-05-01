
# creating a stack by using a list
def stackwithList():
    mystack = []
    mystack.append("Ameer")
    mystack.append("Raj")
    mystack.append("Vimala")
    mystack.append("Kalaam")
    print(mystack)
    mystack.pop()
    print(mystack)
    mystack.append("Hayer")
    print(mystack)

#stackwithList()

#creating a stack with collections.deque
def stackwithDeque():
    from collections import deque
    ourstack = deque()
    ourstack.append("Mamata")
    ourstack.append("kirti")
    ourstack.append("Munna")
    print(ourstack)
    ourstack.appendleft("Salman")
    print(ourstack)
    ourstack.pop()
    print(ourstack)
    ourstack.popleft()
    print(ourstack)

#stackwithDeque()
# creating stack with queue.LifoQueue
def stackwithLifoQueue():
    from queue import LifoQueue
    mstack = LifoQueue()
    mstack.put("hello!")
    mstack.put("How are you?")
    mstack.put("I'm Fine!")
    mstack.put("All is well")
    print(mstack)
    d = mstack.__dict__  # to dictionary
    print(d)
    mstack.get()
    print(d)
#stackwithLifoQueue()
def queuewithList():
    # Queue implementation with list
    queue_list = []
    queue_list.append("alamac")
    queue_list.append("Visuals")
    queue_list.append("rendering")
    print(queue_list)
    print(queue_list.pop(0))
    print(queue_list.pop(0))
    print(queue_list.pop(0))
    print(queue_list)

#queuewithList()
def queuewithDeque():
    # Queue with deque
    from collections import deque
    myque = deque()
    myque.append("Lion")
    myque.append("Tiger")
    myque.append("Wolf")
    print(myque)
   # print(myque.pop())
    print(myque.popleft())
    print(myque)

#queuewithDeque()
def queueWithQueue():
    # queue with Queue
    from queue import Queue
    qq = Queue()
    qq.put("Summit")
    qq.put("Renegade")
    qq.put("Wiscose")
    qq.put("Dezawoo")
    print(qq)
    print(qq.__dict__)
    print(qq.get())
    print(qq.get())
    print(qq.__dict__)
#queueWithQueue()

#lenior Search algorithm demo
def linear_search(alist, key):
    """Return index of key in alist.
     Return -1 if key not present."""
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1

def linearSearchImplement():
    global key, index
    alist = input('Enter the list of numbers: ')
    alist = alist.split()
    alist = [int(x) for x in alist]
    key = int(input('The number to search for: '))
    index = linear_search(alist, key)
    if index < 0:
        print('{} was not found.'.format(key))
    else:
        print('{} was found at index {}.'.format(key, index))


#linearSearchImplement()


# Binary search implementatioin
def binary_search(alist, start, end, key):
    """Search key in alist[start... end - 1]."""
    if not start < end:
        return -1
    mid = (start + end) // 2
    if alist[mid] < key:
        return binary_search(alist, mid + 1, end, key)
    elif alist[mid] > key:
        return binary_search(alist, start, mid, key)
    else:
        return mid


def binarySearchImplement():
    global key, index
    alist = input('Enter the sorted list of numbers: ')
    alist = alist.split()
    alist = [int(x) for x in alist]
    key = int(input('The number to search for: '))
    index = binary_search(alist, 0, len(alist), key)
    if index < 0:
        print('{} was not found.'.format(key))
    else:
        print('{} was found at index {}.'.format(key, index))

#binarySearchImplement()
# Python program to demonstrate working of HashTable

hashTable = [[],] * 12
def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(12)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0


def hashtableImplementation():
    print(hashTable)
    insertData(123, "apple")
    insertData(432, "mango")
    insertData(213, "banana")
    insertData(654, "guava")
    insertData(546,"Grapes")
    print(hashTable)
    removeData(123)
    print(hashTable)

#hashtableImplementation()

def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if alist[j + 1] < alist[j]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                no_swap = False
        if no_swap:
            return


def bubbleSortimplement():
    alist = input('Enter the list of numbers: ').split()
    alist = [int(x) for x in alist]
    bubble_sort(alist)
    print('Sorted list: ', end='')
    print(alist)

#bubbleSortimplement()

#merge sort algorithm
def merge_sort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)


def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1


def mergesortImplementation():
    alist = input('Enter the list of numbers: ').split()
    alist = [int(x) for x in alist]
    merge_sort(alist, 0, len(alist))
    print('Sorted list: ', end='')
    print(alist)

#mergesortImplementation()