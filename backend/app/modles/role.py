class Role:

    def __init__(
            self,
            id=None,
            name="",
            description="",
            status=1
    ):
        self.id = id
        self.name = name
        self.description = description
        self.status = status