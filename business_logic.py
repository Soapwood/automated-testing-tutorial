# business_logic.py

def perform_calculation(a, b):
    # Business logic: perform a calculation
    return a + b

def calculate_discounted_price(price, discount_rate):
    # Business logic: calculate discounted price based on price and discount rate
    discount = price * (discount_rate / 100)
    discounted_price = price - discount
    return discounted_price

def is_prime_number(number):
    # Business logic: check if a number is prime
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_average(numbers):
    # Business logic: calculate the average of a list of numbers
    if not numbers:
        return None
    return sum(numbers) / len(numbers)