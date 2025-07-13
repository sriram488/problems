##Find the missing number in a array
##Problem Statement -
#You are given an unsorted array of positive integers from 1 to n, where n is the length of the array. 
#The array contains all numbers from 1 to n except one number, x. Your task is to find the value of x.
#Example - [3,7,1,2,8,4,5] n=8 missing element=6

def find_missing(input):
    total = sum(input)# Calculate the sum of all elements in the input list 
    n= len(input)
    sum_of_elements = (n * (n+1)) / 2 # calculate the sum of all the numbers using (n*(n+1))/2
    missing_element = int(sum_of_elements - total)
    return missing_element
