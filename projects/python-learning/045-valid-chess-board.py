valid_pieces = ["wking", "bking", "wqueen", "bqueen", "wbishop", "bbishop",
				"wknight", "bknight", "wrook", "brook", "wpawn", "bpawn"]
valid_positions = []
for x in range(1, 9):
	valid_positions.append(str(x) + "a")
for x in range(1, 9):
	valid_positions.append(str(x) + "b")
for x in range(1, 9):
	valid_positions.append(str(x) + "c")
for x in range(1, 9):
	valid_positions.append(str(x) + "d")
for x in range(1, 9):
	valid_positions.append(str(x) + "e")
for x in range(1, 9):
	valid_positions.append(str(x) + "f")
for x in range(1, 9):
	valid_positions.append(str(x) + "g")
for x in range(1, 9):
	valid_positions.append(str(x) + "h")

#compressed: valid_positions = [str(x) + y for x in range(1, 9) for y in "abcdefgh"]

def is_valid_chess_board(board):
	white_count = 0
	black_count = 0
	wpawn = 0
	bpawn = 0
	for k, v in board.items():
		if k not in valid_pieces:
			return False
		elif v not in valid_positions:
			return False
	for piece in board:
		if piece.startswith("w"):
			white_count += 1
		else:
			black_count += 1
	if white_count > 16 or black_count > 16:
		return False
	for piece in board:
		if piece == "wpawn":
			wpawn += 1
		elif piece == "bpawn":
			bpawn += 1
	if wpawn > 8 or bpawn > 8:
		return False
	return True

board1 = {"wqueen": "8b", "bking": "2b", "wrook": "5c"}
board2 = {
	"wqueen": "8b",
	"bking": "2b",
	"wrook": "5c"
}
board3 = {
	"wking": "8z",
	"bking": "2b"
}

print(is_valid_chess_board(board1))
print(is_valid_chess_board(board2))
print(is_valid_chess_board(board3))