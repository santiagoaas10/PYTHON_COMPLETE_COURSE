class RunTimeErrorWithCode(Exception):
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, message,code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code
    

#linea poderosa:
err = RunTimeErrorWithCode('An Error happened', 500)
print(err.__doc__) #el doc llama a la cadena de documentacion que comenté arriba!!! genial!!!



raise RunTimeErrorWithCode('error de server', 500)