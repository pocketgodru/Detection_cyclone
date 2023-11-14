from ultralytics import YOLO
from PIL import Image

model = YOLO('model/best_detect.onnx', task='detect')  # Загрузка обученной модели для детекции

results = model('img/input_1.jpg') # Обработка входного изображение
for r in results:
    im_array = r.plot()
    im = Image.fromarray(im_array[..., ::-1])
    im.show()  # Вывод выходного изображения
    im.save('results.jpg')  # Сохранение выходного изображения
