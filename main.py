class Students:
    def __init__(self, name,  age , height , weight, faculty , knowledge, strength, hobby, character, program_language, laptop):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.faculty = faculty
        self.knowledge = knowledge
        self.strength = strength
        self.hobby = hobby
        self.character = character
        self.program_language = program_language
        self.laptop = laptop
    def __str__(self):
        return f'Имя - {self.name}\n'\
               f'Возраст - {self.age}\n'\
               f'Рост - {self.height}\n'\
               f'Вес - {self.weight}\n'\
               f'Факультет - {self.faculty}\n'\
               f'Уровень знаний - {self.knowledge}\n'\
               f'Сила - {self.strength}\n'\
               f'Хобби - {self.hobby}\n'\
               f'Характер - {self.character}\n'\
               f'Язык программирования - {self.program_language}\n'\
               f'Ноутбук - {self.laptop}'
    def speak (self, language):
        return f'Языки - {language}'
    def live (self, place):
        return f'Место жительства - {place}'
print('-'*50)
Student_1 = Students('Айдар', 17, 170, 70, 'AIN-1-22', 'Отличный', 'Большая', 'Слушать музыку', 'Серьезный', 'python, HTML, CSS ','Есть')
print(Student_1)
print(Student_1.speak(str('Кыргызский, Русский, Английский, Немецкий')))
print(Student_1.live(str('Молдовановка')))
print('-'*50)
Student_2 = Students('Азиз', 18, 195, 63, 'AIN-1-22', 'Отличный', 'Средняя', 'Видеоигры, шахматы', 'Отзывчивый, ответственный', 'python, HTML, CSS ','Есть')
print(Student_2)
print(Student_2.speak(str('Кыргызский, Русский, Английский, Немецкий')))
print(Student_2.live(str('Бишкек')))
print('-'*50)
Student_3 = Students('Кыз Сайкал', 17, 160, 57, 'AIN-1-22', 'Отличный', 'Средняя', 'Волейбол, танцы, пение, рисование, программирование, математика, готовить еду, смотреть сериалы/аниме/фильмы, видеоигры', 'Веселый', 'python, HTML, CSS ','Есть')
print(Student_3)
print(Student_3.speak(str('Кыргызский, Русский, Английский, Немецкий')))
print(Student_3.live(str('Бишкек')))
print('-'*50)
#Сайкал попросила добавить ВСЕ ее хобби
Student_4 = Students('Султанбек', 17, 175, 55, 'AIN-1-22', 'Отличный', 'Средняя', 'Программирование', 'Спокойный', 'python, HTML, CSS ','Есть')
print(Student_4)
print(Student_4.speak(str('Кыргызский, Русский, Английский, Немецкий')))
print(Student_4.live(str('Бишкек')))
print('-'*50)
Student_5 = Students('Санжар', 18, 170 , 50, 'AIN-1-22', 'Отличный','Средняя','Слушать музыку, шахматы, турники','Спокойный','python, HTML, CSS ','Есть')
print(Student_5)
print(Student_5.speak(str('Кыргызский, Русский, Английский, Немецкий')))
print(Student_5.live(str('Бишкек')))
print('-'*50)
class Pupils(Students):
    def __init__(self, name,  age , height , weight, faculty , knowledge, strength, hobby, character, program_language, laptop, school, grade, marks, test, examination, university):
        super().__init__(name,  age , height , weight, faculty , knowledge, strength, hobby, character, program_language, laptop)
        self.grade = grade
        self.school = school
        self.marks = marks
        self.test = test
        self.examination = examination
        self.university = university
    def __str__(self):
        return super(Pupils, self).__str__() + f'\nКласс - {self.grade}\n' \
                                               f'Школа - {self.school}\n'\
                                               f'Оценки - {self.marks}\n'\
                                               f'ОРТ-тестирование (в этом году) - {self.test}\n'\
                                               f'Экзамены (в этом году) - {self.examination}\n'\
                                               f'Выбор университета - {self.university}\n'
    def speak (self, language):
        return f'Языки - {language}'
    def live (self, place):
        return f'Место жительства - {place}'
    def visit (self, extraclasses):
        return f'Дополнительные курсы - {extraclasses}'
    def participate (self, olympiads):
        return f'Участие в олимпиадах - {olympiads}'
