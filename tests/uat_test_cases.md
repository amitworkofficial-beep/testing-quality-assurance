# User Acceptance Testing (UAT)

## UAT-01: Calculate Total Bill

**Scenario:** User enters product price and quantity.

**Input:**
- Price: 100
- Quantity: 5

**Expected Result:** Total should be 500.

**Actual Result:** Total was 500.

**Status:** PASS

---

## UAT-02: Calculate Average

**Scenario:** User wants to calculate the average value.

**Input:**
- Total: 500
- Count: 5

**Expected Result:** Average should be 100.

**Actual Result:** Average was 100.

**Status:** PASS

---

## UAT-03: Zero Division

**Scenario:** User attempts to divide a number by zero.

**Input:**
- Number: 10
- Divisor: 0

**Expected Result:** Application should show a controlled error instead of crashing unexpectedly.

**Actual Result:** ValueError was correctly raised.

**Status:** PASS

---

## UAT-04: Negative Numbers

**Scenario:** User enters negative numbers.

**Input:**
- -10 and -5

**Expected Result:** Application should correctly calculate the result.

**Actual Result:** Result was -15.

**Status:** PASS

---

## UAT-05: Zero Input

**Scenario:** User enters zero to check whether the application handles it correctly.

**Input:**
- Number: 0

**Expected Result:** Zero should be correctly identified as an even number.

**Actual Result:** Zero was correctly identified as even.

**Status:** PASS