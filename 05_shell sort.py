def shell_sort(li):
    n = len(li)
    gap = n//2
    while gap >= 1:
        for i in range(gap,len(li)):
            tmp = li[i]
            j = i-gap
            while j>=0 and tmp < li[j]:
                li[j+gap] = li[j]
                j = j-gap
            li[j+gap] = tmp
        gap = gap//2

if __name__ == '__main__':
    list = [1,7,2,5,7,6,3,9,4]
    shell_sort(list)
    print(list)
