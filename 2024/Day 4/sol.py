from sys import stdin
import re

def countXMAS(s):
    return sum(s[i:].startswith("XMAS") for i in range(len(s)))

def rotate_matrix_90(matrix):
    rotated = ["".join(row[col] for row in reversed(matrix)) for col in range(len(matrix[0]))]
    return rotated

def extract_submatrix(matrix, start_row, start_col):
    submatrix = []
    for r in range(start_row, start_row + 3):
        if r < len(matrix):  
            submatrix.append(matrix[r][start_col:start_col + 3])
    return submatrix
    
def MASmatrix(m):
    if m[0][0] == m[2][0] == "M" and m[1][1] == "A" and m[0][2] == m[2][2] == "S":
        return 1
    return 0

def checkFull(m):
    s = 0
    for i in range(len(m)-2):
        for j in range(len(m[0])-2):
            tinyM = extract_submatrix(m, i, j)
            s += MASmatrix(tinyM)
            tinyM = rotate_matrix_90(tinyM)
            s += MASmatrix(tinyM)
            tinyM = rotate_matrix_90(tinyM)
            s += MASmatrix(tinyM)
            tinyM = rotate_matrix_90(tinyM)
            s += MASmatrix(tinyM)
    return s

sol1 = 0
sol2 = 0
lines = []
for line in stdin:
    lines.append(line.strip())
    sol1 += countXMAS(line.strip())
    sol1 += countXMAS(line.strip()[::-1])
for i in range(len(lines[0])):
    s = ""
    for j in range(len(lines)):
        s += lines[j][i]
    sol1 += countXMAS(s.strip())
    sol1 += countXMAS(s.strip()[::-1])
rows = len(lines)
cols = len(lines[0])

for start in range(rows + cols - 1):
    diag = ""
    for r in range(rows):
        c = start - r
        if 0 <= c < cols:
            diag += lines[r][c]
    sol1 += countXMAS(diag)
for i in range(len(lines)):
    lines[i] = lines[i][::-1]
for start in range(rows + cols - 1):
    diag = ""
    for r in range(rows):
        c = start - r
        if 0 <= c < cols:
            diag += lines[r][c]
    sol1 += countXMAS(diag)

lines = lines[::-1]
for start in range(rows + cols - 1):
    diag = ""
    for r in range(rows):
        c = start - r
        if 0 <= c < cols:
            diag += lines[r][c]
    sol1 += countXMAS(diag)
for i in range(len(lines)):
    lines[i] = lines[i][::-1]
for start in range(rows + cols - 1):
    diag = ""
    for r in range(rows):
        c = start - r
        if 0 <= c < cols:
            diag += lines[r][c]
    sol1 += countXMAS(diag)
sol2 = checkFull(lines)
print(sol1)
print(sol2)