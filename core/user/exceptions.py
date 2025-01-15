from core.common.exception import SystemException

class UserException(SystemException): ...


class InvalidUserPasswordException(UserException):
    @classmethod
    def invalid_password(cls, password: str) -> "InvalidUserPasswordException":
        return cls(f"La contraseña '{password}' es inválida")


class InvalidUserNameException(UserException):
    @classmethod
    def invalid_name(cls, name: str) -> "InvalidUserNameException":
        return cls(f"El nombre de usuario '{name}' es inválido")


class InvalidUserEmailException(UserException):
    @classmethod
    def invalid_user_email(cls, email: str) -> "InvalidUserEmailException":
        return cls(f"El email '{email}' es inválido")


class InvalidPhoneNumberException(UserException):
    @classmethod
    def invalid_phone_number(cls, phone_number: str) -> "InvalidPhoneNumberException":
        return cls(f"El número de celular '{phone_number}' es inválido")


class IncorrectPasswordException(UserException):
    @classmethod
    def incorrect_password(cls, password: str) -> "IncorrectPasswordException":
        return cls(f"La contraseña '{password}' es incorrecta")


class UserIsAlreadyRegisteredException(UserException):
    @classmethod
    def is_already_registered(cls, user: str) -> "UserIsAlreadyRegisteredException":
        return cls(f"El usuario '{user}' ya se encuentra registrado")