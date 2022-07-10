#remove blanks
string_1 =  " Pl ayTha tF u nkyM usi c "

def remove_blanks(str):
    remove = ' '
    for i in remove:
        str = str.replace(i, "")
    print(str)

remove_blanks(string_1)


# get digits
digits_1 = "0s1a3y5w7h9a2t4?6!8?0"

def get_digits(str):
    digits_arr = []
    new_arr = list(str)

    i = 0
    while (i < len (new_arr) - 1):
        if new_arr[i] not in digits:
            for j in range(i, len(new_arr) - 1):
                temp = new_arr[j]
                new_arr[j]=new_arr[j+1]
                new_arr[j+1] = temp
            new_arr.pop()
        i+=1

    return_str=''
    for char in new_arr:
        return_str += char
    return return_str

get_digits(digits_1)


#acronyms
def acronyms(str):
    str_arr=str.split(' ')
    return_arr=[]
    for word in str_arr:
        if word != ' ':
            return_arr.append(word[0])
    return_str=''
    for char in return_arr:
        return_str+=char.upper()
    return return_str

#zip arrays

def zip(arr1, arr2):
    dict = {}
    for i in range(len(arr1)):
        dict[str(arr1[i])] = arr2[i]
    return dict

#invert hash

def invert_hash (dict):
    new_dict = {}
    for keyy,value in dict.items():
        new_dict[value] = key
    return new_dict
