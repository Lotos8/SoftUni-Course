# "1. Strings\n"
# "2. Numbers\n"
# "3. Booleans\n"
# "4. Additional Data Types (List, Tuple, Dictionary)\n"
sentence = "Learning Python is fun!"
first_part_of_sentences = sentence[0:8]
second_part_of_sentences = sentence[16:23]
all_parts_together = first_part_of_sentences + ' ' + second_part_of_sentences
uppercase_string = all_parts_together.upper()
print(uppercase_string)
replacement_string = uppercase_string.replace("FUN", "AWESOME")
print(replacement_string)