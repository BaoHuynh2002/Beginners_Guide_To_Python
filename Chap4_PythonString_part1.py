# 1
print('#1')
string = ''
print('Print empty string: ', string)
# 2
print('#2')
string_a = 'single quotes can be used to define a string'
string_b = "double quotes can be used to define a string"
print(string_a)
print(string_b)
string_c = 'Using single quotes to show "double quotes" in a string'
string_d = "Using double quotes to show 'single quotes' in a string"
print(string_c)
print(string_d)
# 3
print('#3')
val_a = 'Bao'
print('Type of val_a:', type(val_a))
# 4
print('#4')
str_1 = 'Hello'
str_2 = "World"
str_3 = str_1 + str_2
print('Str_1 : ', str_1)
print('Str_2 : ', str_2)
print('Str_3 : ', str_3)
print('Str_1 + Str_2 : ', str_1 + str_2)
print('"Hello" + "World" = ', "Hello" + "World")
# 5
print('#5')
string_1 = 'Good Job'
print('String_1 : ', string_1)
print('Length of string_1 = ', len(string_1))
# 6
print('#6')
my_string = 'Hello World'
print('my_string =', my_string)
print('my_string[0] =', my_string[0])  # characters at position 0
print('my_string[1:4] =', my_string[1:4])  # from position 1 to 5
print('my_string[:5] =', my_string[:5])  # from start to position 5
print('my_string[2:] =', my_string[2:])  # from position 2 to the end
print('my_string[-1] =', my_string[-1])  # last characters
print('my_string[-5:] =', my_string[-5:])
print('my_string[-8:-4] =', my_string[-8:-4])
# 7
print('#7')
string_1 = 'Hi'*10
print('Repeated "Hi" 10 times: ', string_1)
# 8
print('#8')
source_string = 'The Good, The Bad, The Beautiful, The Ugly'
print('Source string:', source_string)
print('Split using a space')
print(source_string.split(' '))
print('Split using a comma')
print(source_string.split(','))
# 9
print('#9')
my_string = 'This sentence, is  not      normal.'
print('my_string:', my_string)
print("my_string.count(' ') #count_space:", my_string.count(' '))
print("my_string.count(',') #count_comma:", my_string.count(','))
print("my_string.count('n') #count_'n':", my_string.count('n'))
# 10
print('#10')
message = 'Nice guy!'
print('message : ', message)
print('message.replace("Nice", "Bad") =', message.replace("Nice", "Bad"))
# 11
print('#11')
string = 'Python is not hard'
print('string : ', string)
print("string.find('Java') = ", string.find('Java'))
print("string.find('Python') = ", string.find('Python'))
print("string.find('not') = ", string.find('not'))
print("string[string.find('not'):] = ", string[string.find('not'):])
# 12
print('#12')
msg = 'Eleven is ' + str(11)
print(msg, ', #use str() to convert int to string')
print("'Bao' == 'Ben' : ", 'Bao' == 'Ben')  # '==' : so sanh bang
print("'Bao' == 'Bao' : ", 'Bao' == 'Bao')
print("'Bao' != 'bao' : ", 'Bao' != 'bao')  # '!=' : so sanh khac
# 13
some_string = 'Hello World'
print('#13')
print('some_string :', some_string)
print('-' * 20)
print("some_string.startswith('H') =", some_string.startswith('H'))
print("some_string.startswith('h') =", some_string.startswith('h'))
print("some_string.endswith('d') =", some_string.endswith('d'))
print('some_string.istitle() =', some_string.istitle())  # Check if each word start with an upper case letter
print('some_string.isupper() =', some_string.isupper())  # Check if all the characters in the text are in upper case
print('some_string.islower() =', some_string.islower())  # Check if all the characters in the text are in lower case
print('some_string.isalpha() =', some_string.isalpha())  # Check the string consists of alphabetic characters only
print('-' * 20)
print('some_string.upper() =', some_string.upper())
print('some_string.lower() =', some_string.lower())
print('some_string.title() =', some_string.title())
print('some_string.swapcase() =', some_string.swapcase())
print('"   xyz   ".strip() = ', " xyz ".strip())
