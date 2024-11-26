from pydantic import BaseModel


class Config(BaseModel):
    weather_api_key: str = ""
    weather_command_priority: int = 10
    weather_plugin_enabled: bool = True
