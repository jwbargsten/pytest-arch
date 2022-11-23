import pytest
import sys

import pytest_arch.core_modules as cm


def test_read_legacy():
    modules = cm.list_core_modules((3, 9))
    assert "__future__" in modules


@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_read():
    modules = cm.list_core_modules((3, 10))
    assert "__future__" in modules


def test_read_error():
    with pytest.raises(FileNotFoundError):
        cm.list_core_modules((3, 5))
