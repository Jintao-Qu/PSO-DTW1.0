def _init_visited_set():
    global _visited_dict
    _visited_dict = {}

def set_value(name, value):
    _visited_dict[name] = value

def get_value(name):
    return _visited_dict[name]