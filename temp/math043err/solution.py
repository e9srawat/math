def generate_permutations(digits, current='', combinations=None):
    if combinations is None:
        combinations = []

    if not digits:
        combinations.append(int(current))
        return combinations
    
    for i in range(len(digits)):
        remaining_digits = digits[:i] + digits[i+1:]
        combinations = generate_permutations(remaining_digits, current + digits[i], combinations)
    
    return combinations

def get_digit_combinations(number):
    digits_str = str(number)
    
    digit_permutations = generate_permutations(digits_str)
    
    return digit_permutations

number = 1234
result = get_digit_combinations(number)
print(result)
