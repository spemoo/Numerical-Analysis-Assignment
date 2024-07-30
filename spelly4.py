import numpy as np
import matplotlib.pyplot as plt

def compute_fft():
    # Parameters
    f1 = 50    # Frequency of the first sine wave
    f2 = 120   # Frequency of the second sine wave
    fs = 1000  # Sampling frequency
    t = np.linspace(0, 1, fs, endpoint=False)  # Time vector for 1 second

    # Signal
    s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

    # Compute FFT
    fft_s = np.fft.fft(s)
    fft_s = np.fft.fftshift(fft_s)  # Shift zero frequency component to the center
    freq = np.fft.fftfreq(len(s), d=1/fs)
    freq = np.fft.fftshift(freq)  # Shift zero frequency component to the center

    # Plot the signal
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, s)
    plt.title('Time Domain Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    # Plot the FFT
    plt.subplot(2, 1, 2)
    plt.plot(freq, np.abs(fft_s))
    plt.title('Frequency Domain Signal (FFT)')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid()

    plt.tight_layout()
    plt.show()

# Run the function
compute_fft()