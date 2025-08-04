import random

def k_statistic(seq, k):

    if not seq or k < 0 or k >= len(seq):
        return None

    pivot = random.choice(seq)
    left = [x for x in seq if x < pivot]
    equal = [x for x in seq if x == pivot]
    right = [x for x in seq if x > pivot]


    if k < len(left):
        return k_statistic(left, k)
    elif k < len(left) + len(equal):
        return pivot
    else:
        return k_statistic(right, k - len(left) - len(equal))
