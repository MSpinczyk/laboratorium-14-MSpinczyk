from app import hello, extract_sentiment, text_contain_word, bubble_sort, matrix_multiplication
import pytest

def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata = ["I think today will be a great day","I do not think this will turn out well"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

# Testy napisane przeze mnie znajdują się poniżej

testdata = [
    ([4,3,7,9,1,4,6,8,1], [1,1,3,4,4,6,7,8,9]),
    ([9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9]),
    ([2,3,2,3,2,3,2,3,2], [2,2,2,2,2,3,3,3,3]),
    ([],[]),
    ([11,12,13,14,8,7,5], [5,7,8,11,12,13,14]),
    ('string', None)
    ]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_bubble_sort(sample, expected_output):

    assert bubble_sort(sample) == expected_output


testdata = [
    ([[1,2,3],[1,2,3],[1,2,3]], [[1,1,1],[1,1,1],[1,1,1]], [[6,6,6],[6,6,6],[6,6,6]])
    ]

@pytest.mark.parametrize('m1, m2, expected_output', testdata)
def test_matrix_multiplication(m1, m2, expected_output):

    assert matrix_multiplication(m1, m2) == expected_output

# Zgodnie z oczekiwaniami wszystkie testy oprócz jednego przeszły, jeden celowo nie przeszedł jest to ten z konspektu do zajęć.
# Testy są bardzo przydatne w momencie gdy znamy wynik jakiejś operacji a chcemy zobaczyć czy nasz kod działa poprawnie.
# Na zajęciach zapoznałem się z tymi pytestami przez co w przyszłości nie będę miał problemów z ich implementacja, może nawet dla
# bardziej złożonych funkcji.