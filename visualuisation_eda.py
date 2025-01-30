import matplotlib.pyplot as plt
import seaborn as sns


def visualize_data(df):
    """
    Function for visualizing numerical and categorical variables in a DataFrame.

    Parameters:
        df (DataFrame): The input dataset.

    Visualizations:
    - Histograms + KDE for numerical variables
    - Countplots for categorical variables
    """

    # Identify numerical and categorical columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numerical_columns = df.select_dtypes(include=['number']).columns.tolist()

    sns.set_style('darkgrid')

    # 📊 Visualization of numerical variables
    if numerical_columns:
        fig, axes = plt.subplots(len(numerical_columns), 1, figsize=(14, len(numerical_columns) * 3))
        fig.suptitle('📈 Distribution of Numerical Variables', fontsize=16, fontweight='bold')

        if len(numerical_columns) == 1:
            axes = [axes]  # Prevents error if there is only one variable

        for idx, feature in enumerate(numerical_columns):
            sns.histplot(df[feature], kde=True, ax=axes[idx], color='royalblue', bins=30)
            axes[idx].set_title(f'{feature} | Skewness: {round(df[feature].skew(), 2)}', fontsize=12, fontweight='bold')
            axes[idx].set_xlabel('')

        plt.tight_layout(rect=[0, 0, 1, 0.98])
        plt.show()

    # 📊 Visualization of categorical variables
    if categorical_columns:
        fig, axes = plt.subplots(len(categorical_columns), 1, figsize=(14, len(categorical_columns) * 3))
        fig.suptitle('📊 Distribution of Categorical Variables', fontsize=16, fontweight='bold')

        if len(categorical_columns) == 1:
            axes = [axes]  # Prevents error if there is only one variable

        for idx, feature in enumerate(categorical_columns):
            sns.countplot(y=df[feature], order=df[feature].value_counts().index, ax=axes[idx], palette='viridis')
            axes[idx].set_title(f'{feature} (Top Categories)', fontsize=12, fontweight='bold')

        plt.tight_layout(rect=[0, 0, 1, 0.98])
        plt.show()

    print("✅ Visualization completed!")
