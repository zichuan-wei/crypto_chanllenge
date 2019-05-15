import cha1

#the source text is encoded by XOR a repeating single character
#as such, there is only 2556 possibilities, and we can just
#output them all and find the suitable one

#s is the input string, and c is the character we decode against
def decode(s , c):
	a = cha1.hex_string_to_bytes(s)
	b = bytearray(a)
	for i in range(len(a)):
		b[i] = a[i] ^ c
	return b
		
if "__main__":
	pass
