import pandas
new = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(new)

# for (index,row) in new.iterrows():
new_dict = {row.letter:row.code for (index,row) in new.iterrows()}
# print(new_dict)

user_name = input('what\'s your name?').upper()
user_name_code = [new_dict[item] for item in user_name]
print(user_name_code)

