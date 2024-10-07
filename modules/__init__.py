from .cryptography import Cryptography
from .database import Database
from .gui import GUI
from .regex import Regex
from .hashing import Hashing
from .exceptions import UserNotFoundError

actions = {
    "login": {
        "positive": 'Login Successfull', 
        "negative": 'Login Unsuccessfull'
    },
    "register": {
        "positive": 'Registration Successfull',
        "negative":'Registration Unsuccessfull'
    },
    "account": {
        "positive": 'Account Information has been Added',
        "negative": 'Account Information cannot be Added'
    },
    "credentials": {
      "username": {
        "negative": 'Invalid Username'
      },
      "password": {
        "negative": 'Invalid Password'
      }
    },
    "not_found": {
      "negative": 'User not Found'
    },
    "empty_fields_account": {
      "negative": 'Platform and Password field cannot be Empty.'
    },
    "empty_fields_reg": {
      "negative": 'Name, Username and Password field cannot be Empty.'
    },
    "empty_fields_login": {
      "negative": 'Username and Password field cannot be Empty.'
    }
}

Database.init()