print('-'*50)
Pupil_1 = Pupils('Асан', 14, 160, 55, 'None', 'Хороший', 'Большая', 'Воркаут', 'Эмоциональный', 'C#','Нет', 8, 'ИШГ-№1',4 , 'нет', 'нет', 'Ала-Тоо')
print(Pupil_1)
print(Pupil_1.speak(str('Кыргызский, Русский, Английский')))
print(Pupil_1.live(str('Каракол')))
print(Pupil_1.visit(str('Дзюдо')))
print(Pupil_1.participate(str('Нет')))
print('-'*50)
Pupil_2 = Pupils('Берниза', 17, 157, 49, 'None', 'Средний', 'Средняя', 'Готовить еду', 'Веселая', 'python','Нет', 11, 'школа им. Гейдара Алиева',4 , 'да', 'да', 'КГМА')
print(Pupil_2)
print(Pupil_2.speak(str('Кыргызский, Русский')))
print(Pupil_2.live(str('Бишкек')))
print(Pupil_2.visit(str('Гимнастика')))
print(Pupil_2.participate(str('Да')))
print('-'*50)
Pupil_3 = Pupils('Даниэль', 16, 180, 78, 'None', 'Плохой', 'Огромная', 'Бокс', 'Взрывной', 'None','Нет', 10, 'школа им.Мамакеева',3 , 'нет', 'нет', 'Манас')
print(Pupil_3)
print(Pupil_3.speak(str('Кыргызский, Русский')))
print(Pupil_3.live(str('Ак-Суу')))
print(Pupil_3.visit(str('Бокс')))
print(Pupil_3.participate(str('Нет')))
print('-'*50)
Pupil_4 = Pupils('Жаныбек', 17, 178, 60, 'None', 'Выше среднего', 'Большая', 'Играть на пианино', 'Отзывчивый', 'pascal ABC','Нет', 11, 'школа им. Пржевальского',4 , 'да', 'да', 'КГТУ')
print(Pupil_4)
print(Pupil_4.speak(str('Кыргызский, Русский, Немецкий')))
print(Pupil_4.live(str('Каракол')))
print(Pupil_4.visit(str('Плавание')))
print(Pupil_4.participate(str('Нет')))
print('-'*50)
Pupil_5 = Pupils('Аделя', 15, 165 , 50, 'None', 'Отличный', 'Слабая', 'Чтение', 'Спокойный', 'python, JavaScrypt', 'Нет', 9, 'Школа №61',5 , 'нет', 'да', 'АУЦА')
print(Pupil_5)
print(Pupil_5.speak(str('Кыргызский, Русский, Английский')))
print(Pupil_5.live(str('Бишкек')))
print(Pupil_5.visit(str('Английский')))
print(Pupil_5.participate(str('Да')))
print('-'*50)
class Graduates(Students):
    def __init__(self, name,  age , height , weight, faculty , knowledge, strength, hobby, character, program_language, laptop, university, science):
        super().__init__(name,  age , height , weight, faculty , knowledge, strength, hobby, character, program_language, laptop)
        self.university = university
        self.science = science
    def __str__(self):
        return super(Graduates, self).__str__() + f'\nКакой университет окончили - {self.university}\n'\
                                               f'Сфера науки - {self.science}\n'
    def speak (self, language):
        return f'Языки - {language}'
    def live (self, place):
        return f'Нынешняя страна проживания - {place}'
    def family (self, family):
        return f'Семья - {family}'
    def work (self, job):
        return f'Работа - {job}'
print('-'*50)
Graduate_1 = Graduates('Евгений', 24, 180, 80, 'None', 'Очень высокий', 'Большая', 'Слушать музыку', 'Веселый', 'python, C++, Java, PHP', 'Да', 'УЦА', 'Философия')
print(Graduate_1)
print(Graduate_1.speak(str('Русский, Английский, Испанский')))
print(Graduate_1.live(str('США')))
print(Graduate_1.family(str('Нет')))
print(Graduate_1.work(str('Да')))
print('-'*50)
Graduate_2 = Graduates('Руслан', 23, 185, 78, 'None', 'Очень высокий', 'Большая', 'Чтение, спорт', 'Спокойный', 'python, Java, HTML, CSS', 'Да', 'КГИПИ', 'Компьютерная инженерия')
print(Graduate_2)
print(Graduate_2.speak(str('Кыргызский, Русский, Английский, Немецкий')))
print(Graduate_2.live(str('Германия')))
print(Graduate_2.family(str('Нет')))
print(Graduate_2.work(str('Да')))
print('-'*50)
Graduate_3 = Graduates('Жанара', 25, 170, 60, 'None', 'Очень высокий', 'Средняя', 'Изучение языков', 'Серьезная', 'python, HTML , CSS , Javascrypt', 'Да', 'КГТУ', 'Математика')
print(Graduate_3)
print(Graduate_3.speak(str('Кыргызский, Русский, Английский, Немецкий, Фрацузский, Итальянский')))
print(Graduate_3.live(str('Швейцария')))
print(Graduate_3.family(str('Да')))
print(Graduate_3.work(str('Нет')))
print('-'*50)
