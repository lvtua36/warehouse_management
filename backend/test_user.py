from app.repositories.user_repository import UserRepository

user = UserRepository.find_by_username("admin")

print(user)