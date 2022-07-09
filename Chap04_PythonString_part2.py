# 1
import string

print('#1')
format_string1 = "I'm {}."
print('format_string1 : ', format_string1)
name = 'Huynh'
print(format_string1.format('Bao'))
print(format_string1.format(name))
print('-'*10)
format_string2 = 'Hi {}, Are you {} or {} ?'
print('format_string2 : ', format_string2)
name = 'Bao'
adj1 = 'happy'
adj2 = 'sad'
print(format_string2.format(name, adj1, adj2))
print('-'*10)
format_string3 = '{name} has lived in {city} for {number} year(s).'
print('format_string3 : ', format_string3)
print(format_string3.format(name='Bean', city='DaNang', number=3))
# 2
print('#2')
print('|{:25}|'.format('25 characters width'))
print('|{:<25}|'.format('Hello World!'))  # '<' Indicates left alignment (the default)
print('|{:>25}|'.format('Hello World!'))  # '>' Indicates right alignment
print('|{:^25}|'.format('Hello World!'))  # '^' Indicates centered
print('{:,}'.format(1234567890.123))  # Can format numbers with comma as thousands separator
# 3
print('#3')
template = string.Template('$name has lived in $city for $number year(s).')
print(template.substitute(name='Bean', city='HaNoi', number=4))
d = dict(name='Bao', city='NgheAn', number=3)
print(template.substitute(d))
print('-'*10)
# Exercises of PythonString
# We are going to try out some of the string related operations.
# 1. Explore replacing a string
#   Create a string with words separated by ',' and replace the commas with spaces;
#   for example replace all the commas in 'Denyse,Marie,Smith,21,London,UK'
#   with spaces. Now print out the resulting string.
# 2. Handle user input
#   The aim of this exercise is to write a program to ask the user for two strings and
#   concatenate them together, with a space between them and store them into a new
#   variable called new_string.
# Next:
# • Print out the value of new_string.
# • Print out how long the contents of new_string is.
# • Now convert the contents of new_string to all upper case.
# • Now check to see if new_string contains the string 'Albus' as a substring.
print('# Exercises of PythonString')
ex_string = 'Denyse,Marie,Smith,21,London,UK'
print('1/ Explore replacing a string \nex_string :', ex_string)
print('-> After replace all the commas with spaces :', ex_string.replace(',', ' '))  # Chap4_PythonString_part1 #10
print('2/ Handle user input')
ip1_string = str(input('Input first string: '))
ip2_string = str(input('Input second string: '))
new_string = ip1_string + ' ' + ip2_string
print('-> Print out the value of new_string :', new_string)  # Chap4_PythonString_part1 #4
print('-> Print out how long the contents of new_string is:', len(new_string))  # Chap4_PythonString_part1 #5
print('-> Convert the contents of new_string to all upper case:', new_string.upper())  # Chap4_PythonString_part1 #13
print("-> Check if new_string contains 'Albus':", new_string.find('Albus'))  # Chap4_PythonString_part1 #11


