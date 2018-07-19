def select_sort(li):
    """选择排序"""
    for i in range(len(li)-1):
        a = i
        for j in range(i,len(li)-1):
            if li[a] > li[j]:
                a = j
        li[i],li[a]=li[a],li[i]

if __name__ == '__main__':
    list = [1,7,2,5,7,6,3,9,4]
    select_sort(list)
    print(list)