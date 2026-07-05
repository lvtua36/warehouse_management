from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = bcrypt.generate_password_hash(
    "123"
).decode()

print(password)
