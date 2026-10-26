import yaml

def load_config(config_text):
    return yaml.load(config_text, Loader=yaml.Loader)
