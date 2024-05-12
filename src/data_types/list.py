from abc import ABC, abstractmethod

class List(ABC):
  @abstractmethod
  def insert_front(self, element): pass


  @abstractmethod
  def insert_back(self, element): pass


  @abstractmethod
  def insert_preferred(self, element): pass

  @abstractmethod
  def insert_back(self, element): pass

  @abstractmethod
  def __getitem__(self, idx): pass

  @abstractmethod
  def __iter__(self): pass

  @abstractmethod
  def selection_sort(self, key=lambda a:a): pass

  @abstractmethod
  def merge_sort(self, key=lambda a:a): pass

