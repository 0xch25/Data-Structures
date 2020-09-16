'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''


def defangIPaddr(address):
    x = address.split(".")
    x = str(("[.]".join(x)))
    return x
address = "1.1.1.1"
print(defangIPaddr(address))