import docx
import requests
import time
from bs4 import BeautifulSoup
from settings import BASE_DIR
import json
import traceback
from fake_useragent import UserAgent
import pymorphy2

ua = UserAgent()
user_agent = ua.random
morph = pymorphy2.MorphAnalyzer()

with open('books.txt') as file:
    words = file.read().split('\n')

dictionary = {}

def get_response(url, word, count=0):
    time.sleep(0.2)
    headers = {'User-Agent': user_agent}
    if count == 11:
        return None
    try:
        response = requests.get(f'{url}{word}', headers=headers)
    except:
        time.sleep(4)
        return get_response(url, word, count=count+1)
    return response

def get_synonyms(word, repeat=False, count_error=0):
    if count_error == 5:
        return []
    try:
        if repeat:
            word = word.replace('ая', 'ость')
        url = 'https://kartaslov.ru/%D1%81%D0%B8%D0%BD%D0%BE%D0%BD%D0%B8%D0%BC%D1%8B-%D0%BA-%D1%81%D0%BB%D0%BE%D0%B2%D1%83/'
        sin = []
        response = get_response(url, word)
        if response is None:
            if not repeat:
                return get_synonyms(word, repeat=True)
            return sin
        if 'Прямых синонимов не найдено.' in response.text:
            if not repeat:
                return get_synonyms(word, repeat=True)
            return sin
        soup = BeautifulSoup(response.text, 'lxml')
        ul = soup.find('ul', {'class': 'v2-syn-list'})
        links = ul.find_all('a')
        for link in links:
            if len(sin) == 5:
                break
            if not repeat:
                m = morph.parse(link.text)
                if m:
                    if 'ADJF' in m[0].tag or 'ADJS' in m[0].tag:
                        if link.text not in sin and not link.text.endswith('ющий'):
                            sin.append(link.text)
            else:
                if link.text.endswith('ость') and link.text not in sin:
                    sin.append(link.text)
        if not sin and not repeat:
            return get_synonyms(word, repeat=True)
        return sin
    except:
        return get_synonyms(word, count_error=count_error+1)

def get_antonyms(word, repeat=False, count_error=0):
    if count_error == 5:
        return []
    try:
        if repeat:
            word = word.replace('ая', 'ость')
        url = 'https://ru.wiktionary.org/wiki/'
        word = word[1:]
        antonym = []
        response = get_response(url, word)
        # print(response.text)
        if response is None:
            if not repeat:
                return get_antonyms(word, repeat=True)
            return antonym
        if 	'В настоящий момент текст на данной странице отсутствует' in response.text:
            if not repeat:
                return get_antonyms(word, repeat=True)
            return antonym
        soup = BeautifulSoup(response.text, 'lxml')
        tags = soup.find('div', {'class': 'mw-parser-output'}).find_all(recursive=False)
        links = []
        flag = False
        for ind, tag in enumerate(tags):
            # print(tag)
            if flag:
                if tag.name == 'ol':
                    a = tag.find_all('a')
                    links = a
                    break
            else:
                spans = tag.find_all('span')
                for span in spans:
                    if span is not None:
                        if span.get('id') == 'Антонимы':
                            # print(span, 'span')
                            flag = True
                            break
                continue
        
        for link in links:
            if len(antonym) == 5:
                break
            if not repeat:
                m = morph.parse(link.text)
                if m:
                    if 'ADJF' in m[0].tag or 'ADJS' in m[0].tag:
                        if link.text not in antonym and not link.text.endswith('ющий'):
                            antonym.append(link.text)
            else:
                if link.text.endswith('ость') and link.text not in antonym:
                    antonym.append(link.text)
        if not antonym and not repeat:
            return get_antonyms(word, repeat=True)
        return antonym
    except:
        return get_antonyms(word, count_error=count_error+1)
            

words = ["нежная", ""]

try:
    for ind, word in enumerate(words, start=1):
        print(word, f'{ind}/{len(words)}')
        if word:
            if word[0] == '-':
                ant = get_antonyms(word)
                dictionary[word] = ant
            else:
                sin = get_synonyms(word)
                dictionary[word] = sin
except:
    print(traceback.format_exc())


with open(BASE_DIR.joinpath('words7.json'), 'w', encoding='utf-8') as f:
    json.dump(dictionary, f, ensure_ascii=False, indent=4)


# if __name__ == '__main__':
#     syn = []
#     for word in words[0:100]:
#         if word.startswith('-'):
#             syn = get_antonyms(word)
#             print(syn, '|||', word)