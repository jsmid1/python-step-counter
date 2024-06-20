import pytest

from . import utils
from src.step_counting import setup_recording


# Define a session-scoped fixture
@pytest.fixture(scope='session')
def setup_session():
    pass


@pytest.fixture(scope='module')
def setup_module(request):
    recorder, _ = setup_recording.setup_recording(None, 
        request.module, {utils, setup_recording}
    )

    return recorder, setup_recording.RecodingActivated


@pytest.fixture(scope='function')
def before_each():
    pass
