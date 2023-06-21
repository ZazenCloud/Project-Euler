def number_to_words(n):
    if n == 1000:
        return "one thousand"
    elif n >= 100:
        hundreds = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return hundreds[n // 100 - 1] + " hundred" + (" and " + number_to_words(n % 100) if n % 100 > 0 else "")
    elif n >= 20:
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return tens[n // 10 - 2] + ("-" + number_to_words(n % 10) if n % 10 > 0 else "")
    elif n >= 10:
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return teens[n - 10]
    else:
        units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return units[n - 1]


def count_letters(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        word = number_to_words(i)
        word = word.replace(" ", "").replace("-", "")
        total_letters += len(word)
    return total_letters


limit = 1000
result = count_letters(limit)
print(result)