def sequence_type(arr):
    if len(arr) == 0 or len(arr) == 1:
        return "RANDOM"
    constant = True
    ascending = True
    weakly_ascending = True
    descending = True
    weakly_descending = True
    for i in range(1,len(arr)):
        if arr[i-1] == arr[i]:
            ascending = False
            descending = False
        if arr[i-1] != arr[i]:
            constant = False
        if arr[i-1] >= arr[i] and ascending and not constant:
            ascending = False
        if arr[i-1] > arr[i] and weakly_ascending:
            weakly_ascending = False
        if arr[i-1] <= arr[i] and descending and not constant:
            descending = False
        if arr[i-1] < arr[i] and weakly_descending:
            weakly_descending = False
    if constant:
        return "CONSTANT"
    if ascending:
        return "ASCENDING"
    if weakly_ascending:
        return "WEAKLY ASCENDING"
    if descending:
        return "DESCENDING"
    if weakly_descending:
        return "WEAKLY DESCENDING"
    return "RANDOM"

assert sequence_type([-530, -530, -530, -530, -530]) == "CONSTANT"

def main():
    flag = True
    arr = []
    while flag:
        elem = int(input())
        if elem == -2000000000:
            flag = False
            print(sequence_type(arr))
        arr.append(elem)

if __name__ == "__main__":
    main()