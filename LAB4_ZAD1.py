import os


def sum_numbers_in_files(directory):
    total_sum = 0
    total_count = 0

    # Przechodzenie przez wszystkie elementy w katalogu
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Jeśli to jest plik działamy
        if os.path.isfile(item_path) and item.endswith('.txt'):
            with open(item_path, 'r') as file:
                for line in file:
                    # Dodawanie liczby z każdej linii
                    try:
                        total_sum += int(line.strip())
                        total_count += 1
                    except ValueError:
                        print("Błąd: Nie można przekonwertować linii na liczbę:", line.strip())

        # Jeśli to jest folder, to rekurencyjnie wywołujemy funkcję dla folderu
        elif os.path.isdir(item_path):
            subdir_sum, subdir_count = sum_numbers_in_files(item_path)
            total_sum += subdir_sum
            total_count += subdir_count

    return total_sum, total_count


# Ścieżka do folderu, który chcesz przeszukać
folder_path = "C:\\Users\\PycharmProjects\\Lab4\\my_folder1"

total_sum, total_count = sum_numbers_in_files(folder_path)

print("Całkowita suma liczb:", total_sum)
print("Całkowita ilość liczb:", total_count)
