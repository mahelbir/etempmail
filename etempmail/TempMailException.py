class TempMailException(Exception):
    def __init__(self, exception_type: str, exception_message: str, response=None, debug: bool = True) -> None:
        if debug and response is not None:
            print(response.status_code)
            print(response.headers)
            print(response.text)
        super().__init__(f"{exception_type.title()}: {exception_message.capitalize()} error")
