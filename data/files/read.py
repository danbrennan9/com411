def search(file_name):
  
  print("Searching...\n")
  
  with open(file_name) as file: #whatever variable is given to file name, open that variable
    for line in file: #for each line in the file, do the following
      print(f"Looked in {line}\n")
  
  print("...Done!")

def run():
  search("data/files/txt/locations.txt")

run()