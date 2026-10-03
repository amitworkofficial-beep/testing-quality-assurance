# Testing and Quality Assurance

## Project Overview

This project demonstrates practical Testing and Quality Assurance techniques using a simple Python calculation application. The project focuses on verifying software correctness, reliability, error handling, maintainability, and performance.

The project includes multiple levels of testing, including unit testing, integration testing, system testing, user acceptance testing (UAT), edge-case testing, error handling, and performance testing.

## Objectives

* Test individual functions using unit testing.
* Verify communication between application modules.
* Perform system-level testing.
* Test edge cases and invalid inputs.
* Handle errors safely.
* Document UAT scenarios and results.
* Evaluate basic code quality and maintainability.
* Measure application performance.
* Document testing results and known issues.

## Technologies Used

* Python 3
* Python `unittest`
* Python standard library
* VS Code
* GitHub

## Project Structure

```text
testing-quality-assurance/
│
├── calculator.py
├── calculator_service.py
├── system_test.py
├── performance_test.py
├── TEST_RESULTS.md
├── CODE_REVIEW.md
├── README.md
│
└── tests/
    ├── test_calculator.py
    ├── test_integration.py
    ├── test_edge_cases.py
    └── uat_test_cases.md
```

## Testing Performed

### Unit Testing

Individual calculator functions were tested independently.

**Result:** 7/7 tests passed.

### Integration Testing

Multiple functions and modules were tested together to verify correct data flow.

**Result:** 3/3 tests passed.

### System Testing

The complete bill calculation workflow was tested from input through final output.

**Result:** PASS

### User Acceptance Testing

Five UAT scenarios were documented covering normal calculations, zero division, negative numbers, and zero input.

**Result:** 5/5 scenarios passed.

### Edge Case Testing

The application was tested with negative numbers, zero values, and division by zero.

**Result:** 5/5 automated edge-case tests passed.

### Performance Testing

The application performed 100,000 bill calculation operations.

**Execution Time:** 0.041920 seconds

**Result:** PASS

## Final Test Results

| Testing Area        | Result     |
| ------------------- | ---------- |
| Unit Testing        | 7/7 Passed |
| Integration Testing | 3/3 Passed |
| System Testing      | PASS       |
| Edge-Case Testing   | 5/5 Passed |
| UAT                 | 5/5 Passed |
| Performance Testing | PASS       |

### Automated Test Summary

* **Total Automated Tests:** 15
* **Passed:** 15
* **Failed:** 0
* **Overall Status:** PASS

## Error Handling

Division by zero is handled using `ValueError`, preventing invalid division operations from being processed silently.

## Code Quality

The project separates application logic from testing code. Functions have clear names, modules have specific responsibilities, and testing documentation is maintained separately.

## Debugging

During development, a module import issue occurred because `calculator_service.py` was placed in the wrong directory. The issue was identified using PowerShell file-location checks and corrected by moving the file to the project root.

After correction, all integration tests passed successfully.

## How to Run Tests

Run the complete automated test suite using:

```bash
python -m unittest discover -s tests -v
```

Run the system test:

```bash
python system_test.py
```

Run the performance test:

```bash
python performance_test.py
```

## Conclusion

This project demonstrates a structured approach to software testing and quality assurance. The application was tested at multiple levels and successfully passed all defined automated tests. Test results, UAT scenarios, performance results, code quality observations, and debugging information are documented for maintainability and future reference.
