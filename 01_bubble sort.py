def bubble_sort(li):
    """冒泡排序"""
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

if __name__ == '__main__':
    list = [1,7,2,5,7,6,3,9,4]
    bubble_sort(list)
    print(list)