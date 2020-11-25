"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

import re


class Solution:
    def defangIPaddrRegex(self, address: str) -> str:
        pattern = '\.'
        res = re.sub(pattern, '[.]', address)
        return res

    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
        # return address.replace('.', '[.]')


print(Solution().defangIPaddr('1.1.1.1'))
