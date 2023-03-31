def get_kmp_array(pattern):
    KMP = [-1]
    for i in range(1, len(pattern)):
        if(pattern[i] == pattern[KMP[i-1]]):
            KMP.append(KMP[i-1]+1)
        else:
            KMP.append(0)
    return KMP

def find_pattern(given_string, pattern):
    size = len(given_string)
    pattern_size = len(pattern)

    kmp_array  = get_kmp_array(pattern)
    match_indexes = []
    i = 0
    j = 0
    while(i<size):  
        if(j==-1 or given_string[i] == pattern[j]):
            i+=1
            j+=1
        else:
            j=kmp_array[j]
        
        if(j == pattern_size):
            match_indexes.append(i-j)
            j=kmp_array[j-1]

    return match_indexes

if __name__ == "__main__":
    testString = "acbabacabcdabcklasdbcabcdababcdabcklfdasgvasbaabcdabcklbcdabcklbcabacb"
    testWord = "abcdabckl"

    print(get_kmp_array(testWord))

    match_indexes = find_pattern(testString, testWord)
    print(match_indexes)
    for i in match_indexes:
        print(testString[i:i+len(testWord)], testWord)
        if(testString[i:i+len(testWord)] != testWord): 
            print("Something Wrong")
            exit()
    print("Search pattern well")