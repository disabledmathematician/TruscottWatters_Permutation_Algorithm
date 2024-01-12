
# Charles Thomas Wallace Truscott 

def print_state(Rubiks):
	print("Front Face: {}\n Right Face: {}\n Left Face: {}\n Back Face: {}\n Upper Face: {}\n Down Face: {}\n".format(Rubiks[0], Rubiks[1], Rubiks[3], Rubiks[2], Rubiks[4], Rubiks[5]))

def FRU_1_1(Rubiks: list):
	SaveStateUF = Rubiks[4][0][0], Rubiks[4][1][0]
	SaveStateLF = Rubiks[3][0][0], Rubiks[3][1][0]
	SaveStateDF = Rubiks[5][0][0], Rubiks[5][1][0]
	SaveStateBF = Rubiks[2][0][1], Rubiks[2][1][1]
	SaveStateFF = Rubiks[0][0][0], Rubiks[0][1][0]
	Rubiks[0][0][0], Rubiks[0][1][0] = SaveStateUF[1], SaveStateUF[0]
	Rubiks[2][0][1], Rubiks[2][1][1] = SaveStateDF[1], SaveStateDF[0]
	Rubiks[5][0][0], Rubiks[5][1][0] = SaveStateFF[0], SaveStateFF[1]
	Rubiks[4][0][0], Rubiks[4][1][0] = SaveStateBF[1], SaveStateBF[0]
	SaveStateLF1 = Rubiks[3][0][1], Rubiks[3][1][1]
	SaveStateLF2 = Rubiks[3][0][0], Rubiks[3][1][0]
	Rubiks[3][0][0] = SaveStateLF2[1]
	Rubiks[3][0][1] = SaveStateLF2[0]
	Rubiks[3][1][0] = SaveStateLF1[1]
	Rubiks[3][1][1] = SaveStateLF1[0]
	return Rubiks
def FRU_1_2(Rubiks: list):
	for x in range(2):
		FRU_1_1(Rubiks)
def FRU_1_3(Rubiks: list):
	for x in range(3):
		FRU_1_1(Rubiks)
def FRU_2_1(Rubiks: list):
	SaveStateUF = Rubiks[4][0][1], Rubiks[4][1][1]
	SaveStateRF = Rubiks[1][0][0], Rubiks[1][1][0]
	SaveStateDF = Rubiks[5][0][1], Rubiks[5][1][1]
	SaveStateBF = Rubiks[2][0][0], Rubiks[2][1][0]
	SaveStateFF = Rubiks[0][0][1], Rubiks[0][1][1]
	Rubiks[0][0][1], Rubiks[0][1][1] = SaveStateUF[0], SaveStateUF[1]
	Rubiks[2][0][0], Rubiks[2][1][0] = SaveStateDF[0], SaveStateDF[1]
	Rubiks[5][0][1], Rubiks[5][1][1] = SaveStateFF[0], SaveStateFF[1]
	Rubiks[4][0][1], Rubiks[4][1][1] = SaveStateBF[1], SaveStateBF[0]
	SaveStateRF1 = Rubiks[1][0][0], Rubiks[1][0][1]
	SaveStateRF2 = Rubiks[1][1][0], Rubiks[1][1][1]
	Rubiks[1][0][0] = SaveStateRF1[1]
	Rubiks[1][0][1] = SaveStateRF2[1]
	Rubiks[1][1][0] = SaveStateRF1[0]
	Rubiks[1][1][1] = SaveStateRF2[0]
	return Rubiks
def FRU_2_2(Rubiks: list):
	for x in range(2):
		FRU_2_1(Rubiks)
def FRU_2_3(Rubiks: list):
	for x in range(3):
		FRU_2_1(Rubiks)
def WL_1_1(Rubiks: list):
	pass
def WL_1_2(Rubiks: list):
	pass
def WL_1_3(Rubiks: list):
	pass
def WL_2_1(Rubiks: list):
	pass
def WL_2_2(Rubiks: list):
	pass
def WL_2_3(Rubiks: list):
	pass
