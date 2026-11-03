"""
Smoke tests for plab.
"""

import importlib.metadata

import plab
import plab.ml
import plab.probability
import plab.stats


def test_package_imports():
    """Verify root package import."""
    assert plab is not None


def test_subpackage_imports():
    """Verify subpackage imports."""
    assert plab.probability is not None
    assert plab.ml is not None
    assert plab.stats is not None


def test_package_version():
    assert importlib.metadata.version("plab") == "0.1.0"
