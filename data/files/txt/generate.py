def search(file_name):
  print("Searching...", end = "")
  data = {}
 
  with open(file_name) as file: #opens whatever file was given to the search function
    section_name = ""
    for line in file: #for each line within the file
      if (line.startswith("Section")): #if the line starts with this 
        section_name = line.split(":")[1].strip() #take the line, strip it, then take the second piece
        

      else:
        if section_name in data: #if that section name already exists within the data
          data[section_name].append(line.strip()) #add the name
        else:
          data[section_name] = [line.strip()] #if not, create a new list containing the name


  print("Done!")
  return data #return the code

def run():
  data = search("data/files/txt/books.txt")
  with open("data/files/txt/generated.csv", "w") as file: #opens a new file for write
    for section, books in data.items(): #for the 1st, and 2nd part of the items in data
      for book in books: #for each items in books
        file.write(f"{section},{book}\n") #write the section name, then the book

run()



