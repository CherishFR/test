"""求出1+3！+5！+7！+9！+50！的和"""
m = 0
for i in range(1,6):
    n = 1
    for j in range(1,2*i):
        n = n*j
    m += n
# 求50！
l = 1
for x in range(1,51):
    l = l*x
# 和
sum = m+l
print(sum)
