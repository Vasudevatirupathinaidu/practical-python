# Strings

# Representing literal text
# Single quote
a = 'Yeah but no butyeah but...'
print(a)

# Double quote
b = 'computer says no'
print(b)

# Triple quotes
c = '''
Look into my eyes, look into my eyes, the eyes,the eyes, the eyes,
not around the eyes,
don't look around the eyes,
look into my eyes, you're under.
'''
print()


# String escape codes
'''
'\n'      Line feed
'\r'      Carriage return
'\t'      Tab
'\''      Literal single quote
'\"'      Literal double quote
'\\'      Literal backslash
'''

# String Representation
'''Each character in a string is stored internally as a so-called Unicode “code-point” which is an integer. You can specify an exact code-point value using the following escape sequences'''
a = '\xf1'
print(a)
b = '\u2200'
print(b)
c = '\U0001D122'
print(c)
d = '\N{FOR ALL}'
print(d)
print()


# String indexing
a = 'Hello world'
print(a[0])
print(a[4])
print(a[-1])
print(a[:5])
print(a[6:])
print(a[3:8])
print(a[-5:])
print()


# String operations
'''Concatenation, length, membership and replication'''
print('Hello ' + 'World')
print(len('Hello'))
print('l' in 'Hello')
print('h' not in 'Hello')
print('Yes' * 5)
print()


# String methods
'''stripping, case conversion, replacing text'''
print(' hello '.strip())
print(' hello'.lstrip())
print('hello '.rstrip())
print('Tenet'.lower())
print('tenet'.upper())
print('tenet'.title())
print('Hello Nolan'.replace('Hello', 'Hola'))
print()

'''More string methods:

s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Joins lists using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()              # Convert to upper case
'''