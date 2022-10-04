from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


class CustomArrayException(Exception):
    def __init__(self, msg: str, status_code: int):
        self.msg = msg
        self.status_code = status_code


def load(app: FastAPI) -> None:
    @app.exception_handler(CustomArrayException)
    async def custom_array_exception_handler(request: Request, exc: CustomArrayException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": f"{exc.msg}"},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=401,
            content={"error": f"{exc.errors()}"},
        )