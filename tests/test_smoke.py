import importlib.metadata

import plab


def test_package_imports():
    assert plab is not None


def test_package_version():
    assert importlib.metadata.version("plab") == "0.1.0"
