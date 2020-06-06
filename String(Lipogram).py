alphabet = 'abcdefghijklmnopqrstuvwxyz'

def panLipogram(s):
    s.lower()

    #variable to keep count of all the letters
    #not found in the string
    counter = 0
    #traverse the string for every letter of the alphabet
    for ch in alphabet:
        # character not found in string then increment count
        if(s.find(ch)<0):
            counter += 1

    if(counter == 0):
        result = "Panagram"

    elif (counter == 1):
        result= "Pangrammatic Lipogram"

    else:
        result = "Not a panagram but might a lipogram"

    return result

def main(): 
    print(panLipogram("The quick brown fox jumped over the lazy dog")) 
      
    print(panLipogram("The quick brown fox jumps over the lazy dog")) 
  
    print(panLipogram("The quick brown fox jump over the lazy dog")) 
      
  
if __name__ == '__main__': 
    main() 
 
