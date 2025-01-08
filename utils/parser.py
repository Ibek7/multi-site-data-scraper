import yaml

def load_yaml(file_path):
    """
    Load a YAML file and return its contents as a Python dictionary.
    """
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise RuntimeError(f"Error loading YAML file {file_path}: {e}")