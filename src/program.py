from command import Command

class Program:

  def __init__(self, data, columns):
    self.data = data
    self.col = columns
    self.exit = False

  def run(self):
    while True:
      command = Command(input("please enter a command: \n"))
      self.data, self.col = command.execute(self.data, self.col)


