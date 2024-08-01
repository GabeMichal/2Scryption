board1 = [0, 1, 2, 3]
board2 = [4, 5, 6, 7]

for k in range(4):
    if k == 0:
        po3 = board1[0]
    if k == 3:
        board1[3] = board2[0]
    else:
        board1[k] = board1[k + 1]
for k in range(4):
    if k == 3:
        board2[3] = po3
    else:
        board2[k] = board2[k + 1]

print(board1)
print(board2)