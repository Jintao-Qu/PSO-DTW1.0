def _init_visited_set():
    global _visited_dict
    _visited_dict = {}

def set_value(name, value):
    _visited_dict[name] = value

def get_value(name):
    if name in _visited_dict:
        return _visited_dict[name]
    else:
        return "not found"