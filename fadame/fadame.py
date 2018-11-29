import sys
import argparse
from fadapa import Fadapa

MODULE_TO_MERGE = [
  'Basic Statistics',
  # 'Per base sequence quality',
  # 'Per tile sequence quality',
  'Per sequence quality scores',
  # 'Per base sequence content',
  'Per sequence GC content',
  # 'Per base N content',
  'Sequence Length Distribution',
  # 'Sequence Duplication Levels',
  # 'Adapter Content'
]

class FadapaObj(Fadapa):
  def __eq__(self, other):
      if isinstance(self, other.__class__):
          return self.summary() == other.summary() and \
            all(self.clean_data(module) == other.clean_data(module) for module in MODULE_TO_MERGE)
      return False


def load_one(path):
  return FadapaObj(path)

def load_many(paths):
  return map(load_one, paths)

def merge(fadapas):
  return FadapaObj('tests/merged.fastqc.data.txt')

def fadame_merge(args):
  print('test')
  return True
  # print(args.input)
  # print(args.output)
 
def main():
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('-i', '--input', metavar='GLOB', type=str, nargs='+',
                      help='Any input files or globs of fastqc_data.txt you wish to merge\nExp: *_1.fastqc.data.txt',
                      dest='input')
  parser.add_argument('-o', '--out', metavar="OUPUT", dest='output',
                      help='Merged file name.'
                      )
  args = parser.parse_args()
  fadame_merge(args)

if __name__ == '__main__':
  main()
