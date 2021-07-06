import pytest
import numpy as np

from example3 import cov_exponential

def test_cov_exponential_values():
    assert cov_exponential([0, 0], 1) == 1.0
    assert cov_exponential([0, 1], 1) == np.exp(-1)
    assert cov_exponential([0, 1], 2) == np.exp(-1 / 2)

def test_cov_exponential_error():
    with pytest.raises(AssertionError):
        cov_exponential([0, 0], -1)