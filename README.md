# **Детекция тропических циклонов**

## Содержание:
  
-  [🌪Введение](#введение)
  
-  [🌟Актуальность](#актуальность)

-  [📌Цель и задачи](#цель-и-задачи)
  
-  [🔍Анализ области](#анализ-области)

-  [📋Критерии определения перспективного алгоритма](#критерии-определения-перспективного-алгоритма)
  
-  [📊Сравнительный анализ используемых алгоритмов](#сравнительный-анализ-используемых-алгоритмов)
  
-  [💡Предлагаемое решение](#предлагаемое-решение)
  
-  [⚖️Преимущества и возможные риски](#%EF%B8%8Fпреимущества-и-возможные-риски)
  
-  [⌨️Реализация](#%EF%B8%8Fреализация)
  
-  [🔛Сравнительный анализ датасетов](#сравнительный-анализ-датасетов)
  
-  [🤖Нейронная сеть:](#нейронная-сеть)
  
	- [Обучение нейронной сети для детекции](#обучение-нейронной-сети-для-детекции)
   
	- [Обучение нейронной сети для сегментации](#обучение-нейронной-сети-для-сегментации)
   
	-  [Пример использования](#пример-использования)
  
-  [📲Телеграмм бот](#телеграмм-бот)
  
-  [📩Обратная связь](#обратная-связь)

# 🌪Введение

  

Для начала давайте поймем, что из себя представляет циклон.

  

Циклон - это внушительное атмосферное явление, характеризующееся сформировавшимся центром низкого давления, сопровождаемым интенсивными ветрами и обильными осадками. Это метеорологическое явление, образующееся изначально в результате возмущения над теплыми океанскими водами, что способствует развитию вихревого движения благодаря накоплению тепла и влажности.

  

Движение и взаимодействие циклонов находятся под влиянием ветров в тропических широтах, над непрерывно меняющейся атмосферной динамикой. Взаимодействие между различными циклонами может вызывать не только формирование более мощных систем, но и изменение их траекторий, усиление интенсивности осадков и ветров, а также приводить к иным метеорологическим изменениям.

  

Затухание циклона - это процесс, обусловленный покиданием теплых океанских вод, истощением источника энергии или воздействием других атмосферных систем, что приводит к угасанию интенсивности и, в конечном итоге, исчезновению этого атмосферного явления.


# 🌟Актуальность

  

Обнаружение тропических циклонов является важной проблемой для современной науки и практики метеорологии. Эта важная проблема привлекает внимание исследователей и специалистов во многих странах, особенно в регионах, где тропические циклоны являются распространенным и опасным природным явлением.

  

1. Предотвращение и уменьшение числа человеческих жертв:

  

Отслеживание тропических циклонов может способствовать снижению человеческих жертв, уменьшению разрушений инфраструктуры и сохранению экосистем.

  

2. Защита экономики:

  

Тропические циклоны могут оказывать серьезное влияние на экономику стран и регионов, где развито сельское хозяйство, туризм и другие виды деятельности. Обнаружение их помогает лучше планировать и защищать экономику от разрушительных последствий.

  

3. Научные исследования:

Понимание и прогнозирование тропических циклонов играют ключевую роль в научных исследованиях, направленных на изучение климатических изменений и паттернов погоды.

  

# 📌Цель и задачи

  

Цель данного проекта – это изучение, разработка и внедрение технологии детектирования тропических циклонов с использованием данных, полученных через фотографии со спутников.

  

**Задачи:**

- Изучить характеристики и поведение циклонов

- Анализ существующих решений

- Выбор наиболее подходящего семейства нейронных сетей

- Создание или поиск датасета с нужными нам данными

- Обучение модели для обнаружения расположения циклона, его центра и траектории

  

В результате у нас должен получиться продукт, которая будет способна достаточно точно определять центр тропического циклона и траекторию его движения на спутниковых снимках.

  

Также возможно создание графического интерфейса для более удобного взаимодействия с пользователями и систему оповещения пользователей, чтобы уведомлять их о возможной опасности.

  

# 🔍Анализ области

  

Нами было проанализировано, как в мире решают задачу детекции тропических циклонов и какие алгоритмы для этого используются.

  

**Были выделены такие решения:**

  

1. Спутниковые системы GOES (Environmental Satellites) и Himawarir, обеспечивают непрерывный мониторинг погодных условий и климатических явлений на Земле.

  

2. Для обработки изображений тропических циклонов используются алгоритмы компьютерного зрения и машинного обучения. Они используют анализ спутниковых данных, чтобы помочь определить контуры, границы, а также предсказать поведение циклона. Примерами таких алгоритмов являются R−CNN, YOLO и SSD. Они основаны на моделях глубокого обучения и широко используются для обнаружения объектов на изображениях.

  

3. Динамическое моделирования циклона используется для прогнозирования движения и развития тропических циклонов. Оно основано на уравнениях атмосферы и океана, позволяя ученым делать более точные прогнозы траектории и силы циклонов.

  

4. Использование данных с метеорологических станций, радаров, буев и других датчиков на местности также используются для уточнения информации о тропических циклонах.

  

# 📋Критерии определения перспективного алгоритма

  

Нами были установлены основные критерии выбора наиболее перспективного алгоритма для решения поставленных задач.

  

1. **Точность (Precision):**

	- Включает в себя способность алгоритма точно идентифицировать циклоны.

	- Предполагает минимизацию ложных срабатываний и пропусков.

	- Может включать в себя использование различных метрик оценки, таких как точность, чувствительность, специфичность и F1-мера.

2. **Полнота (Recall):**

	- Эта метрика оценивает способность модели обнаруживать все фактические положительные экземпляры.

	- Полнота показывает, насколько успешно модель идентифицирует положительные экземпляры в данных.

3. **F1-мера (F1-score):**

	- Это среднее между точностью и полнотой, обеспечивающее обобщенную меру производительности модели.

	- Высокое значение F1-меры указывает на хорошее сочетание точности и полноты классификации модели.

5. **Скорость работы:**

	- Определяет, насколько быстро алгоритм может обрабатывать входные данные и делать прогнозы.

	- Важно для оперативного мониторинга и реагирования на изменения в атмосфере.

6. **Масштабируемость:**

	- Гарантирует, что алгоритм способен обрабатывать входные данные различных размеров без потери производительности.

7. **Легкость внедрения и сопровождения:**

	- Подразумевает, что алгоритм должен быть легко интегрируемым в существующую систему мониторинга и обслуживаемым.

	- Включает в себя удобство настройки параметров, возможность обновления и масштабирования.

8. **Ресурсоемкость и вычислительные требования:**

	- Эффективное использование вычислительных ресурсов устройства (процессор, память и энергия).

	- Оптимизация алгоритма, чтобы минимизировать потребление ресурсов.

  

Итак, идеальный алгоритм должен сбалансированно сочетать высокую точность, быструю обработку данных, масштабируемость, легкость внедрения и обслуживания, а также эффективное использование ресурсов, чтобы соответствовать всем установленным критериям.

  

# 📊Сравнительный анализ используемых алгоритмов

  

Для детекции тропических циклонов существует множество алгоритмов и методов. Традиционные методы компьютерного зрения используют выделение признаков изображений, таких как границы и текстуры.

  

Они развивались с *1960-х годов*, но с появлением глубокого обучения стали менее популярными. Современные алгоритмы глубокого обучения, такие как R-CNN, YOLO и SSD, обеспечивают высокую точность и эффективность и широко используются для детекции тропических циклонов на спутниковых изображениях.

  

Различие между нейронными сетями:

  

1. `R-CNN` и его вариации: Эти сети используются для нахождения объектов на изображениях путем выделения и классификации областей. Fast R-CNN и Faster R-CNN улучшают скорость и точность детекции.

  

2. `YOLO` (You Only Look Once): Эта сеть также обнаруживает объекты, но делает это быстрее, рассматривая изображение целиком как одну проблему.

  

3. `SSD` (Single Shot MultiBox Detector): Она также обнаруживает объекты в реальном времени, используя несколько слоев для разных размеров объектов, в отличие от YOLO, которая использует только один слой.

  

Все эти алгоритмы эффективны при обнаружении объектов, но они подходят для самых разных вариантов использования из-за различных подходов обработки изображений.

  

| Критерии сравнения | R−CNN | YOLO | SSD | Классическое компьютерное зрение |
| :----------------: | :---: | :--: | :-: | :------------------------------: |
| Точность обнаружения | Высокая | Высокая | Высокая | Средняя |
| Скорость работы | Средняя | Высокая | Высокая | Низкая |
| Масштабируемость | Средняя | Средняя | Высокая | Низкая |
| Внедрение и сопровождения | Доп. настройка | Низкая | Высокая | Сложная |
| Ресурсоёмкость | Высокая | Низкая | Средняя | Низкая |


# 💡Предлагаемое решение

Основная идея и концепция предлагаемого нами решения - это обучить модель для детекции тропических циклонов, обученную на открытых (либо созданных нами) датасетах. 

**Для реализации базовой функциональности нам потребуется следующее:**

1. Нам необходимо исследовать доступные открытые датасеты о тропических циклонах, включая спутниковые изображения, метеорологические данные и информацию о траекториях и характеристиках циклонов. Это поможет определить, какие данные могут быть использованы для обучения нейронной сети.
  
2. Нужно оценить качество данных, предоставленных в датасетах. К примеру разрешение изображений, покрытие территории, частоту обновления и другие важные атрибуты. Это поможет определить, насколько эти данные могут быть полезны при обучении нейросети для детекции циклонов.

3. Необходимо оценить потенциальные ограничения и проблемы, связанные с использованием открытых датасетов.

Например, недостаточное количество данных, шум, несбалансированность классов и многие другие факторы, которые могут повлиять на точность и надежность модели детекции циклонов.

**Теперь непосредственно о том, как можно улучшить точность распознавания нейронной сети:**

1. Использование последних версий моделей, таких как R-CNN, YOLO или SSD, повысит точность распознавания тропических циклонов.

2. Улучшение и расширение датасета:

	- Добавление больше разнообразных данных о тропических циклонах
	- Использование вручную размеченного датасета
	- Применение методов аугментации данных (изменение масштаба, добавление шума) улучшает устойчивость нейронной сети к разным условиям.

3. Использование нескольких моделей позволит получить более точные результаты, так как каждая модель будет обращать внимание на разные паттерны на изображении с циклоном.

Применение данных стратегий улучшит точность распознавания центра тропического циклона и обеспечит более надежное прогнозирование его положения.

# ⚖️Преимущества и возможные риски

Использование нашего решения имеет как ряд преимуществ, так и ряд определенных недостатков.

***Преимущества:***

1. Автоматическое **точное** обнаружение тропических циклонов с расчётом его центра и направления движения
   
2. Проект решает общественную проблему безопасности с помощью нейронной сети, позволяющей обнаруживать тропические циклоны

3. Проект способствуют техническому развитию предприятий и отраслей (метеорологические службы, государственные органы и службы, туризм)

***Недостатки:***

  

1. Технические проблемы:
	- Несовместимость систем
	- Непредвиденный отказ оборудования

2. Неправильное внедрение и обучение нейронной сети может повлечь за собой серьёзные проблемы, которые приведут к ухудшению качества работы систем

# ⌨️Реализация

Реализация включает в себя такие этапы, как:

1. Обучение нейронной сети:
	- Поиск нужного датасета
	- Подготовка к обучению модели
	- Обучение модели
	
Этот этап включает в себя процесс сбора данных с открытых источников и обучение модели на предварительно обработанных данных и настройки её параметров.

  

2. Тестирование и валидация модели на реальных снимках:
	- Протестировать обученную модель на реальных снимках
	
На этом этапе мы должны провести тестирования и валидации модели, чтобы оценить ее производительность, точность и способность обнаруживать тропические циклоны на изображениях с высокой точностью.

3. Доработка и использование системы в реальных условиях:
	- Анализ производительности в реальных условиях
	- Улучшение и доработка системы, её обновление и масштабирование
	- Получение обратной связи от пользователей нашего продукта

  

Этот шаг подразумевает проведение анализа производительности системы в реальных условиях и различных ситуациях.

  

# 🔛Сравнительный анализ датасетов


В данном пункте мы произведем сравнительный анализ датасетов, содержащих информацию о детекции циклонов.

**Были выделены датасеты:**

1. Universe Roboflow:
	- [typhoon Image Dataset](https://universe.roboflow.com/hanwen-zhang-poufi/typhoon-6pqhj/dataset/2)

	- [test Image Dataset](https://universe.roboflow.com/hanwen-zhang-poufi/test-fwsao/dataset/2)

> Данный пункт будет дополняться со временем

# 🤖Нейронная сеть
## Обучение нейронной сети для детекции:

Мы провели предварительное обучение модели `YOLOv8` на [наборе данных](https://universe.roboflow.com/hanwen-zhang-poufi/typhoon-6pqhj/dataset/2), который включает в себя обнаружение тропического циклона и его центра.

Актуальный результат тестовой модели:

<br></br>

### *Входное изображение:*

<br></br>

![image](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/blob/main/first_stage/img/input_1.jpg)

<br></br>

### *Изображение на выходе:*

<br></br>

![image](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/blob/main/first_stage/img/output_1.jpg)

<br></br>

> *На данный момент наша модель может обнаруживать тропический циклон и его центр.*

Мы активно **работаем** над улучшением точности нашей модели, одна их наших задач сегодня - это *ручная* разметка датасета для сегментации циклонов на [Roboflow](https://roboflow.com/).
<br></br>

![image](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/assets/104260621/9fc7a5cd-ca79-4f3a-b4de-70220a2fd12e)

<br></br>

### Обучение нейронной сети для сегментации:

---

Так же нами было проведено предварительное обучение на [датасете](https://universe.roboflow.com/sassuke-uchicha-6mbbd/cyclone-ieg77) сделанном нами и опубликованном на [Roboflow](https://roboflow.com/).

  

Мы активно работаем над улучшением качества датасета, а также количеством данных в нём.

  

Актуальный результат тестовой модели:

<br></br>

### *Входное изображение:*

<br></br>

![image](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/blob/main/first_stage/img/input_2.jpg)

<br></br>

### *Изображение на выходе:*

<br></br>

![image](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/blob/main/first_stage/img/output_2.jpg)

<br></br>

  

## Пример использования:

  

<details><summary>Первый этап</summary>

  

1. Установите библиотеки:

```bash

pip install ultralytics

pip install Pillow

pip install numpy

```

2. Откройте файл в папке `example`

  

для детекции:

```bash

detect.py

```

для сегментации:

```bash

segment.py

```

> В строке `results = model("")` в кавычках напишите путь к вашему изображению

3. Запустите файл.

4. Результат с предсказанием сохранится с именем:

## Использование обученной модели

Обученная модель имеет название `best.onnx`.

Скрипт для использования модели предоставлен в `solution.py`.

```bash

result.jpg

python solution.py путь_к_папке_с_изображениями

```

</details>

<details><summary>Второй этап</summary>

Второй этап работы над проектом представлен в папке [second_stage](https://github.com/pocketgodru/SiriusAI_detection_tropical_cyclone/tree/main/second_stage) этого репозитория.

</details>

# 📲Телеграмм бот

Для более удобного тестирования обученной модели предлагаем вам протестировать её в Телеграмме, используя бота, перейти к которому вы можете по [по этой ссылке](https://t.me/cyclone_detection_bot) или воспользоваться Qr-кодом:

> Данный пункт в скором времени дополнится

# 📩Обратная связь

Если у Вас есть вопросы обращайтесь на почту [project@dtcyclone.ru](mailto:project@dtcyclone.ru)
