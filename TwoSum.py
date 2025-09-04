# comparing the adjacent elements in a array
def twoSum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range( i+1, n):
            if arr[i] + arr[j] == target:
                return True
    return False           

print(twoSum([1,2,3,4,5], 9))

#HashSet

def find_sum_of_two(A, val):
    s = set() # does not allow duplicates
    for num in A:
        complement = val - num
        if complement in s:
            return True
        s.add(num)  
    return False


# Hashmap 
def two_sum(arr, t):

    # Replace this placeholder return statement with your code
    hashmap = {}
    
    for i in range(len(arr)):
        difference = t - arr[i]
        if difference in hashmap:
            return [i, hashmap[difference]]
        hashmap[arr[i]] = i
