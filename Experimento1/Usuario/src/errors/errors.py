class ApiError(Exception):
    code = 500  # Código HTTP por defecto
    description = "An error occurred"

    def __init__(self, description=None):
        if description is not None:
            self.description = description