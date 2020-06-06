def findExtraCharacter(strA, strB): 
  
    # store string values in map 
    m1 = {} 
  
    # store second string in map  
    # with frequency 
    for i in strB: 
        if i in m1: 
            m1[i] += 1
        else: 
            m1[i] = 1
  
    # store first string in map  
    # with frequency 
    for i in strA: 
        m1[i] -= 1
  
    for h1 in m1: 
  
        # if the frequency is 1 then this 
        # character is which is added extra 
        if m1[h1] == 1: 
            return h1 
  
# Driver Code 
if __name__ == "__main__": 
  
    # given string 
    strA = 'pqwert'
    strB = 'pqwerty'
  
    # find Extra Character 
    print(findExtraCharacter(strA, strB)) 