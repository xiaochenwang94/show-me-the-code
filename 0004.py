def word_count(filename):
    line_counts = 0
    word_counts = 0
    character_counts = 0
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            line_counts += 1
            word_counts += len(words)
            character_counts += len(line)
    return line_counts, word_counts, character_counts

print(word_count("0002.py"))