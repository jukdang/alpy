def get_suffix_array(given_string, algorithm="Manber-Myers"):
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


if __name__ == "__main__":
    test_word = "bananakangchanseok"
    suffix_array, suffixes = get_suffix_array(test_word)
    print(suffix_array, suffixes)
