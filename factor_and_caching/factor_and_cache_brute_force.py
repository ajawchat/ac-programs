def isPrimeNo(num):
    for i in range(2,num/2):
        if num%i == 0:
            return False
    return True

# Using the caching approach, we do not have to visit all of the earlier elements unless all are prime Numbers
def caching(arr):
    print "in"
    #sort the array, so that we could have a bottom up comparison systematically
    arr = sorted(arr)
    print arr

    #create a new dictionary
    result = {}

    #initialize the first element to an empty list
    result[arr[0]] = []

    division = [2,3,5,7,11]

    for i in range(1,len(arr)):
        result[arr[i]] = []
        if isPrimeNo(arr[i]) == False:
            # Else go through the elements before arr[i]
            for j in range(i-1,-1,-1):
                print "-",arr[j]
                if arr[i] % arr[j] == 0:
                    #get the number and all of its constituents
                    newList = result[arr[i]]
                    newList.append(arr[j])
                    result[arr[i]] = newList
    print result
            


## MAIn
if __name__ == "__main__":
    arr = [10,5,2,71,70,7,20,35]

    result = {}
    flag = False
    
    for i in range(0,len(arr)):
        #print arr[i]
        for j in range(i-1,-1,-1):
            if(arr[i] % arr[j] == 0):
                #print result
                status = result.get(arr[i],"NA")
                if status == "NA":
                    newList = []
                    newList.append(arr[j])
                    result[arr[i]] = newList
                    flag = True
                else:
                    status.append(arr[j])
                    result[arr[i]] = status
                    flag = True

        if flag == False:
            newList = []
            result[arr[i]] = newList
        
    caching(arr)
    
    #print result
        
