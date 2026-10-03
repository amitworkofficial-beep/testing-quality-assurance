from calculator_service import calculate_bill


def run_system_test():
    print("Starting System Test...")

    result = calculate_bill(100, 5, 5)

    assert result["total"] == 500
    assert result["average"] == 100

    print("Bill calculation test: PASSED")
    print("Total:", result["total"])
    print("Average:", result["average"])
    print("System Test: PASSED")


if __name__ == "__main__":
    run_system_test()