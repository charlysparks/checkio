def flat_list(array):
    r = []
    while len(array) > 0:
        l = array.pop()
        if hasattr(l, "__iter__"):
            array.extend(l)
        else:
            r.append(l)

    return r[::-1]
 

if __name__ == "__main__":
    assert flat_list([1, 2, 3]) == [1, 2, 3], "Flat"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "One"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Nested"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "In In"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
