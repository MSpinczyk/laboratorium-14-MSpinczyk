from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output

def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    
    return word in text

# Funkcje napisane przeze mnie znajdują się poniżej

def bubble_sort(list_1: list):
    if not isinstance(list_1,list):
        return None
    n = len(list_1)
    while n > 0:
        for i in range(0,n-1):
            if list_1[i] > list_1[i+1]:
                el = list_1[i]
                list_1[i] = list_1[i+1]
                list_1[i+1] = el
        n = n-1
    return list_1

def matrix_multiplication(m1,m2):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result