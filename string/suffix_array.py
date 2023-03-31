def get_suffix_array_with_suffixes(given_string, algorithm="Manber-Myers"):
    if(algorithm == "Manber-Myers"):
        def compare(x, y, t):
            return suffix_array[x][t//2:t] < suffix_array[y][t//2:t]
        
        suffix_array = []
        suffix_number = []
        size = len(given_string)
        for i in range(size):
            suffix_array.append(given_string[i:])
            suffix_number.append(i)
        
        t = 1
        next_group = [0, size]
        while(t<=size):
            new_group = [0]
            for i in range(1, len(next_group)):
                suffix_number[next_group[i-1]:next_group[i]] = \
                    sorted(
                        suffix_number[next_group[i-1]:next_group[i]],
                        key = lambda x: suffix_array[x][t//2:t])

                for j in range(next_group[i-1], next_group[i]):
                    if(suffix_array[suffix_number[j-1]][t//2:t] != suffix_array[suffix_number[j]][t//2:t]):
                        new_group.append(j)
                new_group.append(next_group[i])

            next_group = new_group
            t = t*2

        return suffix_number, [suffix_array[x] for x in suffix_number]
    
def get_suffix_array(given_string):
    suffix_array, _ = get_suffix_array_with_suffixes(given_string)
    return suffix_array
    
def get_LCP_array(given_string, algorithm="kasai"):
    if(algorithm == "kasai"):
        size = len(given_string)
        suffix_array = get_suffix_array(given_string)
        suffix_array, suffixes = get_suffix_array_with_suffixes(given_string)
        
        ranks = [0] * size
        lcp_array = [0] * size

        for rank, i in enumerate(suffix_array):
            ranks[i] = rank
        
        lcp = 0
        for i in range(size):
            j = suffix_array[ranks[i]-1]
            while(j+lcp < size and given_string[i+lcp] == given_string[j+lcp]):
                lcp+=1
                
            lcp_array[ranks[i]] = lcp

            if(lcp > 0):
                lcp-=1
            

        return lcp_array
            

            






if __name__ == "__main__":
    test_word = "banana"
    suffix_array, suffixes = get_suffix_array_with_suffixes(test_word)
    print(suffix_array)
    print(suffixes)
    lcp_array = get_LCP_array(test_word)
    print(lcp_array)
