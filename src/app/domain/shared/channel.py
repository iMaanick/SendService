from enum import Enum


class ChannelType(str, Enum):
    EMAIL = "email"
    TELEGRAM = "telegram"
    VK = "vk"
