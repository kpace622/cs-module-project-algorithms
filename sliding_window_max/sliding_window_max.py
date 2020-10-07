'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    new_list = []
    start = nums[0] -1 
    end = k
    # print(end)
    # while end += 1 is not None:
    #     window = nums[start:end]
    #     print(window)
    #     start += 1
    #      += 1
    # return -1


    for x in nums:
        window = nums[start:end]
        if len(window) >= k:
            print(window)
            new_list.append(max(window))
            start += 1
            end += 1
        else:
            return new_list




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
