
def listogram(lines):
    listogram = []
    
    #TODO: loop through each word in lines
    for word in lines:
      word = word.rstrip()
    
    #TODO: call get_index() and save the result to a variable
      result= get_index(word,listogram)
      if result == "nope didn't find it":
        listogram.append([word,1])
      else:
        listogram[result][1] += 1
    #TODO: if the result is the non valid index value then
    #we know the word was not found and this is the first time we have seen the word
    #in this case we will append a new inner list with the word and a count of 1
    #otherwise we have seen the word before and we need to use the result which will
    #be the index of the inner list to update the count by 1 in that inner list
    
    #TODO: return the listogram
    return listogram
    
    
    
lines = open("words.txt", "r").readlines()
print(listogram(lines))