import pytest
from steps.ui.desktopMobileSteps.desktop_steps import DesktopSteps
from steps.ui.desktopMobileSteps.mobile_steps import MobileSteps


@pytest.fixture(scope="session")
def desktop_mobile_step(is_mobile):
    return MobileSteps() if is_mobile else DesktopSteps()


@pytest.fixture(scope="session", autouse=True)
def desktop_mobile(request, desktop_mobile_step):
    request.node.desktop_mobile = desktop_mobile_step
