from calculator import add, multiply, divide


def calculate_total(price, quantity):
    return multiply(price, quantity)


def calculate_average(total, count):
    return divide(total, count)


def calculate_bill(price, quantity, count):
    total = calculate_total(price, quantity)
    average = calculate_average(total, count)

    return {
        "total": total,
        "average": average
    }