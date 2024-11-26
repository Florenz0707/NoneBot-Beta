from nonebot import get_plugin_config, on_command
from nonebot.plugin import PluginMetadata
from nonebot.adapters import Message
from nonebot.params import CommandArg, ArgPlainText
from nonebot.matcher import Matcher
from time import sleep

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="Weather",
    description="Just a lesson instance for plugin",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

weather = on_command("weather.get", priority=10, block=True)


@weather.handle()
async def weather_handle(matcher: Matcher, args: Message = CommandArg()):
    await weather.send("1>\n2>\n3>\n4>\n5>")
    matcher.set_arg("option", args)


@weather.got("option", prompt="Please select......")
async def weather_got(option: str = ArgPlainText()):
    await weather.send(f"Option: {option}")
