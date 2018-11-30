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
BASIC_STATISTICS_MEASURE_ORDERS = { 
  'Filename':0, 
  'File type': 1, 
  'Encoding': 2,
  'Total Sequences': 3,
  'Sequences flagged as poor quality': 4,
  'Sequence length': 5,
  '%GC':6
}

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

BASIC_STATISTIC_FIELD_TO_MERGE = ['Sequences flagged as poor quality', 'Total Sequences']
def addSortable(module):
  def func(obj):
    data = obj.clean_data(module)
    headers = data[0]
    if module == 'Basic Statistics':
      orders = BASIC_STATISTICS_MEASURE_ORDERS
      objectValue = { value[0]: (int(value[1]) if value[0] in BASIC_STATISTIC_FIELD_TO_MERGE else value[1]) for value in data[1:] }
    else:
      orders = { value[0]: int(value[0].split('-')[0]) for value in data[1:] }
      objectValue = { value[0]: float(value[1]) for value in data[1:] }
    return headers, orders, objectValue
  return func

def mergeByModule(module):
  def reduced(acc, value):
    (accHeaders, accOrders, accObjectValue) = acc
    (headers, orders, objectValue) = value
    for k, v in objectValue.iteritems():
        if k in accObjectValue:
          if module == 'Basic Statistics':
            if k in BASIC_STATISTIC_FIELD_TO_MERGE:
              accObjectValue[k] += v
          else:
            accObjectValue[k] += v
        else:
          accObjectValue[k] = v
    accOrders.update(orders)
    return (headers, accOrders, accObjectValue)
  return reduced

def merge(fadapas):
  fadapaObjs = load_many(fadapas)
  output = "##FastQC	0.11.8\n"
  summaries = map(lambda obj: { v[1]: (v[0] == "pass") for v in obj.summary()[1:] }, fadapaObjs)
  summary = reduce(lambda acc, obj: { k: acc[k] and v for k, v in obj.iteritems() }, summaries)
  for module in MODULE_TO_MERGE:
    output += ">>%s\t%s\n" % (module, "pass" if summary[module] else "warn")
    parsed = map(addSortable(module), fadapaObjs)
    (headers, orders, objectValue) = reduce(mergeByModule(module), parsed[1:], parsed[0])
    output += "#%s\n" % ("\t".join(headers))
    for key, value in sorted(orders.iteritems(), key=lambda (k,v): (v,k)):
      output += "%s\t%s\n" % (key, objectValue[key])
    output += ">>END_MODULE\n"
  # print(fadapaObjs[0].clean_data('Basic Statistics'))
  # print(fadapaObjs[0].summary())
  return output

def fadame_merge(args):
  with open(args.output, 'w') as f:
    f.write(merge(args.input))
 
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
