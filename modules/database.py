import os
import sqlite3

from .exceptions import UserNotFoundError


class Database:

    app_data = os.getenv('LOCALAPPDATA')

    # * Function to Establish SQLite Connection
    # * No Parameters
    # * Return Value: Connection
    @classmethod
    def _sqliteConnection(cls):
        conn = sqlite3.connect(
            cls.app_data+r'/zAsh7/Password Manager/.database/database.db')
        return conn

    # * Function to Create userTable
    # * No Parameters
    # * No Return Value
    @classmethod
    def init(cls) -> None:
        os.makedirs(cls.app_data+r'/zAsh7'+r'/Password Manager'+r'/.database', exist_ok=True)

        conn = Database._sqliteConnection()
        c = conn.cursor()
        with open(r'./SQL/create-userTable.sql', 'r') as f:
            query = f.read()
            c.execute(query)
        conn.close()

    # * Function to insert User and create a Account Table
    # * Parameters: First Name, Master Username, Hashed Password, Unique Key
    # * No Return Value
    @classmethod
    def userInsertion(cls, first_name: str, master_user_name: str, hashed_password: str, unique_key: str) -> None:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        with open(r'./SQL/insert-userTable.sql', 'r') as f:
            params = {
                'first_name': first_name,
                'master_user_name': master_user_name,
                'hashed_password': hashed_password,
                'unique_key': unique_key
            }
            query = f.read()
            c.execute(query, params)
        conn.commit()
        with open(r'./SQL/create-userData.sql', 'r') as f:
            query = f.read().format(master_user_name)
            c.execute(query)
        conn.close()

    # * Function to insert Account
    # * Parameters: Master Username, Platform, URL, Email, Username, Encrypted Password
    # * No Return Value
    @classmethod
    def accountInsertion(cls, master_user_name: str, platform: str, url: str, email: str, user_name: str, encrypted_password: str) -> None:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        params = {
            'platform': platform,
            'url': url,
            'email': email,
            'user_name': user_name,
            'encrypted_password': encrypted_password
        }
        with open(r'./SQL/insert-userData.sql', 'r') as f:
            query = f.read().format(master_user_name)
            c.execute(query, params)
        conn.commit()
        conn.close()

    # * Function to get User Passowrd
    # * Parameters: Master Username
    # * Return Value: Hashed Password -> String
    @classmethod
    def getUserHashedPassword(cls, master_user_name: str) -> str:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        params = {
            'master_user_name': master_user_name
        }
        with open(r'./SQL/read-HP-userTable.sql', 'r') as f:
            query = f.read()
            c.execute(query, params).fetchall()
            try:
                data = list(c.execute(query, params).fetchall()[0])
            except IndexError:
                raise UserNotFoundError
        conn.commit()
        conn.close()
        return data.pop()

    # * Function to get User Key
    # * Parameters: Master Username
    # * Return Value: Unique Key -> String
    @classmethod
    def getUserUniqueKey(cls, master_user_name: str) -> str:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        params = {
            'master_user_name': master_user_name
        }
        with open(r'./SQL/read-UK-userTable.sql', 'r') as f:
            query = f.read()
            data = list(c.execute(query, params).fetchall()[0])
        conn.commit()
        conn.close()
        return data.pop()

    # * Function to get User First Name
    # * Parameters: Master Username
    # * Return Value: First Name -> String
    @classmethod
    def getUserFirstName(cls, master_user_name: str) -> str:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        params = {
            'master_user_name': master_user_name
        }
        with open(r'./SQL/read-FN-userTable.sql', 'r') as f:
            query = f.read()
            data = list(c.execute(query, params).fetchall()[0])
        conn.commit()
        conn.close()
        return data.pop()

    # * Function to get Account List
    # * Parameters: Master Username
    # * Return Value: All Account List -> List
    @classmethod
    def getAccountTable(cls, master_user_name: str) -> list[list[str]]:
        conn = Database._sqliteConnection()
        c = conn.cursor()
        with open(r'./SQL/read-userData.sql', 'r') as f:
            query = f.read().format(f'"{master_user_name}"')
            data = c.execute(query).fetchall()

        for i in range(len(data)):
            list_cell = list(data[i])
            data.pop(i)
            data.insert(i, list_cell)

        conn.commit()
        conn.close()
        return data
