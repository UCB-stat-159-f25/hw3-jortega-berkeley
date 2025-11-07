import os
import pytest
from ligotools import readligo as rl

DATA_CANDIDATES = [
    "data/H-H1_LOSC_4_V2-1126259446-32.hdf5",
    "data/L-L1_LOSC_4_V2-1126259446-32.hdf5",
]

@pytest.mark.parametrize("path", DATA_CANDIDATES)
def test_loaddata_shapes_and_meta(path):
    if not os.path.exists(path):
        pytest.skip(f"Missing test file: {path}")

    strain, meta, dq = rl.loaddata(path, tvec=False)

    assert strain.ndim == 1 and strain.size > 0
    assert set(["start", "stop", "dt"]).issubset(meta.keys())
    assert isinstance(meta["dt"], (float, int)) and meta["dt"] > 0
    assert isinstance(dq, dict) and len(dq) > 0