def solution(a_list):
    a1, a2 = float('inf'), float('inf')
    for x in a_list:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2
solution([1, 2, -8, -2, 0])
