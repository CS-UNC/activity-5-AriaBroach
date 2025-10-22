words_file = open('CROSSWD.txt','r')

# print(type(words_file))
# words = []
# for line in words_file:
#     print(line.strip())

#print([x for x in dir(words_file) if '_' != x[0]])

# data= [1,3,2,8,5,6,10]

# print([2*x for x in data if x % 2 == 0])


def more_than_20(file):
    words = []
    data= open(file,'r')
    # for word in data:
    #     if len(word.strip()) > 20:
    #         words.append(word.strip)
    # return words
    words=[x.strip() for x in data if len(x.strip()) > 20]
    return words

print(more_than_20("CROSSWD.txt"))


def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

print(has_no_e('fire'))


def uses_only(word,letters):
    for x in word:
        if x not in letters:
            return False
    return True
   
print(uses_only('abracadabra','abr'))


def all_uses_only(file,letters):
    result = []
    with open(file,'r') as file:
        for line in file:
            words= line.split()
            for word in words:
                if uses_only(word,letters):
                    result.append(word)
    
    return result

print(all_uses_only('CROSSWD.txt','arc'))


# grades= []
# Names = ['Alex','Max','Carey']
# grades.append([10,9,8,7])
# grades.append([9,9,8,8])
# grades.append([10,10,10,2])

# #print(grades)
# x = Names.index('Carey')
# print(grades[x][3])

# grades = {}
# grades['Max'] = {'A1':10,'A2': 9,'A3': 8,'A4': 7}
# grades['Alex'] = [9,9,8,8]
# grades['Carey'] = [10,10,10,2]

# print(grades.keys())
# for student in grades.keys():
#     print(student, grades[student])

# print(grades['Max']['A2'])

# statement = "This is not cool"
# data = [12,13,14,15,16]
# print(statement)
# print(data)
# print('--------------------')

# data.append(35)
# print(data)
# statement= statement + ' modified'
# print(statement)

# statement2=statement.upper()
# print(statement2)
# print(statement is statement2)
