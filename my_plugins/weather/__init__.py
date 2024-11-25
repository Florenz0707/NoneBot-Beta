from nonebot import get_plugin_config, on_command
from nonebot.plugin import PluginMetadata
from nonebot.adapters import Message
from nonebot.params import CommandArg
from time import sleep

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="Weather",
    description="Just a lesson instance for plugin",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

get_weather = on_command("weather.get", priority=10, block=True)


@get_weather.handle()
async def _(args: Message = CommandArg()):
    location = args.extract_plain_text()
    await get_weather.send(f"是{location}的天气吗？我看看......")
    sleep(3)
    await get_weather.finish("我不知道！")
