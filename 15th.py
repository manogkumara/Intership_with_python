input_string = 'thequickbrownfoxjumpsoverthelazydog'
char_count = {}
for char in input_string:
    if char.isalpha():  
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

for char, count in char_count.items():
    if count > 1:
        print(f"{char} {count}")
