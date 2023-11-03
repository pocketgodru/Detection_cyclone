from ultralytics import YOLO
from PIL import Image
# Load a model
model = YOLO("best.onnx")  # загрузка обученной модели

results = model("")  # укажите путь к вашему изображению

for r in results:
    im_array = r.plot()  
    im = Image.fromarray(im_array[..., ::-1]) 
    im.show()  # показ изображения
    im.save('results.jpg') # сохранение изображения с предсказанием
