from fadame import FadapaObj, load_one, load_many, merge, fadame_merge
# content of test_sample.py
def inc(x):
    return x + 1

all_reads = [
  "tests/sampleId_1_1.fastqc.data.txt",
  "tests/sampleId_1_2.fastqc.data.txt",
  "tests/sampleId_2_1.fastqc.data.txt",
  "tests/sampleId_2_2.fastqc.data.txt",
  "tests/sampleId_3_1.fastqc.data.txt",
  "tests/sampleId_3_2.fastqc.data.txt",
  "tests/sampleId_4_1.fastqc.data.txt",
  "tests/sampleId_4_2.fastqc.data.txt",
  "tests/sampleId_5_1.fastqc.data.txt",
  "tests/sampleId_5_2.fastqc.data.txt",
  "tests/sampleId_6_1.fastqc.data.txt",
  "tests/sampleId_6_2.fastqc.data.txt",
  "tests/sampleId_7_1.fastqc.data.txt",
  "tests/sampleId_7_2.fastqc.data.txt",
  "tests/sampleId_8_1.fastqc.data.txt",
  "tests/sampleId_8_2.fastqc.data.txt"
]

def test_answer():
    assert inc(3) == 4

def test_merge():
    expected = load_one('tests/merged.fastqc.data.txt')
    merged = merge(all_reads)
    assert False
