from factorial import factorial, factorial_recursive
from fibo import fibo, fibo_recursive
from sorts import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort
from stack import Stack
from queue import Queue


def demo_factorial():
    while True:
        try:
            n = int(input("Введите число для вычисления факториала (или -1 для выхода): "))
            if n == -1:
                break
            print(f"Итеративный факториал({n}) {factorial(n)}")
            print(f"Рекурсивный факториал({n}) {factorial_recursive(n)}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Ошибка ввода: {e}")


def demo_fibonacci():
    while True:
        try:
            n = int(input("Введите n для вычисления n-го элемента Фибоначчи (или -1 для выхода): "))
            if n == -1:
                break
            print(f"Итеративный Фибоначчи({n}) {fibo(n)}")
            if n < 30:
                print(f"Рекурсивный Фибоначчи({n}) {fibo_recursive(n)}")
            else:
                print("Рекурсивная версия пропущена (слишком большое n)")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Ошибка ввода: {e}")


def demo_sorts():
    try:
        arr_str = input("Введите целые числа через пробел: ")
        arr = [int(x) for x in arr_str.split()]
        
        print("1. Пузырьковая сортировка")
        print("2. Быстрая сортировка")
        print("3. Сортировка подсчётом")
        print("4. Поразрядная сортировка")
        print("5. Пирамидальная сортировка")
        print("6. Все алгоритмы")
        
        choice = input()
        
        if choice == '1':
            print(f"Результат (Bubble Sort): {bubble_sort(arr.copy())}")
        elif choice == '2':
            print(f"Результат (Quick Sort): {quick_sort(arr.copy())}")
        elif choice == '3':
            print(f"Результат (Counting Sort): {counting_sort(arr.copy())}")
        elif choice == '4':
            print(f"Результат (Radix Sort): {radix_sort(arr.copy())}")
        elif choice == '5':
            print(f"Результат (Heap Sort): {heap_sort(arr.copy())}")
        elif choice == '6':
            print(f"Bubble Sort: {bubble_sort(arr.copy())}")
            print(f"Quick Sort: {quick_sort(arr.copy())}")
            print(f"Counting Sort: {counting_sort(arr.copy())}")
            print(f"Radix Sort: {radix_sort(arr.copy())}")
            print(f"Heap Sort: {heap_sort(arr.copy())}")
        else:
            print("Неверный выбор")
    except Exception as e:
        print(f"Ошибка: {e}")


def demo_stack():
    stack = Stack()
    
    while True:
        print("1. Push (добавить элемент)")
        print("2. Pop (извлечь элемент)")
        print("3. Peek (посмотреть верхний элемент)")
        print("4. Проверить пустоту")
        print("5. Размер стека")
        print("6. Минимальный элемент")
        print("7. Выход")
        
        choice = input()
        
        try:
            if choice == '1':
                val = int(input("Введите число: "))
                stack.push(val)
                print(f"Элемент {val} добавлен в стек")
            elif choice == '2':
                val = stack.pop()
                print(f"Извлечён элемент: {val}")
            elif choice == '3':
                val = stack.peek()
                print(f"Верхний элемент: {val}")
            elif choice == '4':
                print(f"Стек пустой: {stack.is_empty()}")
            elif choice == '5':
                print(f"Размер стека: {len(stack)}")
            elif choice == '6':
                val = stack.min()
                print(f"Минимальный элемент: {val}")
            elif choice == '7':
                break
            else:
                print("Неверный выбор")
        except Exception as e:
            print(f"Ошибка: {e}")


def demo_queue():
    queue = Queue()
    
    while True:
        print("1. Enqueue (добавить элемент)")
        print("2. Dequeue (извлечь элемент)")
        print("3. Front (посмотреть первый элемент)")
        print("4. Проверить пустоту")
        print("5. Размер очереди")
        print("6. Выход")
        
        choice = input()
        
        try:
            if choice == '1':
                val = int(input("Введите число: "))
                queue.enqueue(val)
                print(f"Элемент {val} добавлен в очередь")
            elif choice == '2':
                val = queue.dequeue()
                print(f"Извлечён элемент: {val}")
            elif choice == '3':
                val = queue.front()
                print(f"Первый элемент: {val}")
            elif choice == '4':
                print(f"Очередь пустая: {queue.is_empty()}")
            elif choice == '5':
                print(f"Размер очереди: {len(queue)}")
            elif choice == '6':
                break
            else:
                print("Неверный выбор")
        except Exception as e:
            print(f"Ошибка: {e}")


def main():
    while True:
        print("1. Демонстрация Факториала")
        print("2. Демонстрация Последовательности Фибоначчи")
        print("3. Демонстрация Алгоритмов Сортировки")
        print("4. Демонстрация Стека")
        print("5. Демонстрация Очереди")
        print("0. Выход")
        
        choice = input()
        
        if choice == '1':
            demo_factorial()
        elif choice == '2':
            demo_fibonacci()
        elif choice == '3':
            demo_sorts()
        elif choice == '4':
            demo_stack()
        elif choice == '5':
            demo_queue()
        elif choice == '0':
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
