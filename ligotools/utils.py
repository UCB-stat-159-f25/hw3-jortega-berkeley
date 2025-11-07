import numpy as np
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

def whiten(strain, psd, dt):
    Nt = len(strain)
    freqs = np.fft.rfftfreq(Nt, dt)
    hf = np.fft.rfft(strain)
    white_hf = hf / (np.sqrt(psd(freqs)/2.0))
    white_ht = np.fft.irfft(white_hf, n=Nt)
    return white_ht

def write_wavfile(filename, fs, data):
    data = np.asarray(data)
    peak = np.max(np.abs(data)) or 1.0
    scaled = (data / peak * 32767).astype(np.int16)
    wavfile.write(filename, int(fs), scaled)

def reqshift(data, f0, sample_rate, df):
    t = np.arange(len(data)) / float(sample_rate)
    shifted = data * np.exp(1j*2*np.pi*df*t)
    return np.real(shifted)

def plot_psd_windowing(strain, fs, nperseg=4*1024, noverlap=2*1024, window="hann", outpath=None):
    f, Pxx = signal.welch(strain, fs=fs, nperseg=nperseg, noverlap=noverlap, window=window)
    plt.figure(figsize=(6,4))
    plt.loglog(f, np.sqrt(Pxx))
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("ASD [strain/√Hz]")
    plt.title("Amplitude Spectral Density (Welch)")
    plt.grid(True, which="both", ls=":")
    if outpath:
        plt.savefig(outpath, dpi=150, bbox_inches="tight")
    return f, Pxx
