from fastapi import HTTPException, status


class DuplicateException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "This instance exist"


class NotFoundException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "Not Found"


class UnauthorizedException(HTTPException):
    def __init__(self, detail="Unauthorized"):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = detail


class ForbiddenException(HTTPException):
    def __init__(self, detail="Operation not permitted"):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = detail


class BadRequestException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "Incorrect email or password"


class KeycloakConnectionError(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_424_FAILED_DEPENDENCY
        self.detail = "Connection to keycloak failed"
