# Implement your function below.
# Implement your function below.
def most_frequent(given_list):
    occurence = {}
    max_occurred=0
    max_item=''
    for num in given_list:
        if num in occurence:
            occurence[num] +=1
        else:
            occurence[num] =1
        if occurence[num] > max_occurred:
            max_occurred = occurence[num]
            max_item = num
    return max_item if max_item !='' else None



# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1.
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3.
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None.
list3 = []
# most_frequent(list4) should return 0.
list4 = [0]
# most_frequent(list5) should return -1.
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
print (most_frequent(list5))