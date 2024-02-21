def join_array_remove_duplicate(arrayA, arrayB):
    result_array = arrayA.copy()
    for x in arrayB:
        if x not in result_array:
            result_array.append(x)
        
    unique_array = []
    for i in result_array:
        if i not in unique_array:
            unique_array.append(i)
    return unique_array

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
