from django.contrib import auth
from django import forms
from .models import Patient, Questionnaire


class LoginForm(auth.forms.AuthenticationForm):

    error_messages = {
        'invalid_login': 'Неверное имя пользователя или пароль.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_required_attribute = False
        self.fields['username'].widget.attrs.pop("autofocus", None)


class PatientCreateForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('fullname', 'gender', 'birthday', 'eyes_col', 'hair_col')
        labels = {
            'fullname': 'ФИО',
            'gender': 'Пол',
            'birthday': 'Дата рождения',
            'eyes_col': 'Цвет глаз',
            'hair_col': 'Цвет волос',
        }


class QuestionnaireCreateForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ("date_of_visit", "patient", "weight",
                  "growth", "freckles", "skin_col",
                  "redness_during_sunburn", "tanning_character", "rest_in_south",
                  "sunscreen_using", "neoplasm_appearance", "neoplasm_location",
                  "skin_tumors_in_fam", "elem_size", "elem_area",
                  "elem_borders", "elem_color", "inclusions", "elem_symmetry","neo_img","ref_img",
                  "doc_decision", "reappearance")
        labels = {
            'date_of_visit': 'Дата посещения',
            'patient': 'Пациент',
            'weight': 'Вес (кг)',
            'growth': 'Рост (см)',
            'freckles': 'Наличие веснушек',
            'skin_col': 'Оттенок кожи',
            'redness_during_sunburn': 'Краснеет ли кожа при загаре',
            'tanning_character': 'Загорает ли кожа',
            'rest_in_south': 'Как часто отдыхаете на юге',
            'sunscreen_using': 'Использование солнцезащитных средств',
            'neoplasm_appearance': 'Когда появилось новообразование',
            'neoplasm_location': 'Расположение новообразования',
            'skin_tumors_in_fam': 'Случаи кожных опухолей в семье',
            'elem_size': 'Размер элемента по оси X-Y (мм)',
            'elem_area': 'Общая площадь элемента (мм)',
            'elem_borders': 'Границы элемента',
            'elem_color': 'Преобладающий цвет элемента',
            'inclusions': 'Наличие включений',
            'elem_symmetry': 'Симметричность элемента',
            "neo_img" : 'Снимок новообразования',
            "ref_img" : 'Эталонный снимок',
            'doc_decision': 'Решение врача',
            'reappearance': 'Повторная явка',
        }
