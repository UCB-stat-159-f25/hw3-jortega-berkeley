import os
import numpy as np
import pytest
from ligotools import utils

def test_whiten_roundtrip_like_shape():
    # fake PSD as callable returning flat spectrum
    def flat_psd(freqs): return np.ones_like(freqs)
    x = np.random.randn(8192)
    y = utils.whiten(x, flat_psd, dt=1/4096)
    assert y.shape == x.shape
    assert np.isfinite(y).all()

def test_write_wavfile_and_reqshift(tmp_path):
    fs = 4096
    t = np.arange(0, 1.0, 1/fs)
    x = np.sin(2*np.pi*200*t)  # 200 Hz tone
    y = utils.reqshift(x, f0=200, sample_rate=fs, df=50)
    out = tmp_path / "tone.wav"
    utils.write_wavfile(out.as_posix(), fs, y)
    assert out.exists() and out.stat().st_size > 0
