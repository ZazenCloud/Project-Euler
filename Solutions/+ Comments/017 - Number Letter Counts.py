def number_to_words(n):
    '''Converts a given number to its corresponding word representation.'''
    if n == 1000:
        return "one thousand"
    elif n >= 100:
        # Handle numbers from 100 to 999
        hundreds = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return hundreds[n // 100 - 1] + " hundred" + (" and " + number_to_words(n % 100) if n % 100 > 0 else "")
    elif n >= 20:
        # Handle numbers from 20 to 99
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return tens[n // 10 - 2] + ("-" + number_to_words(n % 10) if n % 10 > 0 else "")
    elif n >= 10:
        # Handle numbers from 10 to 19
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return teens[n - 10]
    else:
        # Handle single-digit numbers
        units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return units[n - 1]


def count_letters(limit):
    '''Counts the total number of letters used when converting numbers from 1 to a given limit.'''
    total_letters = 0
    for i in range(1, limit + 1):
        word = number_to_words(i)
        word = word.replace(" ", "").replace("-", "")  # Remove spaces and hyphens
        total_letters += len(word)
    return total_letters


limit = 1000
result = count_letters(limit)
print(result)
