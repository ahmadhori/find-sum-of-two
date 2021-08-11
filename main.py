def find_sum_of_two(A, val):
    s = set(A)
    for x in A:
        if (val - x) in (s - {x}):
            return True
    return False;


find_sum_of_two([5, 7, 1, 2, 8, 4, 3],2)