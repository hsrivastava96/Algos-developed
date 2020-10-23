def anagram(arr, i, max_Str, key):
#    print("Start", arr, i)
#    print(str(arr) > str(key))
#    print(str(arr) <= str(max_Str))
#    print(max_Str)
    if(i == len(arr)):
        if(str(arr) > str(key) and str(arr) <= str(max_Str)):
            max_Str = arr
#        print(arr)
    else:
        for j in range(i, len(arr)):
#            print("J = ", j, arr)
            s = list(arr)
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            str1 = ""
            s_A = str1.join(s)
            max_Str = anagram(s_A, i+1, max_Str, key)
    return max_Str

print(anagram("DCBA", 0, "ZZZZ", "DCBA"))    
