import random
import string


def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += '!#$'

    if not characters:
        print("Ошибка: Не выбраны типы символов для использования.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    length = int(input("Введите длину пароля: "))
    use_lowercase = input("Использовать строчные буквы? (да/нет): ").lower() == 'да'
    use_uppercase = input("Использовать прописные буквы? (да/нет): ").lower() == 'да'
    use_digits = input("Использовать цифры? (да/нет): ").lower() == 'да'
    use_symbols = input("Использовать рандомизированные символы? (да/нет): ").lower() == 'да'

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
    if password:
        print("Сгенерированный пароль:", password)


if __name__ == "__main__":
    main()

