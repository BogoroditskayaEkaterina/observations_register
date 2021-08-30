from django.db import models


class Patient(models.Model):
    GENDER_CHOICES = (('М', 'Мужской'), ('Ж', 'Женский'))
    EYES_CHOICES = (('Голубой', 'Голубой'), ('Серый', 'Серый'),
                    ('Зеленый', 'Зеленый'), ('Карий', 'Карий'))
    HAIR_CHOICES = (('Блондин', 'Блондин'), ('Рыжий', 'Рыжий'),
                    ('Темный', 'Темный'), ('Черный', 'Черный'))

    fullname = models.CharField(max_length=120)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    eyes_col = models.CharField(max_length=7, choices=EYES_CHOICES)
    hair_col = models.CharField(max_length=7, choices=HAIR_CHOICES)

    def __str__(self):
        return self.fullname

    def get_questionnaires(self):
        if not hasattr(self, '_questionnaires'):
            self._questionnaires = self.questionnaire_set.all()
        return self._questionnaires



class Questionnaire(models.Model):
    FRECKLES_CHOICES = (('Много', 'Много'), ('Умеренно', 'Умеренно'),
                        ('Единичные', 'Единичные'), ('Нет', 'Нет'))
    SKIN_CHOICES = (('Очень белый', 'Очень белый'), ('Белый', 'Белый'),
                    ('Светло-бежевый', 'Светло-бежевый'), ('Коричневый', 'Коричневый'),
                    ('Темно-коричневый', 'Темно-коричневый'))
    TANNING_CHOICES = (('Сильно сгорает', 'Сильно сгорает'), ('Умеренно сгорает', 'Умеренно сгорает'),
                       ('Иногда сгорает', 'Иногда сгорает'), ('Сгорает редко', 'Сгорает редко'),
                       ('Не сгорает', 'Не сгорает'))
    REST_CHOICES = (('10 дней в год', '10 дней в год'), ('20 дней в год', '20 дней в год'),
                    ('Больше 20 дней в год', 'Больше 20 дней в год'),
                    ('Не отдыхаю на юге', 'Не отдыхаю на юге'))
    NEO_APPEAR_CHOICES = (('Помню с детства', 'Помню с детства'), ('Недавно', 'Недавно'),
                          ('Не могу ответить', 'Не могу ответить'))
    NEO_LOC_CHOICES = (('Волосистая часть головы', 'Волосистая часть головы'), ('Лицо', 'Лицо'),
                       ('Шея', 'Шея'), ('Декольте', 'Декольте'),
                       ('Плечо', 'Плечо'), ('Предплечье', 'Предплечье'),
                       ('Кисть', 'Кисть'), ('Нижняя часть туловища', 'Нижняя часть туловища'),
                       ('Бедро', 'Бедро'), ('Голень', 'Голень'), ('Стопа', 'Стопа'))
    ELEM_BORDERS_CHOICES = (('Четкие', 'Четкие'), ('Нечеткие', 'Нечеткие'))
    ELEM_COLOR_CHOICES = (('Красный', 'Красный'), ('Бежевый', 'Бежевый'),
                          ('Коричневый', 'Коричневый'), ('Черный', 'Черный'))
    DOC_DECISION_CHOICES = (('Взять гистологическое исследование', 'Взять гистологическое исследование'),
                            ('Провести иссечение элемента', 'Провести иссечение элемента'))
    REAPPEARANCE_CHOICES = (('Без повторной явки', 'Без повторной явки'),
                            ('1 мес', '1 мес'), ('3 мес', '3 мес'),
                            ('6 мес', '6 мес'), ('1 год', '1 год'))


    #fields are required
    date_of_visit = models.DateField(auto_now=False, auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()
    growth = models.PositiveSmallIntegerField()
    freckles = models.CharField(max_length=9, choices=FRECKLES_CHOICES)
    skin_col = models.CharField(max_length=16, choices=SKIN_CHOICES)
    redness_during_sunburn = models.BooleanField()
    tanning_character = models.CharField(max_length=16, choices=TANNING_CHOICES)
    rest_in_south = models.CharField(max_length=20, choices=REST_CHOICES)
    sunscreen_using = models.BooleanField()
    neoplasm_appearance = models.CharField(max_length=16, choices=NEO_APPEAR_CHOICES)
    neoplasm_location = models.CharField(max_length=23, choices=NEO_LOC_CHOICES)
    skin_tumors_in_fam = models.BooleanField()

    #fields are optional
    elem_size = models.PositiveSmallIntegerField(null=True, blank=True)
    elem_area = models.PositiveSmallIntegerField(null=True, blank=True)
    elem_borders = models.CharField(max_length=8, choices=ELEM_BORDERS_CHOICES, null=True, blank=True)
    elem_color = models.CharField(max_length=10, choices=ELEM_COLOR_CHOICES, null=True, blank=True)
    inclusions = models.BooleanField(null=True, blank=True)
    elem_symmetry = models.BooleanField(null=True, blank=True)
    doc_decision = models.CharField(max_length=34, choices=DOC_DECISION_CHOICES, null=True, blank=True)
    reappearance = models.CharField(max_length=18, choices=REAPPEARANCE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.patient.fullname + " " + str(self.date_of_visit)

