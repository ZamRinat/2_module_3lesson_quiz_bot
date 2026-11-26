from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text

    def get_answer_id(self):
        return self.__answer_id

    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)

        for i, option in enumerate(i, self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(text=option, callback_data="correct"))
            else:
                markup.add(InlineKeyboardButton(text=option, callback_data="wrong"))
        return markup


# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "Спят", "Пишут мемы"),
    Question(
        "Как котики выражают свою любовь?",
        0,
        "Громким мурлыканием",
        "Отправляют фото на Instagram",
        "Гавкают",
    ),
    Question(
        "Какие книги котики любят читать?",
        3,
        "Обретение вашего внутреннего урр-мирения",
        "Тайм-менеджмент или как выделить 18 часов в день для сна",
        "101 способ уснуть на 5 минут раньше, чем хозяин",
        "Пособие по управлению людьми",
    ),
    Question(
        "Какая планета Солнечной системы самая большая?",
        2,
        "Земля",
        "Сатурн",
        "Юпитер",
        "Нептун",
    ),
    Question(
        "Сколько будет 7 × 8?",
        1,
        "54",
        "56",
        "64",
        "48",
    ),
    Question(
        "Кто написал роман «Мастер и Маргарита»?",
        0,
        "Михаил Булгаков",
        "Лев Толстой",
        "Фёдор Достоевский",
        "Антон Чехов",
    ),
    Question(
        "Какой язык программирования создал Гвидо ван Россум?",
        3,
        "Java",
        "C++",
        "Ruby",
        "Python",
    ),
    Question(
        "Какое животное является символом мудрости во многих культурах?",
        1,
        "Лев",
        "Сова",
        "Лиса",
        "Волк",
    ),
]
