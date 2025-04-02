import sqlite3


def create_database():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        author TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("✅ База даних і таблиця Articles створені!")


def add_article():
    title = input("📝 Введіть назву статті: ").strip()
    content = input("📄 Введіть зміст статті: ").strip()
    author = input("✍️ Введіть автора статті: ").strip()

    if not title or not content or not author:
        print("❌ Помилка: усі поля мають бути заповнені!")
        return

    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Articles (title, content, author) VALUES (?, ?, ?)",
                       (title, content, author))
        conn.commit()
        print("✅ Статтю додано успішно!")
    except sqlite3.Error as e:
        print(f"❌ Помилка: {e}")

    conn.close()

    view_all_articles()  # Додаємо перегляд всіх статей після додавання


def delete_article():
    try:
        article_id = int(input("🗑 Введіть ID статті для видалення: "))
    except ValueError:
        print("❌ Помилка: ID має бути числом!")
        return

    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Articles WHERE id = ?", (article_id,))
    conn.commit()

    if cursor.rowcount:
        print(f"✅ Статтю з ID {article_id} видалено.")
    else:
        print(f"❌ Статтю з ID {article_id} не знайдено.")

    conn.close()


def view_article():
    try:
        article_id = int(input("🔍 Введіть ID статті для перегляду: "))
    except ValueError:
        print("❌ Помилка: ID має бути числом!")
        return

    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Articles WHERE id = ?", (article_id,))
    article = cursor.fetchone()

    if article:
        print("\n📖 Стаття:")
        print("───────────────────────────────")
        print(f"🆔 ID: {article[0]}")
        print(f"📌 Назва: {article[1]}")
        print(f"📄 Зміст: {article[2]}")
        print(f"✍️ Автор: {article[3]}")
        print("───────────────────────────────\n")
    else:
        print("❌ Статтю не знайдено!")

    conn.close()


def view_all_articles():
    """Функція для перегляду всіх статей"""
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Articles")
    articles = cursor.fetchall()

    if articles:
        print("\n📚 Усі статті в базі:")
        print("───────────────────────────────")
        for article in articles:
            print(f"🆔 ID: {article[0]}")
            print(f"📌 Назва: {article[1]}")
            print(f"📄 Зміст: {article[2]}")
            print(f"✍️ Автор: {article[3]}")
            print("───────────────────────────────")
    else:
        print("❌ У базі немає статей!")

    conn.close()


def main():
    create_database()

    while True:
        print("\n📚 Меню:")
        print("1️⃣ Додати статтю")
        print("2️⃣ Видалити статтю")
        print("3️⃣ Переглянути статтю")
        print("4️⃣ Переглянути всі статті")  # Додано новий пункт меню
        print("5️⃣ Вихід")

        choice = input("🔹 Виберіть опцію: ").strip()

        if choice == "1":
            add_article()
        elif choice == "2":
            delete_article()
        elif choice == "3":
            view_article()
        elif choice == "4":
            view_all_articles()
        elif choice == "5":
            print("👋 Вихід...")
            break
        else:
            print("❌ Невірний вибір, спробуйте ще раз!")


if __name__ == "__main__":
    main()
