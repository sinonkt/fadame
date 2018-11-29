from fadame import FadapaObj, load_one, load_many, merge, fadame_merge
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

def test_fadame_merge():
    assert fadame_merge([])

def test_merge():
    expected = load_one('tests/merged.fastqc.data.txt')
    merged = merge([])
    assert expected == merged
