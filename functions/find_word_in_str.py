
def find_word_in_str(total_str=str, key=str):
    """
    Allows to find a word in a string object
    (Sensible to lower case etc)

    Parameters:
    total_str: Complete string to look for key in
    key: Character sequence to find

    Returns:
    indexes_list: list
    List of tuples of starting and ending indices of where the word is in the total string

    Example:
    ```
    python
    Password1 = 'MyNamename0000'
    Password2 = 'MyNameName1111'
    first_ex_list = find_word_in_str(Password1, 'Name')
    second_ex_list = find_word_in_str(Password2, 'Name')
    ```
    first_ex_list will be [(1,5)]
    while second_ex_list will be [(1,5), (5,9]
    """
    total_length = len(total_str)
    key_length = len(key)
    index_count = 0
    count = 0
    relative_length = total_length - key_length
    indexes_list = []
    while index_count<relative_length:
        start = index_count
        end = index_count + key_length
        testing_seq = total_str[start:end]
        if testing_seq == key:
            indexes_list.append((start,end))
            count+=1
        index_count+=1
    if count>0:
        print(f"|{key}| was found {count} time(s) in the string.")
    else:
        print(f"|{key}| wasn't found in the string.")
    return(indexes_list)