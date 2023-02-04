def count_letter(word_list, letter):
    count = 0
    for word in word_list:
        if letter in word:
            count += 1
    return count


list_words = ["python", "c++", "c", "scala", "java"]

print(count_letter(list_words, "c"))
