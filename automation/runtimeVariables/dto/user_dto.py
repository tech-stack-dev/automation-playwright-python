from dto.user_dto import UserDto


class UserDtoVariable:
    def __init__(self):
        self.value: UserDto


user_dto_variable = UserDtoVariable()

# Example usage:
# user_dto_variable.value = some_user_dto
