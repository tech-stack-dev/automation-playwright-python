from desktop_mobile_steps import DesktopMobileSteps


class MobileSteps(DesktopMobileSteps):
    def do_something(self) -> None:
        raise NotImplementedError("Method not implemented.")


mobile_steps = MobileSteps()
