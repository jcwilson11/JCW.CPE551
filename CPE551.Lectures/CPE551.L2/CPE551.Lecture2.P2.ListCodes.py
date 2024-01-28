# Filter out odd items from a list by column
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# List comprehension
[row[1] for row in M if row[1] % 2 == 0]

# Collect a diagonal from matrix
diag = [M[i][i] for i in [0, 1, 2]]

# List comprehension and map
[int(c) * 2 for c in str(345) + 'a' if c.isdigit()]

S = "Stevens" #0123456
S1 = S[2:6] + S[:-4] + S[-3:0]
S1 