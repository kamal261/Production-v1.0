from abc import ABC, abstractmethod


class BaseProvider(ABC):

    name = "base"

    @abstractmethod
    def chat(self, messages, **kwargs):
        raise NotImplementedError