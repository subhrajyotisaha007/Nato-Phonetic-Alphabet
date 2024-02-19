# l = [3,4,5,6,7,8,9]
# m = [3,21,5,7,10,29,90]
# n = []
# for i in l:
#     for j in m:
#         if i == j:
#             n.append(i)
#
# # print(n)
# import random
#
# names = ['subhra','aparna','souvik','arka','sk']
# a =[]
# for each in names:
#     a.append(random.randint(101))
#
# print(a)


# sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
# l = 'saha'
# word_list = sentence.split()
# print(word_list)
#
# a = []
# for i in word_list:
#     a.append(len(i))
# print(a)
# names = {'subhra':10,'ARKA':5,'aparna':20,'sk':60}
# for (key,value) in names.items():
#     print(key)


import pandas
new = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(new.to_dict())
# print(new)

# for (index,row) in new.iterrows():
new_dict = {row.letter:row.code for (index,row) in new.iterrows()}
# print(new_dict)

# user_name_code =[]
user_name = input('what\'s your name?').upper()
# for j in user_name:
#     user_name_code.append(new_dict[j])

user_name_code = [new_dict[item] for item in user_name]
print(user_name_code)

