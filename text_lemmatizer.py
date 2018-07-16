'''ИМЕЕТ ДЕЛО ТОЛЬКО С ФАЙЛАМИ, ГДЕ ЕСТЬ ПРЕФИКС TEXT'''

import pymystem3
from collections import Counter

def stemming(text):
    lemmas = stemmer.lemmatize(file_path=text, speedup=True)
    lemma_stat = sorted(Counter(lemmas).most_common(), key=lambda x: (-x[1], x[0]))
    over_file.write('Number of tokens: {}\n'.format(len(lemmas)))
    over_file.write('Number of lemmas: {}\n\n'.format(len(lemma_stat)))
    for tuple in lemma_stat:
        over_file.write('{:<2}: {}\n'.format(tuple[1], tuple[0]))


texts_name = 'text.txt'
over_file = open('text_lemmas.txt', 'w', encoding='utf-8')

stemmer = pymystem3.Mystem(disambiguation=False, entire_input=False)
stemming(texts_name)

over_file.close()
