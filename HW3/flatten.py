def flatten(lst):
    # Base case: if input is not a list, wrap it in a list and return
    if not isinstance(lst, list):
        return [lst]
    
    # Recursive case:
    # 1. map applies flatten to each element in lst and sum combines all resulting lists, with its base addend being the empty list
    return sum(map(flatten, lst), [])