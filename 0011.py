with open('0011.txt', 'r') as f:
    filtered_words = f.readlines()
filtered_words = [x.strip() for x in filtered_words]
while True:
    word = input()
    if word in filtered_words:
        print('Freedom')
    else:
        print('Human Rights')
