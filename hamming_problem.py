def compute_hamming_distance(a1, a2):
    # Calculate Hamming distance between two strings
    return sum(b1 != b2 for b1, b2 in zip(a1, a2))

def reorganize_str_cost(str, X, Y):
    count_01 = str.count("01")
    count_10 = str.count("10")
    
    cost_01 = count_01 * X
    cost_10 = count_10 * Y
    
    total_cost = cost_01 + cost_10
    
    # Reorganize the string by minimizing cost
    if cost_01 <= cost_10:
        reorganized_str = "01" * count_01 + "10" * count_10
    else:
        reorganized_str = "10" * count_10 + "01" * count_01
    
    hamming_dist = compute_hamming_distance(str, reorganized_str)
    
    print(hamming_dist)

# Input processing
T = int(input("Enter the number of test cases: "))

for _ in range(T):
    binary_str = input("Enter the binary string: ")
    X, Y = map(int, input("Enter X and Y separated by space: ").split())
    
    # Validate constraints
    if len(binary_str) < 1 or len(binary_str) > 10**5 or X < 0 or Y < 0:
        print("INVALID")
    else:
        reorganize_str_cost(binary_str, X, Y)
