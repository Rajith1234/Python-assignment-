def fibonacci(n):
    # Create a list to store the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate Fibonacci numbers up to the nth number
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Example: Generate the first 10 Fibonacci numbers
n = 10
print(fibonacci(n))
