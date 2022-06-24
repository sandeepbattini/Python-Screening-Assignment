#Creating a class to show or replace the content in the text file
class File:
    
    #Creating method to show the contents of the file
    def show(location):
        #open the file in reading mode by taking the location of the file from instance 
        fileLocation = open(location,'r')
        
        #Storing the content of the file in a variable
        content = fileLocation.read()
        
        return content
    
    #Creating a method to replace the old word by new word
    def replace(location,replace,new):
        file = open('location','r')
        content = file.read()
        replaceWord = replace
        newWord = new
        
        #Creating a variable which contains the changed content of the file
        newFile = content.replace(replaceWord,newWord)
        return newFile

showFile = File.show('example.txt')
print(showFile)
newFile = File.replace('example.txt','placement','screening')
print(newFile)