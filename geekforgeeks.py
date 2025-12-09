def create_dict(arr):
    N = len(arr)
    dict = {}

    # Your code here
    # Hint: use loop to iterate through arr
    # and assign key value to the dict
    for i in range(N):
        dict[arr[i]] = i + 1

    return dict

names = [john, ala, ilia, sudan, mercy] 
marks = [100, 200, 150, 80, 300]
create_dict