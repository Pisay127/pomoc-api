import os
import uuid
from enum import Enum
from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName:
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return self.path.format(uuid.uuid4(), extension)


class ChoiceEnum(Enum):
    @classmethod
    def get_choices(cls):
        return tuple((choice.name, choice.value) for choice in cls)