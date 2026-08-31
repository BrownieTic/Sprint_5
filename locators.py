class TestDescriptionOfElements:
#Шапка
    # Конструктор
    button_header_constructor_selector = '.AppHeader_header__link__3D_hX'
    # Логотип
    button_header_logo_selector = '.AppHeader_header__logo__2D0X2'
    # Личный кабинет
    button_header_profile_selector = 'a[href*="/account"]'

#Страница регистрации
    # Поля для регистрации
    name_for_registration_path = './/label[text() = "Имя"]/following-sibling::input'
    login_for_registration_path = './/label[text() = "Email"]/following-sibling::input'
    password_for_registration_path = './/input[@name="Пароль"]'
    # Кнопка «Зарегистрироваться»
    button_register_path = './/button[text()="Зарегистрироваться"]'
    # Сообщение об ошибке с паролем
    password_erroror_registration_selector = '.input__error.text_type_main-default'
    button_input_from_registration_selector = 'a[href*="/login"]'

#Главная страница
    # Кнопка «Войти в аккаунт» на главной
    button_input_main_page_selector = '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg'
    # Кнопка Оформить заказ
    button_order_path = './/button[text()="Оформить заказ"]'
    # Раздел Булки
    button_buns_main_page_path = './/span[text()="Булки"]/parent::div'
    section_buns_main_page_path = './/h2[text()="Булки"]'
    # Раздел Соусы
    button_sauces_main_page_path = './/span[text()="Соусы"]/parent::div'
    section_sauces_main_page_path = './/h2[text()="Соусы"]'
    # Раздел Начинки
    button_fillings_main_page_path = './/span[text()="Начинки"]/parent::div'
    section_fillings_main_page_path = './/h2[text()="Начинки"]'

#Страница входа
    # Кнопка «Войти»
    button_input_page_input_path = './/button[text()="Войти"]'
    # Поля для входа
    login_for_input_page_input_name = 'name'
    password_for_input_page_input_name = 'Пароль'

#Страница восстановления пароля
    # Кнопка "Войти" в форме восстановления пароля
    button_input_password_recovery_form_selector = 'a[href*="/login"]'

#Страница профиля
    # Кнопка Выход
    button_out_profile_page_path = '//button[text()="Выход"]'
