from bs4 import BeautifulSoup

def find_all_a(path):
    ret = []
    with open(path, 'r') as f:
        text = BeautifulSoup(f, 'html.parser')
        text = text.find_all('a')
        for t in text:
            print(t['href'])
            ret.append(t['href'])
    return ret

find_all_a('Show-Me-the-Code_show-me-the-code_1.html')

