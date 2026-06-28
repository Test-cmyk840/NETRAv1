from config import load_config, save_config


def get_token():
    config = load_config()
    return config["agent_token"]


def save_token(token):
    config = load_config()
    config["agent_token"] = token
    save_config(config)
