def missingChars(s): 
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
  
#store missing character in alphabetic order
res = ""; 
for  p in range(0,26):
    if(s[i] == False):
        res.push_back((char)(p+'a'));

        return res;

sentence = "The quick brown fox jumps over the  lazy dog"

print(missingChars(sentence))