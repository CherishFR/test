def quick_sort(li,first,last):
    """快速排序"""
    if first >= last:
        return
    key = li[first]
    low = first
    high = last
    while low < high:
        while low < high and key <= li[high]:
            high -= 1
        li[low]=li[high]
        while low < high and key > li[low]:
            low  += 1
        li[high] = li[low]
    li[low] = key
    quick_sort(li, first, low-1)
    quick_sort(li, low+1, last)

if __name__ == '__main__':
    list = [1,7,2,5,7,6,3,9,4]
    quick_sort(list,0,len(list)-1)
    print(list)