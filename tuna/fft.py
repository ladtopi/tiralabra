"""
This module contains functions for taking the Discrete Fourier Transform of a
signal, and its inverse. The algorithm is basically the one suggested by Cooley
and Tukey in 1965, as discussed in Introduction to Algorithms (CLRS).
"""

from cmath import exp, pi

from tuna.typing import NumericSequence


def fft(x: NumericSequence) -> NumericSequence:
    """
    Implements the Fast Fourier Transform (FFT) algorithm. The algorithm follows
    the variant of Cooley-Tukey that is discussed in Introduction to Algorithms by CLRS.

    [Cooley-Tukey FFT algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm)

    Args:
        x: The input signal as a sequnce of discrete samples.

    Returns:
        The complex-valued spectrum of the input signal.
    """
    n = len(x)
    if n == 1:
        return x
    X = [0] * n
    even = fft(x[::2])
    odd = fft(x[1::2])
    for k in range(n // 2):
        twiddle_factor = exp(-2j * pi * k / n)
        X[k] = even[k] + twiddle_factor * odd[k]
        X[k + n // 2] = even[k] - twiddle_factor * odd[k]
    return X
