'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # if the word has no letters then return 0
    if word == "":
        return 0
    # if the word between the first two letters contains "th"
    if word[0:2] == 'th':
        # return recursivley the function at the 1: position and add 1
        return 1 + count_th(word[1:])
    # else return the recursive call at 1:
    else:
        return count_th(word[1:])
        
    
    
