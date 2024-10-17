from knapsackSAT_MJ import kp_SAT

def validate_kp_SAT():
    # Test cases: (value, coins, expected_result)
    test_cases = [
        (11, [1, 2, 5], False),
        (3, [2, 3], True),
        (0, [1, 2, 3], True),
        (10, [5, 2, 3], True),
        (7, [5, 3, 2], True),
        (15, [2, 3, 7], False),
        (100, [99, 1], True),
        (8, [1, 4, 5], False),
        (6, [1, 3, 4], False),
        (12, [1, 2, 3, 4, 5], True)
    ]

    for i, (value, coins, expected) in enumerate(test_cases, 1):
        result = kp_SAT(value, coins)
        is_correct = (result is not None) == expected
        
        print(f"Test case {i}:")
        print(f"  Value: {value}")
        print(f"  Coins: {coins}")
        print(f"  Expected: {'Satisfiable' if expected else 'Unsatisfiable'}")
        print(f"  Result: {'Satisfiable' if result is not None else 'Unsatisfiable'}")
        print(f"  Correct: {'Yes' if is_correct else 'No'}")
        print()

    print("Validation complete.")

if __name__ == "__main__":
    validate_kp_SAT()