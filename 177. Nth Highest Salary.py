import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Получаем уникальные зарплаты и сортируем по убыванию
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Проверяем, существует ли N-ая зарплата
    if len(unique_salaries) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Берем N-1 элемент (индексация с 0)
    nth_salary = unique_salaries.iloc[N-1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})
