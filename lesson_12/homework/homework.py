import threading
from collections import Counter

# Exercise 1: Threaded Prime Number Checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    result = []
    step = (end - start) // num_threads
    for i in range(num_threads):
        s = start + i * step
        e = start + (i + 1) * step if i < num_threads - 1 else end
        t = threading.Thread(target=check_primes, args=(s, e, result))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    result.sort()
    return result


# Exercise 2: Threaded File Processing
def process_lines(lines, counter):
    words = []
    for line in lines:
        words.extend(line.strip().split())
    counter.update(words)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    length = len(lines)
    step = length // num_threads
    threads = []
    counters = [Counter() for _ in range(num_threads)]
    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else length
        t = threading.Thread(target=process_lines, args=(lines[start:end], counters[i]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    total_counter = Counter()
    for c in counters:
        total_counter.update(c)
    return total_counter


# Main execution
if __name__ == "__main__":
    print("=== Threaded Prime Number Checker ===")
    primes = threaded_prime_checker(1, 100)
    print("Primes from 1 to 100:", primes)

    print("\n=== Threaded File Processing ===")
    sample_file = "sample_text.txt"
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("hello world\nthis is a test\nhello again world\n")
    word_counts = threaded_word_count(sample_file)
    print("Word counts:", dict(word_counts))
