import os

# Ширина и высота изображения для вычисления новых координат
width_photo, height_photo = 2101, 2101

# Функция для обработки и перезаписи файлов с новыми значениями координат
def rename_values_in_files(folder_path):
    # Получаем список файлов в папке
    files = os.listdir(folder_path)

    # Проходим по каждому файлу
    for file_name in files:
        all_lines = list()
        if file_name.endswith('.txt'):
            # Создаем полный путь к файлу
            file_path = os.path.join(folder_path, file_name)

            # Читаем содержимое файла
            with open(file_path, 'r+') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                lines_res = lines[i].split(',')
                class_cyc = lines_res[0]
                x1 = (int(lines_res[1]) - int(int(lines_res[3]) // 2))
                y1 = (int(lines_res[2]) - int(int(lines_res[4]) // 2))
                x2 = (int(lines_res[1]) + int(int(lines_res[3]) // 2))
                y2 = (int(lines_res[2]) + int(int(lines_res[4]) // 2))
                
                x = (int(lines_res[1]) ) / width_photo 
                y = (int(lines_res[2])) / height_photo
                width =  ((x2 - x1)) / width_photo
                height = ((y2 - y1)) / height_photo

                x = f'{x:.6}'
                y = f'{y:.6}'
                width = f'{width:.6}'
                height = f'{height:.6}'

                new_line = f'{class_cyc} {x} {y} {width} {height}\n'
                all_lines.append(new_line)
        # Перезаписываем файл
        with open(file_path, 'w') as file:
            file.writelines(all_lines)

# Функция для переименования файлов, добавляя суффикс "_pro"
def rename_files(folder_path):
    # Получаем список файлов в папке
    files = os.listdir(folder_path)

    # Проходим по каждому файлу и переименовываем
    for file_name in files:
        # Создаем полный путь к файлу
        old_path = os.path.join(folder_path, file_name)

        # Создаем новое имя файла с добавлением "_pro"
        new_name = f'{os.path.splitext(file_name)[0]}_pro{os.path.splitext(file_name)[1]}'

        # Создаем полный путь к новому файлу
        new_path = os.path.join(folder_path, new_name)

        # Переименовываем файл
        os.rename(old_path, new_path)

# Функция для удаления префикса "Class_" из каждой строки в текстовых файлах
def rename_class_in_files(folder_path):
    # Получаем список файлов в папке
    files = os.listdir(folder_path)

    # Проходим по каждому файлу
    for file_name in files:
        if file_name.endswith('.txt'):
            # Создаем полный путь к файлу
            file_path = os.path.join(folder_path, file_name)

            # Читаем содержимое файла
            with open(file_path, 'r') as file:
                lines = file.readlines()
            # Заменяем " Class_" на " "
            new_lines = [line.strip(' Class_') for line in lines]

            # Перезаписываем файл с измененными данными
            with open(file_path, 'w') as file:
                file.writelines(new_lines)

if __name__ == "__main__":
    folder_path = ''  # Замените на путь к вашей папке

    rename_class_in_files(folder_path)
    rename_files(folder_path)
    rename_values_in_files(folder_path)
