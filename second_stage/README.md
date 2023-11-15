


# Этапы выполнения задания второго этапа:
- [Анализ предоставленного датасета](#анализ-предоставленного-датасета)
- [Обучение нейронной сети](#обучение-нейронной-сети)
- [Использование обученной модели](#использование-обученной-модели)

## Анализ предоставленного датасета
Нами был проанализирован предоставленный вами [датасет](https://github.com/academy21/TC-Satellite-DataSet/tree/main).

После анализа наша команда пришла к выводу, что данные, в том формате, котором были предоставлены, не подходят для обучения модели семейства `YOLO`. Поэтому мы написали **скрипт**, который форматирует данный датасет в нужный формат.

Также было выявлено отсутствие аннотаций для циклонов 0-го и 2-го класса, в связи чего наша модель распознаёт классы циклонов, кроме двух вышеперечисленных.

![Labels](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/blob/main/second_stage/img/labels.jpg)

## Обучение нейронной сети

Обучение нейронной сети проводилось на предоставленном [датасете](https://github.com/academy21/TC-Satellite-DataSet/tree/main).
Из-за неподходящего формата датасета, нами был написан скрипт для форматирования его в *формат*, подходящий `YOLO`. Данный [скрипт](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/blob/main/second_stage/utils/convert_to_yolo.py) вы можете просмотреть в `second_stage/utils/convert_to_yolo.py`.

*Изображение с требованиями по формату файла для модели `YOLO` c [официального сайта](https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format)*
![image](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/assets/104260621/af40e879-52db-48a0-b949-39c9a4e77f63)

Следовательно, нам нужно было преобразовать все файлы в вышепоказанный формат для корректного обучения модели.
*Изначальный формат:*
![image](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/assets/104260621/1fc8aa51-63f4-4ccf-8f1e-922cca0037b1)
*Формат после обработки нашим скриптом:*
![image](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/assets/104260621/9a9a8311-f728-4331-918a-5fa4e755725f)

После этого нами была успешно обучена модель на **15 эпохах** с настройками, [представленными](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/blob/main/second_stage/train/args.yaml) в `second_stage/train/args.yaml`.

## Использование обученной модели
Обученная модель имеет название `best.onnx`.
Скрипт для использования модели предоставлен в `solution.py`.
```bash
python solution.py путь_к_папке_с_изображениями 
```
