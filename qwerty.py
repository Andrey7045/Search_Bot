from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json


def main(data):
    with open('train.json', 'r', encoding='utf-8') as f:
        BD = json.load(f)

    question = []
    answer = []

    for i in range(len(BD)):
        try:
            BD[i]['ANSWER']
            BD[i]['QUESTION']
            answer.append(BD[i]['ANSWER'])
            question.append(BD[i]['QUESTION'])
        except:
            pass


    # data = input()

    def canonize(source):
        stop_symbols = '.,!?:;-\n\r()'

        stop_words = (u'это', u'как', u'так',
                      u'и', u'в', u'над',
                      u'к', u'до', u'не',
                      u'на', u'но', u'за',
                      u'то', u'с', u'ли',
                      u'а', u'во', u'от',
                      u'со', u'для', u'о',
                      u'же', u'ну', u'вы',
                      u'бы', u'что', u'кто',
                      u'он', u'она')

        return [x for x in [y.strip(stop_symbols) for y in source.lower().split()] if x and (x not in stop_words)]


    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(question)
    clv = LogisticRegression()
    clv.fit(vectors, answer)
    texer = vectorizer.transform([data]).toarray()[0]
    answerw = clv.predict([texer])[0]

    return answerw