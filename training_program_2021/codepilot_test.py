#check a binary search

def check_binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



# define a function to compare merge 2 cvs file

def compare_csv(file1, file2):
    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            for line1, line2 in zip(f1, f2):
                if line1 != line2:
                    print(line1, line2)
                    return False
    return True