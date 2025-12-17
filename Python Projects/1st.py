############### NOTES ###############
# CTRL + / to highlight all the comments in different lines then press (CTRL+/)
# Sourse Code: It is the code that you write in any programming language to make the program work.
# Translator: It is a program that converts the source code into machine code so that the computer can understand and execute it.
# Machine Code: It is the code that the computer understands and executes. It is in binary format (0s and 1s).
# Run Time: It is the period when the program is being executed (run) by the computer and the instructions are being followed.
# Compiler: It is a program that converts the entire source code into machine code before executing (run) it.
# Interpreter: It is a program that reads and executes (run) the source code line by line during the run time and converts it into machine code.

############### PRINT STATEMENT ###############
print("Hello from 1st Python file!"); print('I Love Programming') # This is a comment
print('HELLO') # This is will show in different lines



############### DATA TYPES ###############
print(type(10))  # Integer Int
print(type(-10))  # Integer Int
print(type(2.5)) # Float
print(type(-2.501)) # Float
print(type("Python")) # String str
print(type('Book')) # String str
print(type(True)); print(type(False)) # Boolean bool
print(type([1,2,3,4,5])) # Array list
print(type((1,2,3,4,5,6,7,8))) # Tuple
print(type({"One":1, "Two":2, 'Three':3})) # Dictionary Dict

print(3==3)

################### RESERVED WORDS ###################
help("keywords")  # To see all the reserved words in Python

################ VARIABLES #################
myVariable = "MyValue"  # Variable must start from (A-Z or a-z or _) ONLY
print(myVariable)
a, b, c = 10, 20, 30  # Multiple variable assignment in single line
print(a); print(b); print(c) # That will print in different lines
#or
print(a)
print(b)
print(c)
#or
print(a, b, c) # That will print in single line with space between them


First22_ = 'Mo' # You can include numbers or _ between variables. CAN NOT include any special characters like (!,@,#,$,%,^,&,*,(,),-,+,=,/,.,>,<, etc..).
print(First22_)


############## PYTHON ESCAPE CHARACTERS ##############
print("Hello \"Python\"")  # \ To ignore the character after it and to put it before the double quotes to include double quotes inside double quotes
print('It\'s a nice day')  # \ To ignore the character after it and to put it before the single quotes to include single quote inside single quotes
print("C:\MyFolder\MyFile")  # \ To include single backslash between the string
print("MyFile\\")  # \\ To include single backslash at the end of the string
print("Hello \
Python \
2025")  # \ To break the line of code into multiple lines to show in single line
print("Hello\nPython")  # \n New Line 
print("Hellokkk\rPython")  # \r Carriage Return. Any text printed after the (\r) will overwrite the existing characters on that same line before (\r), character by character. 
print("Hello\bPython")  # \b Backspace the character before it
print("Hello\fPython")  # \f Form Feed to break the line
print("Hello\tPython")  # \t Tab Space or Horizontal Tab
print("Hello\vPython2")  # \v Vertical Tab
print("Hello\aPython")  # \a Alert (Bell) to produce a sound
print("Hello\0Python88")  # \0 Null Character to ignore the character after it
############# Hex, decimal, and symbol values (https://www.ibm.com/docs/en/ste/11.0.0?topic=maps-hex-decimal-symbol-values) ##############
print("\x4D\x6F\x68")  # \x Hexadecimal Value to represent Unicode character to print my name letters.
print("Hello\u03A9Python")  # \u Greek Letter Omega to represent Unicode character
print("Hello\u00A9Python")  # \u Copyright Symbol to represent Unicode character  ssssssssssssssssss
print("Hello\xA9Python")  # \x Copyright Symbol
############## End of the File ##############


############## CONCATENATION ##############
firstName = "John"
lastName = "Doe"
fullName = firstName + " " + lastName  # Concatenation of strings. ("") to add space between first and last names
print(fullName)
color = 'red'
Skin = "tan"
print(color + "\n" + Skin)  # Concatenation of strings with new line
print(color + "\t" + Skin)  # Concatenation of strings with tab space


############## STRING METHODS ##############
myString = "Hello Python Programming Language"
print(myString.lower())  # To convert all characters to lowercase
print(myString.upper())  # To convert all characters to uppercase

myString1 = ("Python1 'Test' ") # You can use single quotes inside double quotes
myString2 = ('Python2 "Test"') # You can use double quotes inside single quotes
print(myString1)
print(myString2)

myString3 = ('''Python3
glass3
book3''') # You can use triple single quotes for multiple lines string to show in different lines
print(myString3)

myString4 = ("""Python4
glass4
book4""") # You can use triple double quotes for multiple lines string to show in different lines
print(myString4)

myString5 = ("""Python5
glass5 'Test' "Test"
book5""") # You can use triple double quotes for multiple lines string to show in different lines
print(myString5)
