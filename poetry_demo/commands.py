from enum import Enum


class Commands(str, Enum):
    ATTACK = "a",
    CURE = "c",
    COUNTER_ATTACK = "ca"