def HL_1_1(Rubiks: list) -> list:
	SingleStateUF = (Rubiks[4][0][0], Rubiks[4][0][1])
	SingleStateLF = (Rubiks[3][0][0], Rubiks[3][1][0])
	SingleStateRF = (Rubiks[1][0][1], Rubiks[1][1][1])
	Rubiks[3][0][0], Rubiks[3][1][0] = Rubiks[5][0][0], Rubiks[5][0][1]
	Rubiks[1][0][1], Rubiks[1][1][1] = Rubiks[4][0][0], Rubiks[4][0][1]
	Rubiks[5][0][0], Rubiks[5][0][1] = SingleStateRF[0], SingleStateRF[1]
	Rubiks[4][0][0], Rubiks[4][0][1] = SingleStateLF[0], SingleStateLF[1]
	SavedStateBF0 = (Rubiks[2][0][1], Rubiks[2][1][1])
	SavedStateBF1 = Rubiks[2][0][0], Rubiks[2][1][0]
	Rubiks[2][0][0], Rubiks[2][0][1] = SavedStateBF0[0], SavedStateBF0[1]
	Rubiks[2][1][0], Rubiks[2][1][1] = SavedStateBF1[0], SavedStateBF1[1]
	return Rubiks
def HL_1_2(Rubiks: list):
	for x in range(2):
		HL_1_1(Rubiks)
	return Rubiks
def HL_1_3(Rubiks: list):
	for x in range(3):
		HL_1_1(Rubiks)
	return Rubiks
def HL_2_1(Rubiks: list) -> list:
	SingleStateUF = (Rubiks[4][1][0], Rubiks[4][1][1])
	SingleStateLF = (Rubiks[3][0][1], Rubiks[3][1][1])
	Rubiks[3][0][1] = Rubiks[5][1][0]; Rubiks[3][1][1] = Rubiks[5][1][1]
	Rubiks[4][1][0] = SingleStateLF[0]; Rubiks[4][1][1] = SingleStateLF[1]
	Rubiks[0][0][0], Rubiks[0][0][1],Rubiks[0][1][0], Rubiks[0][1][1] = Rubiks[0][1][0], Rubiks[0][0][0], Rubiks[0][1][1], Rubiks[0][0][1]
	Rubiks[5][1][0], Rubiks[5][1][1] = Rubiks[1][0][0], Rubiks[1][1][0]
	Rubiks[1][0][0] = SingleStateUF[0]
	Rubiks[1][1][0] = SingleStateUF[1]
	return Rubiks
def HL_2_2(Rubiks: list):
	for x in range(2):
		HL_2_1(Rubiks)
	return Rubiks
def HL_2_3(Rubiks: list):
	for x in range(3):
		HL_2_1(Rubiks)
	return Rubiks
def CharlesTruscott():
	FF = [["G", "G"], ["G", "G"]]
	BF = [["B", "B"], ["B", "B"]]
	LF = [["O", "O"], ["O", "O"]]
	RF = [["R", "R"], ["R", "R"]]
	UF = [["W", "W"], ["W", "W"]]
	DF = [["Y", "Y"], ["Y", "Y"]]
	RubiksCube = [FF, RF, BF, LF, UF, DF]
	print_state(RubiksCube)
#	print("Rotate left closest facing side upward once")
#	HL_2_1(RubiksCube)
#	print_state(RubiksCube)
#	print("Then three more times for its original state")
#	HL_2_3(RubiksCube)
#	print_state(RubiksCube)
#	print("Turn the left closest side upward twice and the left furthest side upward twice")
#	HL_2_2(RubiksCube)
#	HL_1_2(RubiksCube)
#	print_state(RubiksCube)
#	print("Then turn the left closest side once")
#	HL_2_1(RubiksCube)
#	print_state(RubiksCube)
#	print("Then turn the left furthest side once")
#	HL_1_1(RubiksCube)
#	print_state(RubiksCube)
	answer = ""
	while answer != str("quit"):
		print("Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1")
		answer = str(input())
		if answer == str("LFFU1"):
			HL_1_1(RubiksCube)
		elif answer == str("LFFU2"):
			HL_1_2(RubiksCube)
		elif answer == str("LFFU3"):
			HL_1_3(RubiksCube)
		elif answer == str("LFCU1"):
			HL_2_1(RubiksCube)
		elif answer == str("LFCU2"):
			HL_2_2(RubiksCube)
		elif answer == str("LFCU3"):
			HL_2_3(RubiksCube)
		elif answer == str("FRLU1"):
			FRU_1_1(RubiksCube)
		elif answer == str("FRLU2"):
			FRU_1_2(RubiksCube)
		elif answer == str("FRLU3"):
			FRU_1_3(RubiksCube)
		elif answer == str("FRRU1"):
			FRU_2_1(RubiksCube)
		print_state(RubiksCube)
