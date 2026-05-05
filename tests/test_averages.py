import numpy as np
import sagittal_brain as sb


def test_run_averages():
    sample_data = np.zeros((20, 20))
    sample_data[0, 0] = 1
    np.savetxt("brain_sample.csv", sample_data, fmt="%.1f", delimiter=",")
    sb.run_averages("brain_sample.csv", "brain_average.csv")
    result = np.loadtxt("brain_average.csv", delimiter=",")

    expected = np.zeros(20)
    expected[0] = 1.0 / 20
    # what is the error here and how to fix it?
    # the expected is a 1D array, but the result is a 2D array with one row and 20 columns.
    # we can fix it by making the expected a 2D array with one row and 20 columns, or by making the result a 1D array with 20 elements.
    expected = expected[np.newaxis, :]

    assert np.allclose(result, expected)
