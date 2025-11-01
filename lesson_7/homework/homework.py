# Example 1: Using map() with lambda
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Map example (squares):", squared)

# Example 2: Using filter() with lambda
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter example (even numbers):", filtered)


# 1. is_prime(n) funksiyasi

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 2. digit_sum(k) funksiyasi

def digit_sum(k):
    return sum(map(int, str(k)))


# 3. Ikki sonning darajalari

def powers_of_two(n):
    result = []
    power = 1
    while True:
        power *= 2
        if power > n:
            break
        result.append(power)
    return result


# Test calls
if __name__ == "__main__":
    print("\n1. is_prime examples:")
    print(is_prime(4))
    print(is_prime(7))

    print("\n2. digit_sum examples:")
    print(digit_sum(24))
    print(digit_sum(502))

    print("\n3. powers_of_two example:")
    print(powers_of_two(10))
