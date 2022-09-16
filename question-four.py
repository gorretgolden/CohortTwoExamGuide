#4(c)file handling


#global varriable number of words
total_words = 0
 
#opening the text file for reading mode
with open(r'data.txt','r') as file:
 
    
    content = file.read()
 
    # Splitting the content into separate lines
    lines = content.split()
 

    #update the global varriable
    total_words += len(lines)
 
 
# Printing total number of words in the file
print('Total number of words in the file is:',total_words)



#4(d)