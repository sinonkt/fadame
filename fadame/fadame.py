import sys
import glob
import argparse
from fadapa import Fadapa

def fadame_merge(args):
  print('test')
  print(args)

def main():
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('-i', '--input', metavar='GLOB', type=str, nargs='+',
                      help='Any input files or globs of fastqc_data.txt you wish to merge\nExp: *_1.fastqc.data.txt',
                      dest='input')
  parser.add_argument('-o', '--out', dest='output',
                      help='Merged file name.'
                      )
  args = parser.parse_args()
  fadame_merge(args)

if __name__ == '__main__':
  main()