import pymystem3
from collections import Counter

def stemming(text):
    lemmas = stemmer.lemmatize(text, speedup=True)
    lemma_stat = Counter(lemmas).most_common()
    for tuple in lemma_stat:
        print('{}: {}'.format(tuple[1], tuple[0]))
    print('\n#####\n')
    over_file.write('Number of tokens: {}\n'.format(len(lemmas)))
    over_file.write('Number of lemmas: {}\n\n'.format(len(lemma_stat)))


texts_file = open('SampleRU.txt', 'r', encoding='utf-8')
over_file = open('overview.txt', 'w', encoding='utf-8')

stemmer = pymystem3.Mystem(disambiguation=False, entire_input=False)
new_text = True
text_str = ''

for line in texts_file:
    # если встречается разделитель между текстами, заводим новые переменные
    if line == '####\n':
        stemming(text_str)
        new_text = True
        text_str = ''
        continue
    # записываем название текста
    elif new_text:
        over_file.write(line.upper())
        new_text = False
    # пишем текст в одну строку
    else:
        text_str += line
stemming(text_str)

texts_file.close()
over_file.close()
