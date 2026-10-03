import time
from calculator_service import calculate_bill


def run_performance_test():
    start_time = time.perf_counter()

    for _ in range(100000):
        calculate_bill(100, 5, 5)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print("Performance Test")
    print("----------------")
    print("Operations: 100000")
    print(f"Execution Time: {execution_time:.6f} seconds")

    if execution_time < 2:
        print("Performance Test: PASSED")
    else:
        print("Performance Test: REVIEW REQUIRED")


if __name__ == "__main__":
    run_performance_test()