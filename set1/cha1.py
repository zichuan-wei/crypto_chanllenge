import sys
import math
import base64

#given a string reperests a hex number, return a bytearray
def hex_string_to_bytes(s):
	#length of the string has to be divisble by 2, since 2 charater represents one byte
	b = bytearray(math.ceil(len(s)/2))
	i1 = 0
	i2 = 0
	while i1 < len(s):
		v = 0
		if s[i1] >= '0' and s[i1] <= '9':
			v = v + ord(s[i1]) - ord('0')
		elif s[i1] >= 'a' and s[i1] <= 'f':
			v = v + ord(s[i1]) - ord('a') + 10
		elif s[i1] >= 'A' and s[i1] <= 'F':
			v = v + ord(s[i1]) - ord('A') + 10
		v = v * 16
		if s[i1+1] >= '0' and s[i1+1] <= '9':
			v = v + ord(s[i1+1]) - ord('0')
		elif s[i1+1] >= 'a' and s[i1+1] <= 'f':
			v = v + ord(s[i1+1]) - ord('a') + 10
		elif s[i1] >= 'A' and s[i1] <= 'F':
			v = v + ord(s[i1]) - ord('A') + 10
		b[i2] = v
		i1 = i1 + 2
		i2 = i2 + 1
	return b

#given 2 equal length hex string, return their XOR
def fixedXOR(s1, s2):
	b1 = hex_string_to_bytes(s1)
	b2 = hex_string_to_bytes(s2)
	b3 = bytearray(b2)
	for i in range(len(b2)):
		b3[i] = b1[i] ^ b2[i]
	return b3

if "__main__":
	s1 = sys.argv[1]
	s2 = sys.argv[2]
	b = fixedXOR(s1,s2)
	print(base64.b64encode(b))
	print(base64.b16encode(b))
	print(int.from_bytes(b, byteorder='big'))
