def replace_not_poor(input_str):
    not_index = input_str.find('not')
    poor_index = input_str.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return input_str[:not_index] + 'good' + input_str[poor_index + 4:]
    else:
        return input_str
sample_str1 = 'The lyrics is not that poor!'
sample_str2 = 'The lyrics is poor!'
result_str1 = replace_not_poor(sample_str1)
result_str2 = replace_not_poor(sample_str2)

print(result_str1)  # Output: 'The lyrics is good!'
print(result_str2)  # Output: 'The lyrics is poor!'
