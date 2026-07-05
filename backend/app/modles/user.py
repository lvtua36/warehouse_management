class User:
    def __init__(
            self,
            id=None,
            role_id=None,
            full_name="",
            username="",
            email="",
            password="",
            phone="",
            avatar="",
            status=1
    ):
        self.id = id
        self.role_id = role_id
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.avatar = avatar
        self.status = status