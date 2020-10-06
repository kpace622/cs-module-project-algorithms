'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    # First approach creating a new arry

    # Your code here
    # new_arr = []
    # for x in arr:
    #     if x != 0:
    #         new_arr.insert(0, x)
    #     else:
    #         new_arr.append(x)
    # return new_arr


    # Better? approach moving elements in place

    # for x in arr:
    #     if x != 0:
    #         saved = x
    #         arr.remove(x)
    #         arr.insert(0, saved)
    # return arr


    # Best? Still moving elements in place but appending 0s to the end rather than inserting at the beginning which causes reindexing 

    for x in arr:
        if x == 0:
            saved = x
            arr.remove(x)
            arr.append(saved)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")