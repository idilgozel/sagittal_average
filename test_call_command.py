import subprocess

import numpy as np
import sagittal_brain as sb


def test_call_command():
    input = np.zeros((20, 20))
    expected = np.array(
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]
    )
    np.savetxt("brain_sample.csv", input, fmt="%.1f", delimiter=",")
    result = subprocess.run(
        ["python", "sagittal_brain.py", "brain_sample.csv", "-o", "brain_average.csv"],
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    print(result.stderr)
    print(result.returncode)
    assert result.returncode == 0
    output = np.loadtxt("brain_average.csv", delimiter=",")
    np.testing.assert_array_equal(output, expected)
