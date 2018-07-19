def insert_sort(li):
    """插入排序"""
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j >= 0 and tmp < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp

if __name__ == '__main__':
    list = [1,7,2,5,7,6,3,9,4]
    insert_sort(list)
    print(list)
