import csv
import matplotlib.pyplot as plt 

def read_data():
  with open ("train.csv") as csv_file: 
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    
    data = {
      "survived":[],
      "age":[], 
      "sex":[],
      "fare":[]
    }
    
    for line in csv_reader:
      survived = line[1].strip()
      age = line[5].strip()
      sex = line[4].strip()
      fare = line[9].strip()

      if (len(survived) == 0 or len(age) == 0 or len(sex) == 0 or len(fare) == 0):
        continue
      else:
       data["survived"].append(int(survived))
       data["age"].append(float(age))
       data["sex"].append(sex)
       data["fare"].append(float(fare))
    
    return data 

def run():
  data = read_data()
  fig, axs = plt.subplots(2, 2)

  axs[0,0].bar(data["survived"], data["age"])
  axs[0,1].plot(data["sex"], data["survived"])
  axs[1,0].bar(data["survived"], data["fare"])
  axs[1,1].bar(data["fare"], data["age"])
  
  plt.tight_layout()
  plt.show()

run()