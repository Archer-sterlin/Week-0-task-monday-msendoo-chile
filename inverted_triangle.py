def inverted_triangle(num):
    i = num + 3
    m = num 
    char = '*'
    for x in range(1,num):
        if num % 2 == 0:
            if m == num:
                print('',char*i)
                m -= 1
                i -= 2
            print(' '*x,char*i)    
            i -= 2
        else:
            if m == num:
                i += 1
                print('',char*i)
                m -= 1
                i -= 2
            print(' '*x,char*i)    
            i -= 2



inverted_triangle(5)