CharlesTruscott()


""" Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['W', 'W']]
 Down Face: [['Y', 'Y'], ['Y', 'Y']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRRU 1
Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['W', 'W']]
 Down Face: [['Y', 'Y'], ['Y', 'Y']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRRU1
Front Face: [['G', 'W'], ['G', 'W']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['Y', 'B'], ['Y', 'B']]
 Upper Face: [['W', 'B'], ['W', 'B']]
 Down Face: [['Y', 'G'], ['Y', 'G']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
Frlu1
Front Face: [['G', 'W'], ['G', 'W']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['Y', 'B'], ['Y', 'B']]
 Upper Face: [['W', 'B'], ['W', 'B']]
 Down Face: [['Y', 'G'], ['Y', 'G']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRLU1
Front Face: [['W', 'W'], ['W', 'W']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['Y', 'Y'], ['Y', 'Y']]
 Upper Face: [['B', 'B'], ['B', 'B']]
 Down Face: [['G', 'G'], ['G', 'G']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
LFCU1
Front Face: [['W', 'W'], ['W', 'W']]
 Right Face: [['B', 'R'], ['B', 'R']]
 Left Face: [['O', 'G'], ['O', 'G']]
 Back Face: [['Y', 'Y'], ['Y', 'Y']]
 Upper Face: [['B', 'B'], ['O', 'O']]
 Down Face: [['G', 'G'], ['R', 'R']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRRU1
Front Face: [['W', 'B'], ['W', 'O']]
 Right Face: [['R', 'R'], ['B', 'B']]
 Left Face: [['O', 'G'], ['O', 'G']]
 Back Face: [['G', 'Y'], ['R', 'Y']]
 Upper Face: [['B', 'Y'], ['O', 'Y']]
 Down Face: [['G', 'W'], ['R', 'W']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1

Front Face: [['G', 'G'], ['G', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'B'], ['B', 'B']]
 Upper Face: [['W', 'W'], ['W', 'W']]
 Down Face: [['Y', 'Y'], ['Y', 'Y']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRLU1
Front Face: [['W', 'G'], ['W', 'G']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['B', 'Y'], ['B', 'Y']]
 Upper Face: [['B', 'W'], ['B', 'W']]
 Down Face: [['G', 'Y'], ['G', 'Y']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRRU1
Front Face: [['W', 'W'], ['W', 'W']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['Y', 'Y'], ['Y', 'Y']]
 Upper Face: [['B', 'B'], ['B', 'B']]
 Down Face: [['G', 'G'], ['G', 'G']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRRU3
Front Face: [['W', 'W'], ['W', 'W']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['Y', 'Y'], ['Y', 'Y']]
 Upper Face: [['B', 'B'], ['B', 'B']]
 Down Face: [['G', 'G'], ['G', 'G']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRLU3
Front Face: [['G', 'W'], ['G', 'W']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['Y', 'B'], ['Y', 'B']]
 Upper Face: [['W', 'B'], ['W', 'B']]
 Down Face: [['Y', 'G'], ['Y', 'G']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
FRLU1
Front Face: [['W', 'W'], ['W', 'W']]
 Right Face: [['R', 'R'], ['R', 'R']]
 Left Face: [['O', 'O'], ['O', 'O']]
 Back Face: [['Y', 'Y'], ['Y', 'Y']]
 Upper Face: [['B', 'B'], ['B', 'B']]
 Down Face: [['G', 'G'], ['G', 'G']]

Enter LFFU or LFCU for left face furthest left face closest upward followed by the amount of rotations, i.e. LFFU1, LFCU3 (to rotate the first supported moves of the cube) FRLU1 FRRU1
"""

# Thank you Eric Grimson, John Guttag, Ana Bell and MITx and MIT OCW
