from core.common.exception import SystemException
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from typing import Any, Dict, List, Callable, Type

def success_response(data: Dict[str, Any]|List[Dict[str, Any]]) -> Response:
    return Response({
        'status': 'success',
        'code': 200,
        'data': data
    }, status = status.HTTP_200_OK)

def failure_response(message: str) -> Response:
    return Response({
        'status': 'failure',
        'code': 400,
        'message': message
    }, status = status.HTTP_400_BAD_REQUEST)

def internal_server_error_response() -> Response:
    return Response({
        "status": "failure",
        "code": 500,
        "message": "Internal Server Error"
    }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

def invalid_field_response(errors: Dict) -> Response:
    msg = "Asegurese de llenar correctamente los campos requeridos: " + str(list(errors.keys()))
    e = Exception(msg)
    return failure_response(str(e))

def validate(format: Type[serializers.Serializer] = None) -> Callable:
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            try:
                if request.method == "GET" or request.method == "DELETE":
                    return func(self, request, **kwargs)
                else:
                    serializer = format(data=request.data)
                    if not serializer.is_valid():
                        return invalid_field_response(serializer.errors)
                    return func(self, request)
            except SystemException as e:
                return failure_response(str(e))
            except:
                return internal_server_error_response()
        return wrapper
    return decorator
