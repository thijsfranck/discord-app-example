import pytest
from pytest_mock import MockerFixture

from .client import logger, on_ready


@pytest.mark.asyncio()
async def test__on_ready_logs_correct_message(mocker: MockerFixture) -> None:
    """
    Test the on_ready function.

    Asserts
    -------
    - The logger.info function is called once with the correct message.
    """
    logger_info = mocker.spy(logger, "info")
    await on_ready()
    logger_info.assert_called_once_with("%s has connected to Discord!", mocker.ANY)
