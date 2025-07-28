def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW

# RECURSIVE VERSION OF ASSIGNMENT METHODS

def sum_of_digits(n: int) -> int:
    # If n is less than 10, it's a single digit, returns it
    if n < 10:
        result = n
    # If n has multiple digits...
    # Extracts last digit of n and gets added to total sum
    # Calls the same function recursively on remaining digits, excluding last digit (n // 10)
    else:
        result = (n % 10) + sum_of_digits(n // 10)
    return result

def count_occurences(data_list: list[int], target: int) -> int:
    # If no list is provided 0 is returned
    if not data_list:
        result = 0
    else:
        # Checks if first item matches the target
        # If it does it adds 1 to result, repeats on the rest of the list
        increment = 1 if data_list[0] == target else 0
        result = increment + count_occurences(data_list[1:], target)
    return result


def factorial_iterative(n: int) -> int: 
    result: int = 1
    i: int = 1
    # Uses while loop to multiply by every number from 1 to n
    while i <= n:
        result *= i
        # Increments i by 1 to move to the next number in the loop
        i += 1
    return result


def fibonacci_iterative(n: int) -> int:
    if n == 1:
        result = 1
    elif n == 2:
        result = 2
    # Runs if n is greater than 2
    else:
        # represents first Fibonacci number
        prev1: int = 1
        # represents second Fibonacci number
        prev2: int = 2
        # starts iteration from 3 since 1 and 2 are already known
        i: int = 3
        # stores computed Fibonacci value at each step
        fib: int = 0
        while i <= n:
            # computes the next Fibonacci number by adding two previous ones
            fib = prev1 + prev2
            # updates prev1 to what prev2 was
            prev1 = prev2
            # updates prev2 to hold new fib value
            prev2 = fib
            # Moves to the next
            i += 1
        result = fib
    return result


# TESTING 
print("\n\nTest of sum_of_digits:")
print("---------------------\n")
print(sum_of_digits(1234))
print(sum_of_digits(1234))
print("\n\nTest of count_occurerences:")
print("--------------------------\n")
print(count_occurences([4, 5, 6, 7, 7, 6, 8, 1], 7))
print(count_occurences([4, 5, 6, 7, 4, 6, 4, 1], 4))
print("\n\nTest of factorial_iterative:")
print("---------------------------\n")
print(factorial_iterative(4))
print(factorial_iterative(5))
print("\n\nTest of fibonacci_iterative:")
print("---------------------------\n")
print(fibonacci_iterative(2))
print(fibonacci_iterative(6))
print(fibonacci_iterative(9))