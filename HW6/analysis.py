import random
import time
import copy
import sys

# Try to import matplotlib, but handle the case where it's not available
try:
    import matplotlib
    # Set a non-interactive backend that doesn't require a display
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False
    print("Note: Matplotlib or NumPy not available. Skipping plot generation.")


# Global counters for operations
comparisons = 0
swaps = 0

def reset_counters():
    """Reset the global counters for a new measurement."""
    global comparisons, swaps
    comparisons = 0
    swaps = 0

def compare(a, b):
    """Compare two elements and increment the comparison counter."""
    global comparisons
    comparisons += 1
    return a > b

def counted_swap(l, i, j):
    """Swap elements at indices i and j in list l and increment the swap counter."""
    global swaps
    swaps += 1
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

# Implementation of the required algorithms with instrumentation

def sort3_counted(l):
    assert len(l) == 3
    
    if compare(l[0], l[1]): counted_swap(l, 0, 1)
    if compare(l[1], l[2]): counted_swap(l, 1, 2)
    if compare(l[0], l[1]): counted_swap(l, 0, 1)

def bubble_sort_counted(l):
    n = len(l)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(l[j], l[j + 1]):
                counted_swap(l, j, j + 1)

def insertion_sort_counted(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        
        # Use compare to count comparisons
        while j >= 0 and compare(l[j], key):
            l[j + 1] = l[j]  # This is not exactly a swap, but we'll count it
            counted_swap(l, j, j + 1)  # Count the movement as a swap
            j -= 1
            
        l[j + 1] = key

def selection_sort_counted(l):
    n = len(l)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # Use compare to count comparisons (but reverse the comparison)
            if compare(l[min_idx], l[j]):
                min_idx = j
                
        # Swap the minimum element with the first element
        counted_swap(l, i, min_idx)

def partition_counted(l, low, high):
    pivot = l[high]
    i = low - 1
    
    for j in range(low, high):
        # Use compare to count comparisons (but reverse the comparison)
        if not compare(l[j], pivot):
            i += 1
            counted_swap(l, i, j)
            
    counted_swap(l, i + 1, high)
    return i + 1

def quicksort_helper(l, low, high):
    """Helper function for instrumented quicksort."""
    if low < high:
        pi = partition_counted(l, low, high)
        quicksort_helper(l, low, pi - 1)
        quicksort_helper(l, pi + 1, high)

def quicksort_counted(l):
    quicksort_helper(l, 0, len(l) - 1)

def merge_counted(l, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    # Create temp arrays
    L = [0] * n1
    R = [0] * n2
    
    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = l[left + i]
    
    for j in range(n2):
        R[j] = l[mid + 1 + j]
    
    # Merge the temp arrays back into l[left..right]
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if not compare(L[i], R[j]):
            l[k] = L[i]
            i += 1
        else:
            l[k] = R[j]
            j += 1
        k += 1
        global swaps
        swaps += 1  # Count each placement as a swap
    
    # Copy the remaining elements of L[], if any
    while i < n1:
        l[k] = L[i]
        i += 1
        k += 1
        swaps += 1  # Count each placement as a swap
    
    # Copy the remaining elements of R[], if any
    while j < n2:
        l[k] = R[j]
        j += 1
        k += 1
        swaps += 1  # Count each placement as a swap

def mergesort_helper(l, left, right):
    if left < right:
        mid = left + (right - left) // 2
        
        mergesort_helper(l, left, mid)
        mergesort_helper(l, mid + 1, right)
        merge_counted(l, left, mid, right)

def mergesort_counted(l):
    mergesort_helper(l, 0, len(l) - 1)

def counting_sort_counted(l):
    """counting sort (works for non-negative integers)."""
    # Find the maximum value in the list
    max_val = max(l) if l else 0
    
    # Create count array and initialize it with zeros
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element
    for i in range(len(l)):
        count[l[i]] += 1
        global comparisons
        comparisons += 1  # Count each access as a comparison
    
    # Update count array to store the position of each object
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Create an output array
    output = [0] * len(l)
    
    # Build the output array
    for i in range(len(l) - 1, -1, -1):
        output[count[l[i]] - 1] = l[i]
        count[l[i]] -= 1
        global swaps
        swaps += 1  # Count each placement as a swap
    
    # Copy the output array to the original list
    for i in range(len(l)):
        l[i] = output[i]
        swaps += 1  # Count each copy as a swap

# Functions to generate test data

def generate_random_list(size, max_val=1000):
    """Generate a list of random integers."""
    return [random.randint(0, max_val) for _ in range(size)]

def generate_nearly_sorted_list(size, swap_count):
    """Generate a nearly sorted list by starting with a sorted list and performing some swaps."""
    l = list(range(size))
    for _ in range(swap_count):
        i = random.randint(0, size - 1)
        j = random.randint(max(0, i - 10), min(size - 1, i + 10))  # Swap with a nearby element
        l[i], l[j] = l[j], l[i]
    return l

def generate_reversed_list(size):
    """Generate a list in reverse sorted order."""
    return list(range(size, 0, -1))

def generate_few_unique_list(size, unique_count=10):
    """Generate a list with few unique values."""
    unique_values = [random.randint(0, 1000) for _ in range(unique_count)]
    return [random.choice(unique_values) for _ in range(size)]

def generate_almost_sorted_with_outliers(size, outlier_count=5):
    """Generate a mostly sorted list with a few outliers at wrong positions."""
    l = list(range(size))
    # Move some large values to the beginning
    for i in range(outlier_count):
        if i < len(l) and size - i - 1 < len(l):
            l[i], l[size - i - 1] = l[size - i - 1], l[i]
    return l

# Function to test and measure sorting algorithms

def measure_sort_algorithm(sort_func, input_list, name=""):
    """
    Measure the performance of a sorting algorithm.
    Returns a dictionary with the number of comparisons, swaps, and execution time.
    """
    # Make a copy of the input list to avoid modifying the original
    test_list = copy.deepcopy(input_list)
    
    # Reset counters
    reset_counters()
    
    # Measure execution time
    start_time = time.time()
    sort_func(test_list)
    end_time = time.time()
    
    # Check if the list is actually sorted
    is_sorted = all(test_list[i] <= test_list[i + 1] for i in range(len(test_list) - 1))
    
    return {
        "name": name,
        "comparisons": comparisons,
        "swaps": swaps,
        "time": end_time - start_time,
        "sorted": is_sorted
    }

def run_all_sorts(input_list, list_name=""):
    """Run all sorting algorithms on the given input list and return their measurements."""
    results = []
    
    # Skip sort3 for lists with more than 3 elements
    if len(input_list) == 3:
        results.append(measure_sort_algorithm(sort3_counted, input_list, "Sort3"))
    
    results.append(measure_sort_algorithm(bubble_sort_counted, input_list, "Bubble Sort"))
    results.append(measure_sort_algorithm(insertion_sort_counted, input_list, "Insertion Sort"))
    results.append(measure_sort_algorithm(selection_sort_counted, input_list, "Selection Sort"))
    results.append(measure_sort_algorithm(quicksort_counted, input_list, "Quick Sort"))
    results.append(measure_sort_algorithm(mergesort_counted, input_list, "Merge Sort"))
    
    # Only run counting sort if the list contains only non-negative integers
    if all(isinstance(x, int) and x >= 0 for x in input_list):
        results.append(measure_sort_algorithm(counting_sort_counted, input_list, "Counting Sort"))
    
    # Add list name to results
    for result in results:
        result["list_name"] = list_name
    
    return results

def generate_all_test_data(size=1000):
    """Generate all test data cases."""
    test_data = [
        ("Random", generate_random_list(size)),
        ("Nearly Sorted", generate_nearly_sorted_list(size, size // 10)),
        ("Reversed", generate_reversed_list(size)),
        ("Few Unique", generate_few_unique_list(size)),
        ("Almost Sorted with Outliers", generate_almost_sorted_with_outliers(size))
    ]
    return test_data

def run_benchmarks(sizes=[100, 500, 1000, 5000, 10000]):
    """Run benchmarks for various list sizes and generate a table of results."""
    all_results = []
    
    for size in sizes:
        print(f"Running benchmarks for size {size}...")
        test_data = generate_all_test_data(size)
        
        for name, data in test_data:
            list_name = f"{name} (size {size})"
            results = run_all_sorts(data, list_name)
            all_results.extend(results)
    
    return all_results

def print_results_table(results):
    """Print the results in a formatted table."""
    # Group results by list name
    grouped_results = {}
    for result in results:
        list_name = result["list_name"]
        if list_name not in grouped_results:
            grouped_results[list_name] = []
        grouped_results[list_name].append(result)
    
    # Print the table
    print("=" * 100)
    print("{:<30} {:<15} {:<15} {:<15} {:<15}".format(
        "List Type", "Algorithm", "Comparisons", "Swaps", "Time (s)"
    ))
    print("=" * 100)
    
    for list_name, list_results in grouped_results.items():
        print("-" * 100)
        print(list_name)
        print("-" * 100)
        
        for result in list_results:
            print("{:<30} {:<15} {:<15} {:<15.6f}".format(
                "", result["name"], result["comparisons"], result["swaps"], result["time"]
            ))
    
    print("=" * 100)

def save_results_to_file(results, filename="summary.txt"):
    """Save the results to a file."""
    with open(filename, "w") as f:
        f.write("# Sorting Algorithm Benchmark Results\n\n")
        
        # Write description of the test data
        f.write("## Test Data Description\n\n")
        f.write("1. **Random**: Lists with randomly generated integers.\n")
        f.write("2. **Nearly Sorted**: Lists that are almost sorted with about 10% of elements out of place.\n")
        f.write("3. **Reversed**: Lists in reverse sorted order (worst case for most sorting algorithms).\n")
        f.write("4. **Few Unique**: Lists with many repeated values and only a few unique items.\n")
        f.write("5. **Almost Sorted with Outliers**: Mostly sorted lists with a few outliers at wrong positions.\n\n")
        
        # Write the table header
        f.write("## Benchmark Results\n\n")
        f.write("{:<30} {:<15} {:<15} {:<15} {:<15}\n".format(
            "List Type", "Algorithm", "Comparisons", "Swaps", "Time (s)"
        ))
        f.write("{:<30} {:<15} {:<15} {:<15} {:<15}\n".format(
            "-" * 30, "-" * 15, "-" * 15, "-" * 15, "-" * 15
        ))
        
        # Group results by list name
        grouped_results = {}
        for result in results:
            list_name = result["list_name"]
            if list_name not in grouped_results:
                grouped_results[list_name] = []
            grouped_results[list_name].append(result)
        
        # Write the table data
        for list_name, list_results in grouped_results.items():
            f.write("\n**{}**\n\n".format(list_name))
            
            for result in list_results:
                f.write("{:<30} {:<15} {:<15} {:<15} {:.6f}\n".format(
                    "", result["name"], result["comparisons"], result["swaps"], result["time"]
                ))

def plot_results(results, metric="time", save_file=None):
    """Plot the results for visual comparison."""
    if not PLOTTING_AVAILABLE:
        print(f"Skipping plot generation for {metric} (plotting libraries not available)")
        return
        
    # Get unique list names and algorithm names
    list_names = sorted(set(result["list_name"] for result in results))
    alg_names = sorted(set(result["name"] for result in results))
    
    # Prepare data for plotting
    data = {alg: [] for alg in alg_names}
    
    for list_name in list_names:
        list_results = [r for r in results if r["list_name"] == list_name]
        
        for alg in alg_names:
            alg_result = next((r for r in list_results if r["name"] == alg), None)
            if alg_result:
                data[alg].append(alg_result[metric])
            else:
                data[alg].append(0)
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Set the width of each bar and positions
    width = 0.8 / len(alg_names)
    x = np.arange(len(list_names))
    
    # Plot bars for each algorithm
    for i, alg in enumerate(alg_names):
        ax.bar(x + (i - len(alg_names)/2 + 0.5) * width, data[alg], width, label=alg)
    
    # Add labels and legend
    ax.set_xlabel('Input List Type')
    
    if metric == "time":
        ax.set_ylabel('Execution Time (seconds)')
        ax.set_title('Execution Time Comparison of Sorting Algorithms')
    elif metric == "comparisons":
        ax.set_ylabel('Number of Comparisons')
        ax.set_title('Comparison Count of Sorting Algorithms')
    elif metric == "swaps":
        ax.set_ylabel('Number of Swaps')
        ax.set_title('Swap Count of Sorting Algorithms')
    
    ax.set_xticks(x)
    ax.set_xticklabels([name.split(' (size')[0] for name in list_names], rotation=45, ha='right')
    ax.legend()
    
    plt.tight_layout()
    
    if save_file:
        plt.savefig(save_file)
    else:
        plt.show()

# Main function to run all the analysis
def main():
    try:
        # Set random seed for reproducibility
        random.seed(42)
        
        print("Running benchmarks (this may take a moment)...")
        results = run_benchmarks(sizes=[100, 500]) 
        
        # Print results table
        print_results_table(results)
        
        # Save results to file
        save_results_to_file(results)
        print("Results saved to summary.txt")
        
        # Generate plots if plotting is available
        if PLOTTING_AVAILABLE:
            try:
                plot_results(results, "time", "time_comparison.png")
                plot_results(results, "comparisons", "comparison_count.png")
                plot_results(results, "swaps", "swap_count.png")
                print("Plots generated and saved as PNG files.")
            except Exception as e:
                print(f"Warning: Failed to generate plots: {e}")
                print("Continuing without plots.")
        
        print("Analysis complete!")
        return 0
    except Exception as e:
        print(f"Error in analysis: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())