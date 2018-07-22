def func(li,num):
    for i in range(num):
        max = 0
        for j in li:
            if j > max:
                max = j
        if i != num -1:
            li.remove(max)
    return max

li = [1,22,33,4,3,1]
a = func(li,3)
print(a)