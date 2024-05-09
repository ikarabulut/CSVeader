
class Command:
  valid = ["print", "sortby", "add", "exit"]
  def __init__(self, command):
    if command not in self.valid:
      print("Invalid command, Valid commands are: ")
      print(*self.valid, sep="\n")
    self.command = command

  def execute(self):
    if self.command == "exit":
      print("Exiting")
      exit()