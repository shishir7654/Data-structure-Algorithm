#Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

#Examples : The quick brown fox jumps over the lazy dog ” is a Pangram [Contains all the characters from ‘a’ to ‘z’]

def checkPangram(s): 
    List = [] 
    # create list of 26 charecters and set false each entry 
    for i in range(26): 
        List.append(False) 
          
    # converting the sentence to lowercase and iterating 
    # over the sentence  
    for c in s.lower():  
        if not c == " ": 
  
            # make the corresponding entry True 
            List[ord(c) -ord('a')]= True 
              
    # check if any charecter is missing then return False 
    for ch in List: 
        if ch == False: 
            return False
    return True
  
# Driver Program to test above functions 
sentence = "The quick brown fox jumps over the  lazy dog"
  

if (checkPangram(sentence)): 
    print ('"'+sentence+'"')
    print ("This is a pangram")
else: 
    print ('"'+sentence+'"')
    print ("This is not a pangram")
