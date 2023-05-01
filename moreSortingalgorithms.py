class selectionSortAlgorithm:
    def selection_sort(self,alist):
        for i in range(0, len(alist) - 1):
            smallest = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[smallest]:
                    smallest = j
            alist[i], alist[smallest] = alist[smallest], alist[i]
            print(alist)

def selectionsortimplement():
    alist = input('Enter the list of numbers: ').split()
    alist = [int(x) for x in alist]
    selection = selectionSortAlgorithm()
    selection.selection_sort(alist)
    print('Sorted list: ', end='')
    print(alist)

#selectionsortimplement()

class insertionSortalgorithm:
    def insertion_sort(self,arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print(arr)
        return arr

def insertionSortImplement():
    insertion= insertionSortalgorithm()
    alist = input('Enter the list of numbers: ').split()
    alist = [int(x) for x in alist]
    alist=insertion.insertion_sort(alist)
    print(alist)

#insertionSortImplement()

class quicksortAlgorithm:
    def quick_sort(self,arr):
        stack = [(0, len(arr) - 1)]
        while stack:
            low, high = stack.pop()
            if high - low > 0:
                pivot = arr[high]
                i = low - 1
                for j in range(low, high):
                    if arr[j] <= pivot:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                stack.append((low, i))
                stack.append((i + 2, high))
                #print(stack)
                print(arr)
        return arr

def quicksortImplement():
    print("Quick sorting" )
    quicksort=quicksortAlgorithm()
    alist = input('Enter the list of numbers: ').split()
    alist = [int(x) for x in alist]
    quick= quicksort.quick_sort(alist)
    print(quick)

quicksortImplement()