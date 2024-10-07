import re

class Regex:

    # * Function to verify Master Username
    # * Parameters: Master USer Name
    # * Return Value: Boolean
    @classmethod
    def verifyMasterUserName(cls, master_user_name: str) -> bool:
        pattern = '^[A-Za-z0-9._]+$'
        return bool(re.match(pattern, master_user_name))
    
    # * Function to verify Master Password
    # * Parameters: Master Password
    # * Return Value: Boolean
    @classmethod
    def verifyPassword(cls, master_password: str) -> bool:
        s = master_password
        if  len(s) < 8 or len(s) > 35:
            print(1)
            return False
        if not re.search(r'[a-z]', s):
            print(2)
            return False

        if not re.search(r'[A-Z]', s):
            print(3)
            return False

        if not re.search(r'\d', s):
            print(4)
            return False

        if not re.search(r'[@$!%*?&#]', s):
            print(5)
            return False

        return True

