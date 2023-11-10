from ultralytics import YOLO
from PIL import Image
# Load a model
model = YOLO('model/best_segment.onnx', task='segment')  # загрузка обученной модели для сегментирования 
#model = YOLO('best_detect.onnx', task='detect')  # загрузка обученной модели для детекции

results = model('img/input_1.jpg') # ваше изображение
# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # показ изображения
    #im.save('results.jpg')  # сохранение изображения