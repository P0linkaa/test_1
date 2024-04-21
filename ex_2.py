def is_prime(n):
    # Проверка на простое число
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(minimum, maximum):
    # Создаем пустой список для простых чисел
    primes = []
    
    # Проходим по каждому числу в заданном диапазоне
    for num in range(minimum, maximum):
        # Если число простое, добавляем его в список
        if is_prime(num):
            primes.append(num)
    
    return primes

print(prime_numbers_in_range(13, 333))
