def even_last(array):
    if len(array) == 0:
        return 0
        
    return sum([z for (i, z) in enumerate(array) if i % 2 == 0]) * array[-1]
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_last([6]) == 36, "(6)*6=36"
    assert even_last([]) == 0, "An empty array = 0"

    print("Use 'Check' to earn sweet rewards!")
