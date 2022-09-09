def delete_letters(word):
    '''
    Input:
        word: the string/word
    Output:
        delete_l: a list of all possible strings obtained by deleting 1 character from word
    '''

    delete_l = []
    split_l = []
    
    #*** list comprehension without condition ***
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    #*** Simple form without list comprehension ***
    #for i in range(len(word)+1):
    #    splits.append([(word[:i],word[i:])])
    
    #*** list comprehension with condition ***
    delete_l = [L+R[1:] for L,R in split_l if R]
    #*** Simple form without list comprehension ***
    #for L,R in splits:
    #    if R:
    #        delete_l.append(L+R[1:])
    

    print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")
    
    return  split_l

delete_letters("nice")