def search(file_name): #1st function, requires an argument (the name of the file)
  
  print("Searching...")
  
  sections = [] #creating two lists
  books = []

  with open(file_name) as file: #opening the file
    
    for line in file: #for each line within the file, do this:
      
      if line.startswith("Section"): #if the line starts with the txt section, then
        section_name = line.split(":")[1] #split the section line from the colon, and take the 2nd piece, the turn this into a  local variable
        sections.append(section_name.strip()) #add the new variable to the sections list
      
      else:
        books.append(line.strip()) #else do the same process for books list

    print("Done!")

    return (sections, books)

def save(file_name, data): #2nd function, requires two arguments, the name of the file, and data from function 1
  print("Saving...")
  with open(file_name, "w") as file: #open the file in write mode
    file.write(f"Sections: {data[0]}") #write the first piece of data (sections) created by the first function in file
    file.write(f"Books: {data[1]}") #same process but for the books data from function 1
    print("Done!")

def run():
  data = search("data/files/txt/books.txt") #define the data
  save("data/files/txt/section-books.txt", data) #use the writing function to save a new text file

run()

