from PIL import Image
import os
import argparse
from ultralytics import YOLO

def main():
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Обработка изображений с использованием YOLO.")
    parser.add_argument("image_folder", help="Путь к папке с изображениями для обработки.")
    args = parser.parse_args()

    # Загрузка модели YOLO с предварительно обученными весами
    model = YOLO('A:/TC-Satellite-DataSet/dataset/runs/detect/train14/weights/best.onnx', task='detect')

    # Путь к директории с тестовыми изображениями
    image_path = args.image_folder 

    # Путь для сохранения результатов
    save_path = '../../results'

    # Запуск модели YOLO на изображениях и сохранение результатов
    results = model(image_path, save_txt=True, name=f'{save_path}', stream=True)

    # Путь к директории с сохранёнными файлами меток (label)
    folder_path_label = 'results/labels'

    # Функция для переименования значений в файлах меток на основе размеров соответствующих изображений в пикселях
    def rename_values_in_files(folder_path_label, folder_path_image):
        files_label = os.listdir(folder_path_label)
        files_images = os.listdir(folder_path_image)

        for file_name_label in files_label:
            all_lines = list()
            if file_name_label.endswith('.txt'):
                for file_name_images in files_images:
                    if file_name_images.endswith('.jpg') and (file_name_images.strip('.jpg') == file_name_label.strip('.txt')):
                        file_path_lb = os.path.join(folder_path_label, file_name_label)
                        file_path_img = os.path.join(folder_path_image, file_name_images)
                        im = Image.open(f'{file_path_img}')
                        width, height = im.size

                        with open(file_path_lb, 'r') as file:
                            lines = file.readlines()

                        for i in range(len(lines)):
                            lines_res = lines[i].split(' ')
                            class_cyc = f'Class_{lines_res[0]}'
                            
                            x = int(width * float(lines_res[1]))
                            y = int(height * float(lines_res[2]))
                            width = int(width * float(lines_res[3]))
                            height = int(height * float(lines_res[4]))

                            new_lines = list()
                            new_lines.append(class_cyc)
                            new_lines.append(x)
                            new_lines.append(y)
                            new_lines.append(width)
                            new_lines.append(height)
                            new_line = f'{class_cyc} {x} {y} {width} {height}\n'
                            all_lines.append(new_line)
            # Перезаписываем файл
            with open(file_path_lb, 'w') as file:
                file.writelines(all_lines)

    # Из-за особенностей YOLO(из-за stream=True)
    for _ in results:
        pass

    # Переименование значений в файлах меток на основе размеров соответствующих изображений
    rename_values_in_files(folder_path_label=folder_path_label, folder_path_image=image_path)

if __name__ == "__main__":
    main()