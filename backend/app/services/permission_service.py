from app.repositories.permission_repository import PermissionRepository

class PermissionService:

    @staticmethod
    def get_all():
        return PermissionRepository.get_all()

    @staticmethod
    def find_by_id(permission_id):
        return PermissionRepository.find_by_id(permission_id)

    @staticmethod
    def create(code, name, module, description):
        PermissionRepository.create(
            code,
            name,
            module,
            description
        )

    @staticmethod
    def update(permission_id, code, name, module, description):
        PermissionRepository.update(
            permission_id,
            code,
            name,
            module,
            description
        )

    @staticmethod
    def delete(permission_id):

        PermissionRepository.delete(permission_id)