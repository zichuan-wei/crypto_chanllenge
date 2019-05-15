import cha1
import sys

#the source text is encoded by XOR a repeating single character
#as such, there is only 256 possibilities, and we can just
#output them all and find the suitable one

#s is the input string, and c is the character we decode against
def decode(s , c):
	a = cha1.hex_string_to_bytes(s)
	b = bytearray(a)
	for i in range(len(a)):
		b[i] = a[i] ^c 
	return b
		
if "__main__":
	s = sys.argv[1]
	for c in range(256):
		print(str(decode(s, c)))

#the answer is "b"ooking MC\'s like a pound of bacon""
