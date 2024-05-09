import sys
import csv

from program import Program

if len(sys.argv) <= 1:
      print("please enter location of the csv you would like to read")
      exit()

csv_location = sys.argv[1]

csv_l = []
columns = []

with open(csv_location, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0

    csv_l = list(csv_reader)
    columns = csv_l[0]

    del(csv_l[0])


program = Program(csv_l, columns)
program.run()