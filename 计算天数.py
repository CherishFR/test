def judge_dayth(y=None,m=None,d=None):
    # 判断是否是润年
    if y%4==0 and y%100!=0 or y%400==0:
        m_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        m_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 1:
        dayth = d
    else:
        m_days = 0
        for i in range(m-1):
            m_days += m_list[i]
        dayth = m_days + d
    print(dayth)