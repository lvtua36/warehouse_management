from app.repositories.role_repository import RoleRepository

class RoleService:

    @staticmethod
    def get_all():

        return RoleRepository.get_all()

    @staticmethod
    def create(
            name,
            description,
    ):

        RoleRepository.create(
            name,
            description
        )

    @staticmethod
    def update(
            role_id,
            name,
            description,
    ):
        RoleRepository.update(
            role_id,
            name,
            description
        )

    @staticmethod
    def delete(role_id):
        RoleRepository.delete(role_id)

    @staticmethod
    def find_by_id(role_id):
        return RoleRepository.find_by_id(role_id)