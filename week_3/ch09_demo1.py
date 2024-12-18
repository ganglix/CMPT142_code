# print the names of chessboard tiles.    # mention print new line
# row: 1-8, col: a-h
"""
a8 b8 c8 d8 e8 f8 g8 h8
a7 b7 c7 d7 e7 f7 g7 h7
a6 b6 c6 d6 e6 f6 g6 h6
a5 b5 c5 d5 e5 f5 g5 h5
a4 b4 c4 d4 e4 f4 g4 h4
a3 b3 c3 d3 e3 f3 g3 h3
a2 b2 c2 d2 e2 f2 g2 h2
a1 b1 c1 d1 e1 f1 g1 h1
"""

# just do the first row
row = 8
for col in 'abcdefgh':
    print(f"{col}{row}", end=' ')  # by default print() will print a new line, end = '\n'

# do the second row
print()  # print a newline
row = 7
for col in 'abcdefgh':
    print(f"{col}{row}", end=' ')  # by default print() will print a new line, end = '\n'

# do all the rows
print()
print('-'*40)

for row in range(8,0,-1):  # 8 7...1
    for col in 'abcdefgh':
        print(f"{col}{row}", end=' ')  # by default print() will print a new line, end = '\n'
    # after printing cols in each row
    # move to the next row
    print()  # print a newline
