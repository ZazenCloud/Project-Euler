alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total_score = 0

with open('./p022_names.txt', encoding="utf-8") as file:
    list_file = file.read()
    name_generator = (name.strip('"') for name in list_file.split(','))
    name_list = list(name_generator)
    name_list.sort()
    for name in name_list:
        position_score = name_list.index(name) + 1
        characters = list(name)
        char_score = 0
        for char in characters:
            char_score += alphabet.index(char) + 1
        name_score = position_score * char_score
        total_score += name_score

print(total_score)