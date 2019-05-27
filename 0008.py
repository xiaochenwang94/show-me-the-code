from bs4 import BeautifulSoup

def find_the_content(path):
    with open(path) as f:
        text = BeautifulSoup(f, 'lxml')
        content = text.get_text().replace('\n', '')

        return content


if __name__ == '__main__':
    print (find_the_content('Show-Me-the-Code_show-me-the-code_1.html'))
