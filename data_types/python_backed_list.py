from .list import List

class PythonBackedList(List):
  def __init__(self):
    self.contents = []

  def insert_front(self, element):
    self.contents[:0] = [element] 

  def insert_back(self, element): 
    self.contents[len(self.contents):] = [element] 

  def insert_preferred(self, element):
    self.contents[len(self.contents):] = [element] 

  def __getitem__(self, idx):
    return self.contents[idx]

  def __iter__(self):
    return iter(self.contents)

  def selection_sort(self, key=lambda a:a): pass
  def merge_sort(self, key=lambda a:a): pass