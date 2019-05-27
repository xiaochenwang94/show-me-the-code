with open('0011.txt', 'r') as f:
    filtered_words = f.readlines()
filtered_words = list(map(lambda x: x.strip('\n'), filtered_words))
while True:
    x = input()
    for filtered_word in filtered_words:
        x = x.replace(filtered_word, '*'*len(filtered_word))
    print(x)