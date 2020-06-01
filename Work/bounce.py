# bounce.py
'''A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.

Your program should make a table that looks something like this:

1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998
'''

# Exercise 1.5
height = 100
bounce_backup = 3/5

height_var = 100 * (3/5)

for i in range(1, 11):
    print(f'{i} {round(height_var,4)}')
    height_var = height_var * (3/5)