def sum_array(arr):
    #your code here
    if not arr or len(arr) <= 2:
        return 0
    sorted0= sorted(arr)
    return sum(sorted0[1:-1])