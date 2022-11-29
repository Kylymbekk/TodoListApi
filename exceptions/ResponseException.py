from fastapi.responses import JSONResponse


class ResponseException(Exception):
    def __init__(self, text, status):
        self.text = text
        self.status = status

    def get_response(self):
        return JSONResponse(content={
            'text': self.text
        }, status_code=self.status)