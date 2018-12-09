def _init_globalar():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value

def get_value(name):
    if name in _global_dict:
        return _global_dict[name]
    else:
        return "not found"