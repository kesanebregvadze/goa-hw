def find_shortest_word_length(s):

    words = s.split()
    
    
    return min(len(word) for word in words)