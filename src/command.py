
class Command:
  valid = ["print", "sortby", "add", "exit"]

  def __init__(self, command):
    if command not in self.valid:
      print("Invalid command, Valid commands are: ")
      print(*self.valid, sep="\n")
    self.command = command

  def execute(self, data, columns):
    if self.command == "exit":
      print("Exiting")
      exit()
    elif self.command == "print":
      self.print(data)
    elif self.command == "add":
      self.add(data, columns)
    elif self.command == "sort":
      self.sort(data, columns)


  def print(self, data):
    rows_to_print = input("Please enter how many rows you would like printed: \n")
    for row in data[:int(rows_to_print)]:
      print(*row)

  def add(self, data, columns):
    new_row = []
    for col in columns:
      col_info = input(f"Please enter the value for {col}: ")
      new_row.append(col_info)
    print("Row to be added: ")
    print(*new_row)
    data.append(new_row)
