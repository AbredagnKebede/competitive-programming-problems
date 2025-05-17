import re
class Solution:
    def maskPII(self, s: str) -> str:
        def maskmail(email):
            n = email.split('@')
            local = n[0].lower()
            domain = n[1].lower()
            return local[0] + '*****' + local[-1] + '@' + domain

        def maskphone(phone):
            num = re.sub(r"\D", "", phone)  # Remove all non-numeric characters
            if len(num) == 10:
                return "***-***-" + num[-4:]
            elif len(num) == 11:
                return "+*-***-***-" + num[-4:]
            elif len(num) == 12:
                return "+**-***-***-" + num[-4:]
            elif len(num) == 13:
                return "+***-***-***-" + num[-4:]
        
        if "@" in s:
            return maskmail(s)
        else:
            return maskphone(s)
