def calculate_covariance_matrix(data):
    """
    Calculate the covariance matrix for the given asset returns data.

    Parameters:
    data (DataFrame): A DataFrame containing asset returns.

    Returns:
    DataFrame: A covariance matrix.
    """
    return data.cov()


def visualize_covariance_matrix(covariance_matrix):
    """
    Visualize the covariance matrix using a heatmap.

    Parameters:
    covariance_matrix (DataFrame): A covariance matrix to visualize.
    """
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 8))
    sns.heatmap(covariance_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Covariance Matrix')
    plt.show()