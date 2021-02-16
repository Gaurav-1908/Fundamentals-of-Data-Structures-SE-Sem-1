def binary_search(arr, key):
    arr.sort()
    l, h = 0, len(arr) - 1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            l = mid + 1
        else:
            h = mid - 1
    return -1


def fibonacci_search(arr, key):
    arr.sort()
    f1 = 0
    f2 = 1
    f = f1 + f2
    while (f < len(arr)):
        f1 = f2
        f2 = f
        f = f1 + f2
    offset = -1
    while (f > 1):
        i = min(offset+f1, len(arr)-1)
        if (arr[i] < key):
            f = f2
            f2 = f1
            f1 = f - f2
            offset = i
        elif (arr[i] > key):
            f = f1
            f2 = f2 - f1
            f1 = f - f2
        else:
            return i
    if(f2 and arr[offset+1] == key):
        return offset+1
    return -1


if __name__ == "__main__":
    arr = [int(x) for x in input(
        "Enter roll nos of students who attended training : ").split()]
    print(f"Student was {'not ' if binary_search(arr, int(input('Enter roll no. of student to be searched (binary) : '))) == -1 else ' '}present.")
    print(f"Student was {'not ' if fibonacci_search(arr, int(input('Enter roll no. of student to be searched (fibonacci) : '))) == -1 else ' '}present.")
