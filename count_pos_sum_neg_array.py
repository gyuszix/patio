
def count_positives_sum_negatives(arr):
    answer = [0, 0]

    if len(arr) == 0:
        return []
    for value in arr:
        if value > 0:
            answer[0] += 1
        else:
            answer[1] += value
    return answer


print(count_positives_sum_negatives([1, 2, 0, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
