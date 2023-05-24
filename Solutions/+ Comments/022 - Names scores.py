alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total_score = 0

# Read file
with open('./p022_names.txt', encoding="utf-8") as file:
    list_file = file.read()
    # Split content on commas and strip double quotes
    name_generator = (name.strip('"') for name in list_file.split(','))
    # Convert to a list and sort it
    name_list = list(name_generator)
    name_list.sort()
    # Iterate over each name in the sorted name list
    for name in name_list:
        # Calculate the position score of the current name
        position_score = name_list.index(name) + 1
        # Convert the name into a list of characters
        characters = list(name)
        char_score = 0
        # Calculate the character score for each character in the name
        for char in characters:
            char_score += alphabet.index(char) + 1
        # Multiply the position score with the character score    
        name_score = position_score * char_score
        total_score += name_score

print(total_score)