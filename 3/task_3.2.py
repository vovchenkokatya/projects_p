import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
    while len(numbers) < quantity:
        num = random.randint(min, max)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

if __name__ == '__main__':
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
