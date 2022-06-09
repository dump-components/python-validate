
def validation_type(type, func):
    args = func
    if not isinstance(args, type):
        raise ValueError(f'argumento {args} da função {func.__name__} não é uma {type}')
    return args

def valid_keys_content(keys_content, keys_valid):
    if keys_content == keys_valid:
        return True