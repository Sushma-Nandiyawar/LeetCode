class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        a, b = a[::-1], b[::-1]
        carry = 0
        for i in range(max(len(a), len(b))):
            da = ord(a[i]) - ord("0") if i<len(a) else 0
            db = ord(b[i]) - ord("0") if i<len(b) else 0
            total = da+ db+ carry
            char = str(total%2)
            result = char + result
            carry = total // 2
        if carry:
            result = "1"+result
        return result





