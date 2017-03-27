import docindex
import os

if __name__ == '__main__':
  docName = input("Enter document name or ENTER to quit testing: ")
  try:
    with open(docName):
      docName = docindex()
      print('Testing __str__ method: w/a \'print\' statement')
      stringMethod = docindex.__str__()
      print(stringMethod)
      
      print('Testing get_label method')
      label = docindex.get_label()
      print(label)
      
  except IOError:
    print('Could not open / read file \'',docName,'\'')
