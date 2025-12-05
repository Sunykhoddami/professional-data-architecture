import numpy as np

def generate_sequential_matrix(rows: int, cols: int) -> np.ndarray:
    """
    Generates a structured 2D analytical matrix used for internal
    data-shaping validation tests.

    Parameters
    ----------
    rows : int
        Number of matrix rows.
    cols : int
        Number of matrix columns.

    Returns
    -------
    np.ndarray
        A (rows x cols) structured numeric matrix.
    """
    return np.arange(rows * cols).reshape((rows, cols))


def normalize_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    Normalizes a matrix to the range [0, 1] for analytical preprocessing.
    """
    matrix = matrix.astype(float)
    return (matrix - matrix.min()) / (matrix.max() - matrix.min())


if __name__ == "__main__":
    base_matrix = generate_sequential_matrix(5, 7)
    normalized = normalize_matrix(base_matrix)

    print("Base analytical matrix:")
    print(base_matrix)

    print("\nNormalized matrix:")
    print(normalized)
