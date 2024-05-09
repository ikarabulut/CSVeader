from command import Command

class Program:
  valid_command = ["print", "sortby", "add", "exit"]
  def __init__(self, data, columns):
    self.data = data
    self.col = columns
    self.exit = False

  def run(self):
    while True:
      command = Command(input("please enter a command: \n"))
      command.execute()


