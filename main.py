# домашній номер телефону (тільки цифри та довжина номера)
# def validate_home_phone(phone_number):
#     return phone_number.isdigit() and 1 <= len(phone_number) <= 15
#
# Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# def validate_mobile_phone(phone_number):
#     return phone_number.replace("+", "").isdigit() and 1 <= len(phone_number) <= 15
#
# Email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# def validate_email(email):
#      return "@" in email and email.count("@") == 1 and email.endswith("gmail.com") and 5 <= len(email) <= 30
#
# ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
# def validate_full_name(full_name):
#         names = full_name.split()
#     return len(names) == 3 and all(2 <= len(name) <= 20 for name in names)
#
# Пароль (мінімально: одна велика літера, одна маленька літера,
# #     одна цифра, один символ, довжина пароля – від 8 до 16 символів)
# def validate_password(password):
#          return any(c.isupper() for c in password) and any(c.islower() for c in password) \
#            and any(c.isdigit() for c in password) and any(c in "@$!%*?&" for c in password) \
#            and 8 <= len(password) <= 16
