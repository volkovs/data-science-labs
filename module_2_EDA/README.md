# Описание работы

## Основные цели и задачи проекта

- Подготовка данных для дальнейшего анализа (очистка, приведение типов, исправление или исключение аномалий).
- Предварительный анализ данных (в том числе с использованием средств визуализации данных) с отбором свойств для дальнейшего построения модели (влияние внешних факторов на успеваемость по математике в старших классах).

## Краткая информация о данных

Влияние внешних факторов на успеваемость по математике в старших классах

## Этапы работы над проектом

1. Просмотр свойств данных
1. Переименование / нормализация названий свойств
1. Итеративное создание вспомогательных функций анализа и визуализации даннных
1. Анализ данных по каждому свойству:
    * Количество пустых значений
    * Количество уникальных значений
    * Количество уникальных значений с частотой более 10
    * Уникальные значения и их типы
    * Гистограмма
1. Анализ целевой метрики (бала успеваемости по математике)
    * Медиана
    * Перцентили и межперцинтильный размах
    * Границы аномалий
1. Удаление записей с аномалией в целевой метрике
1. Визуализация данных
    * Попарные графики свойств с попыткой нахождения зависимостей
    * Нахождения коеффициентов корелляции (для непрерывных свойств)
    * Графики распределения значений целевой метрики для каждого значения выбранного категориального свойства (повтор по всем категориальным свойствам).
1. Отбор свойств для модели
    * По коэффициенту корелляции `> 0.05` выбираем свойство `age`
    * По T-тесту статистически значимых различий (среди категориальных свойств) выбираем свойства: `address_type`, `mother_education`, `father_education`, `mother_job`, `father_job`, `study_time`, `failures`, `school_edu_support`, `go_out_time`, `score` 
    

Ответы на вопросы саморефлексии:

1. Какова была ваша роль в команде?

Я волк одиночка

2. Какой частью своей работы вы остались особенно довольны?

Частично доволен написанием макроса для унифицированного поколоночного анализа данных.

3. Что не получилось сделать так, как хотелось? Над чем ещё стоит поработать?

Над пониманием какие группы значений являются аномалиями или некорректной выборкой. Например возраст 20 лет существенно повышает средний бал. С одной стороны это может быть вызвано подготовкой к ЕГЭ (что влияет на результаты исследования именно внешних факторов, и в таком случае эту группу желательно исключить из исследования. Но тогда полученная модель не сможет предказывать бал для этой группы и было бы хорошо все таки включить группу обратно, но не ясно как это повлияет на результаты исследования). С другой стороны в этой группе находится всего три человека и неясно надо ли исключать эту группу в связи с некачественной выборкой, или все таки выборка отражает распределение учеников по возрасту... 

4. Что интересного и полезного вы узнали в этом модуле?

Про Т-тест.

5. Что является вашим главным результатом при прохождении этого проекта?

Записная книжка Юпитера, которая чертовски долго запускается :)

6. Какие навыки вы уже можете применить в текущей деятельности?

Пока не могу.

7. Планируете ли вы дополнительно изучать материалы по теме проекта?

Да. Учебник по статистике.