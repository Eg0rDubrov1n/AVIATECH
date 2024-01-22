from environs import  Env
from dataclasses import dataclass
@dataclass
class Server:
    host: str
    port: int
    user: str
    password: str
    db_name: str
    # admin_id: str
@dataclass
class Bots:
    bot_token: str
    path_save: str
    # admin_id: str

@dataclass
class Settings:
    bots :Bots
    server: Server

def get_settings(path: str):
    env = Env()
    env.read_env(path)
    return  Settings(
        bots = Bots(
            bot_token = env.str("TOKEN"),
            path_save = env.str("myPATH")
            # admin_id = env.str("ADMIN_ID")
        ),
        server = Server(
            host = env.str("HOST"),
            port=env.str("PORT"),
            user = env.str("USER"),
            password = env.str("PASSWORD"),
            db_name = env.str("DB_NAME")
        )
    )
settings = get_settings('input')
print(settings)
