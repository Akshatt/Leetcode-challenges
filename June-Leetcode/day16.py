'''
Validate IP Address

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.
'''
class Solution:
    def validIPAddress(self, IP: str) -> str:
        IP4 = 'IPv4'
        IP6 = 'IPv6'
        Neither = 'Neither'
        if '.' in IP and ':' in IP:
        	return Neither
        elif '.' in IP:
        	Count = IP.split('.')
        	if len(Count) != 4:
        		return Neither
        	for i in Count:
        		if i.isdigit() == False or len(i) == 0 or int(i) > 255 or int(i) < 0 or (len(i) != 1 and i[0] == '0'):
        			return Neither
        	return IP4
        else:
        	Count = IP.split(':')
        	if len(Count) != 8:
        		return Neither
        	for i in Count:
        		if len(i) > 4 or len(i) == 0 or i.isalnum() == False:
        			return Neither
        		for j in i:
        			if j <= '9' and j >= '0':
        				continue
        			if (j > 'f' and j <= 'z') or (j > 'F' and j <= 'Z'):
        				return Neither
        	return IP6


#Runtime: 32 ms
#Memory Usage: 13.8 MB