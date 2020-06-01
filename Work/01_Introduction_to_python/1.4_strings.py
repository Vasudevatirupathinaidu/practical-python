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
