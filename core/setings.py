from environs import  Env
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str
    path_save: str
    # admin_id: str

@dataclass
class Settings:
    bots :Bots

def get_settings(path: str):
    env = Env()
    env.read_env(path)
    return  Settings(
        bots = Bots(
            bot_token = env.str("TOKEN"),
            path_save = env.str("myPATH")
            # admin_id = env.str("ADMIN_ID")
        )
    )
settings = get_settings('input')
print(settings)
