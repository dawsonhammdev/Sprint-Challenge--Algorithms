'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word): 
    target = "th"
    n1 = word
    n2 = target
    # Base Case
    if len(word) == 0:
        return 0
    if (word[0 : n1] == target): 
        return count_th(word[n2 - 1:],  
                             target) + 1
