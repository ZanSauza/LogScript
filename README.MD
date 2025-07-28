# LogScript
## скрипт для обработки лог-файла

```
Скрипт читает файл и формирует отчет со списком эндпоинтов, 
количеством запросов по каждому эндпоинту и средним временем ответа. 
Пути к файлам и название отчета передаются как параметры, 
например python main.py --file file.log --report average.
```



## примеры комманд:
### Формирует среднее время ответа по каждому эндпоинту
`python main.py --file example1.log --report average`
![img1.PNG](screenshots/img1.PNG)
### Формирует среднее время ответа по каждому эндпоинту по указанной дате
`python main.py --file example1.log --report average --date 2025-22-06`
![img2.PNG](screenshots/img2.PNG)
### тоже самое но другой файл
`python main.py --file example2.log --report average --date 2025-24-06`
![img3.PNG](screenshots/img3.PNG)
### если дата указана неверно 
`python main.py --file example1.log --report average --date 2025-23-08`
![img4.PNG](screenshots/img4.PNG)
### в задании было указано что можно дополнительно сделать так что бы в архитектуру была заложена возможность быстрого добавления новых отчётов. Я реализовал это с помощью абстрактных классов, здесь я просто на примере показал что это можно сделать, то же самое можно реализовать с другими отчетами
`python main.py --file example1.log --user agent --date 2025-22-06`
![img8.PNG](screenshots/img8.PNG)
### другой файл
`python main.py --file example2.log --user agent --date 2025-23-06`
![img7.PNG](screenshots/img7.PNG)

