def find_min(element: list):
    """TODO: complete for Step 1
    ~ check if element is a list if false return -1
      if true continue
    ~ check if list is empty if true return -1
      if not empty then continue
    ~ check if there is only 1 element then return that 1 element
    ~ check if the elements are a string then return -1
      if not continue
    ~ compare the first and last places in the list
      delete the greater one and return the new list"""
    if isinstance(element, list) == False:
        return -1
    if element == []:
        return -1    
    if len(element) == 1:
        return element[0]
    if type(element[0]) == str or type(element[-1]) == str:
        return -1

    if element[0] < element[-1]:
        return find_min(element[:-1])
    else:
        return find_min(element[1:])

element = [80,7,99, 5, 77,6]
print(find_min(element))


def sum_all(element):
    """TODO: complete for Step 2
    ~ check if there is only 1 element then return that 1 element
    ~ check if list is empty if true return -1
      if not empty then continue
    ~ check if the elements are a string then return -1
      if not continue
    ~ instance x is equal to element at position 0 plus
      element at position 1
    ~ new list is equal to x plus element at position 2 onwards
    ~ return the new element list"""
    if len(element) == 1:
        return element[0]
    if element == []:
        return -1  
    if type(element[0]) == str or type(element[1]) == str:
        return -1

    x = element[0] + element[1]
    new_element = [x] + element[2:]
    return sum_all(new_element)

element = [1,2,3,4,5]
print (sum_all(element))


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3
    ~ initialise an empty string to store the end result
    ~ n is decamenting 
    ~ if the instance in the character set is not a string(False)
      return an empty string else continue
    ~ if the lungth of the character set is 0 then return the 
      character set
    ~ if n i less than 0 simply return the character set
    ~ for every instance that is in the possible combinations
      is appended(added) to the empty string storage
    ~ return storage"""
    storage = []
    n -= 1
    for a in character_set:
        if isinstance(a, str) == False:
            return []
    if len(character_set) == 0:
        return character_set
    if n <= 0:
        return character_set
    for i in character_set:
        for find in find_possible_strings(character_set, n):
            storage.append(i + find)
    return storage
        
list1 = ['a', 'b']
print(find_possible_strings(list1, 1))