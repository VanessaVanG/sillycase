'''I need you to create a new function for me.
This one will be named sillycase and it'll take a single string as an argument.
sillycase should return the same string but the first half should be lowercased and the second half should be uppercased.
For example, with the string "Treehouse", sillycase would return "treeHOUSE".
Don't worry about rounding your halves, but remember that indexes should be integers. You'll want to use the int() function or integer division, //.'''

#The first one is the better answer. The second one works but it's overly complicated

def sillycase(word):
    #get the value for half of the word length
    half_val = len(word) // 2
    #lowercase first half and put in variable
    first = word[:half_val].lower()
    #Capitalize last half and put in variable
    last = word[half_val:].upper()
    #combine the two and put in variable and return
    silly = first + last
    return silly
    
def sillycase(word):
    #Capitalize everything
    word = word.upper()
    #Get the value for half of the word length
    half_val = int(len(word) / 2)
    #make the last half of word into a list with separate letters
    last = list(word[half_val:])    
    #make a list of the first half of word lowercased with separate letters
    first = list(word[:half_val].lower())
    #put two lists together
    letters = first + last
    #make that list a string and return
    silly = "".join(letters)
    return silly