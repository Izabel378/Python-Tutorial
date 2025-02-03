def count_syllables(word):
    vowels = "aeiouy"
    count = 0

    if len(word) <= 3:
        return 1

    for i in range(1, len(word)):
        if word[i] in vowels and word[i - 1] not in vowels:
            count += 1

    if word.endswith("e"):
        count = max(1, count - 1)

    return count

def calculate_flesch_index(text):
    words = text.split()
    sentences = text.split(". ")

    total_syllables = sum(count_syllables(word.lower().strip(",.!?")) for word in words)

    avg_syllables_per_word = total_syllables / len(words)
    avg_words_per_sentence = len(words) / len(sentences)

    flesch_index = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
    grade_level = 0.39 * avg_words_per_sentence + 11.8 * avg_syllables_per_word - 15.59

    return flesch_index, grade_level

with open("flesch.txt", "r") as file:
    text = file.read()

flesch_index, grade_level = calculate_flesch_index(text)

print(f"Flesch Index: {flesch_index:.2f}")
print(f"Grade Level: {grade_level:.2f}")
