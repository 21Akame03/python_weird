# fibonacci until that number
def fibonacci(num):
    array = []
    for i in range(num):
        if i > 3 :
            count = array[i -1] + array[i-2]
            array.append(count)
            continue
        
        array.append(i)
    print(array)

fibonacci(10)
