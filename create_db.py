import  pandas as pd
import numpy as np
import random


def generate_large_dataset(n_rows=100000, output_file="synthetic_data.csv"):
    """
    Генерує велику базу даних для тренування EDA та зберігає її у CSV-файл.

    :param n_rows: Кількість рядків у датасеті
    :param output_file: Ім'я файлу для збереження
    """
    np.random.seed(42)  # Для відтворюваності результатів

    # Списки значень для категоріальних змінних
    education_levels = ["High School", "Bachelor", "Master", "PhD", "None"]
    marital_statuses = ["Single", "Married", "Divorced", "Widowed"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Diego", "Dallas", "San Jose", "Austin",
              "Seattle"]
    jobs = ["Engineer", "Doctor", "Teacher", "Lawyer", "Artist", "Scientist", "Salesperson", "Manager", "Clerk",
            "Freelancer"]
    genders = ["Male", "Female"]

    # Генеруємо дані
    data = {
        "id": np.arange(1, n_rows + 1),
        "age": np.random.randint(18, 90, n_rows),
        "income": np.random.randint(20000, 200000, n_rows),
        "hours_per_week": np.random.randint(10, 70, n_rows),
        "expenses": lambda x: x["income"] * np.random.uniform(0.3, 0.8, n_rows),
        "education": np.random.choice(education_levels, n_rows),
        "marital_status": np.random.choice(marital_statuses, n_rows),
        "city": np.random.choice(cities, n_rows),
        "job": np.random.choice(jobs, n_rows),
        "gender": np.random.choice(genders, n_rows)
    }

    df = pd.DataFrame(data)

    # Випадково додаємо пропущені значення у 5% випадків
    for col in df.columns:
        df.loc[df.sample(frac=0.05).index, col] = np.nan

    # Додаємо аномальні значення
    df.loc[np.random.choice(df.index, size=50), "income"] = 1_000_000  # Дуже високий дохід
    df.loc[np.random.choice(df.index, size=20), "hours_per_week"] = 100  # Нереалістичне навантаження

    # Зберігаємо у файл
    df.to_csv(output_file, index=False)
    print(f"✅ База даних '{output_file}' створена! Розмір: {df.shape}")

    return df


# Виклик функції
df = generate_large_dataset()
