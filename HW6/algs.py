def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def sort3(l):
    """
    Oblivious sorting algorithm for a list of exactly 3 elements.
    Uses only conditionals and swaps, no loops or new variables.
    """
    assert len(l) == 3
    
    if l[0] > l[1]: swap(l, 0, 1)
    
    if l[1] > l[2]: swap(l, 1, 2)
    
    if l[0] > l[1]: swap(l, 0, 1)

def bubble_sort(l):
    """
    Implementation of bubble sort algorithm.
    Repeatedly steps through the list, compares adjacent elements, 
    and swaps them if they are in the wrong order.
    """
    n = len(l)
    
    # Traverse through all list elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                swap(l, j, j + 1)