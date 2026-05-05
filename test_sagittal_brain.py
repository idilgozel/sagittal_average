import numpy as np
import sagittal_brain as sb


def test_run_averages():
    sample_data = np.array([[0.0, 0.0, 0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    np.savetxt("brain_sample.csv", sample_data, fmt="%.1f", delimiter=",")
    sb.run_averages("brain_sample.csv", "brain_average.csv")
    result = np.loadtxt("brain_average.csv", delimiter=",")

    expected = np.array([3.66666667, 4.33333333, 5.0])
    np.allclose(result, expected)
