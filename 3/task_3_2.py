import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
    if min > max:
        return []
    if max > 1000:
        return []
    if min < 1:
        return []
    if (max - min + 1) < quantity:
        return []
    while len(numbers) < quantity:
        num = random.randint(min, max)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

if __name__ == '__main__':
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
