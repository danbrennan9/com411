import csv
import matplotlib.pyplot as plt #import required modules

def read_data():
  with open ("visual/subplots/temps.csv") as csv_file: #open required file
    csv_reader = csv.reader(csv_file) #open the file in a csv reader
    header = next(csv_reader) #skip the header
    data = {
      "week 1":[],
      "week 2":[] #create a dictionary, the key being the header week 1, the contents being a list, same for week 2
    }
    
    for line in csv_reader: #for each line in the reader
      data["week 1"].append(int(line[0].strip())) #add the contents of line 0 to week 1's list as an integer, stripped
      data["week 2"].append(int(line[1].strip())) #add the contents of line 1 to week 2's list as an integer, stripped
     #THIS MEANS THAT WEEK 1 AND WEEK 2 ARE THE KEYS, THE LIST ARE THE VALUES
    return data #return the dictionary

def run():
  data = read_data() #read the dictionary provided by function
  fig, axs = plt.subplots(2, 1) #create a subplot of 2 rows 1 column

  axs[0].plot(range(1,8), data["week 1"]) #plot the contents of axs as follows: go from 1 to 7, with the y axis (contents) being datas (local variable) key "week 1"'s values
  axs[1].plot(range(1,8), data["week 2"]) #same as
  plt.tight_layout()
  plt.show()

run()

