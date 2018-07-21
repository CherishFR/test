def merge_sort(li):
    n = len(li)
    if n <= 1:
        return li
    mid = n // 2
    l_li = merge_sort(li[:mid])
    r_li = merge_sort(li[mid:])
    l_po = 0
    r_po = 0
    new_li = []
    while l_po < len(l_li) and r_po < len(r_li):
        if l_li[l_po] <= r_li[r_po]:
            new_li.append(l_li[l_po])
            l_po += 1
        else:
            new_li.append(r_li[r_po])
            r_po += 1
    new_li += l_li[l_po:]
    new_li += r_li[r_po:]
    return new_li

if __name__ == '__main__':
    list = [1,7,2,5,7,6,3,9,4]
    a=merge_sort(list)
    print(a)