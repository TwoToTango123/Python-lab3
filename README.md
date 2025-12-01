# Лабораторная работа №3. Алгоритмический мини-пакет

## Основные файлы и функции

- **`factorial.py`** — функции вычисления факториала:  
  - `factorial(n: int) -> int` — итеративная реализация  
  - `factorial_recursive(n: int) -> int` — рекурсивная реализация

- **`fibo.py`** — функции вычисления n-го элемента последовательности Фибоначчи:  
  - `fibo(n: int) -> int` — итеративная реализация  
  - `fibo_recursive(n: int) -> int` — рекурсивная реализация

- **`sorts.py`** — реализации алгоритмов сортировки:  
  - `bubble_sort(a: list[int]) -> list[int]`  
  - `quick_sort(a: list[int]) -> list[int]`  
  - `counting_sort(a: list[int]) -> list[int]`  
  - `radix_sort(a: list[int], base: int = 10) -> list[int]`  
  - `bucket_sort(a: list[float], buckets_count: int | None = None) -> list[float]`  
  - `heap_sort(a: list[int]) -> list[int]`

- **`stack.py`** — класс `Stack` с методами:  
  - `push(x: int) -> None`  
  - `pop() -> int`  
  - `peek() -> int`  
  - `is_empty() -> bool`  
  - `__len__() -> int`  
  - `min() -> int`

- **`queue.py`** — класс `Queue` с методами:  
  - `enqueue(x: int) -> None`  
  - `dequeue() -> int`  
  - `front() -> int`  
  - `is_empty() -> bool`  
  - `__len__() -> int`

## Проверки ошибок

Тестами покрыты основные ошибочные сценарии:

- Передача отрицательного значения в `factorial_recursive()` и `fibo_recursive()` вызывает `ValueError` с сообщением `"n must be non-negative"`.
- Вызов `dequeue()` или `front()` у пустой очереди вызывает `IndexError` с описанием `"dequeue from empty queue"` / `"front from empty queue"`.
- Вызов `pop()` или `peek()` у пустого стека вызывает `IndexError` с соответствующим сообщением.
- Все функции сортировки корректно обрабатывают пустые списки и списки из одного элемента.
- `bucket_sort` корректно работает с числами в диапазоне `[0, 1)` и не падает на пустом вводе.

## Запуск тестов

```bash
pip install pytest
pytest tests -v
