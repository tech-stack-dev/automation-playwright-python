from steps.ui.desktopMobileSteps.desktop_mobile_steps import DesktopMobileSteps


class DesktopSteps(DesktopMobileSteps):
    def do_something(self) -> None:
        raise NotImplementedError("Method not implemented.")


desktop_steps = DesktopSteps()
