from abc import ABC, abstractmethod


class DesktopMobileSteps(ABC):
    @abstractmethod
    def do_something(self) -> None:
        pass

    def common_step(self) -> None:
        raise NotImplementedError("Method not implemented.")
