import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},  # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# ------- Этап 1. Числа и math -------


def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, округлённую до одного знака."""
    return round(sum([movie["rating"] for movie in movies]) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (возраст самого старого, самого нового, средний).

    Средний возраст округляется вверх через math.ceil.
    """
    movies_ages = [current_year - movie["year"] for movie in movies]
    oldest_movie_age = max(movies_ages)
    newest_movie_age = min(movies_ages)
    average_age = math.ceil(sum(movies_ages) / len(movies_ages))
    return oldest_movie_age, newest_movie_age, average_age


def duration_in_hours(minutes):
    """Переводит минуты в строку вида "2ч 35м"."""
    return f"{minutes // 60}ч {minutes % 60}м"


# ------- Этап 2. Условия и match -------


def rating_tier(rating):
    """Возвращает категорию: шедевр (>=9), хорошо (7-8.9), средне (5-6.9), слабо."""
    if rating >= 9:
        result = "шедевр"
    elif rating >= 7:
        result = "хорошо"
    else:
        result = "средне" if rating >= 5 else "слабо"
    return result


def decade_label(year):
    """Возвращает метку года: новые (после 2020), недавние (2015-2020), старые."""
    match year:
        case _ if year > 2020:
            result = "новые"
        case _ if year >= 2015:
            result = "недавние"
        case _:
            result = "старые"
    return result


# ------- Этап 3. Циклы -------


def print_non_comedies(movies):
    """Печатает названия всех фильмов, которые не относятся к жанру comedy."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    """Печатает первый по порядку фильм с рейтингом выше 9.0."""
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Первый шедевр: {movies[i]['title']}")
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее threshold минут через накопительную переменную."""
    long_movies_counter = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            long_movies_counter += 1
    return long_movies_counter


# ------- Этап 4. Строки -------


def normalize_title(title):
    """Приводит название к Title Case без str.title()."""
    return " ".join([word[0].upper() + word[1:] for word in title.split()])


def make_slug(title):
    """Превращает название в слаг вида the-quiet-algorithm."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Возвращает строку с описанием фильма для отчёта."""
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f"{movie['rating']}/10, {duration_in_hours(movie['duration_min'])}, "
        f"жанры: {', '.join(sorted(movie['genres']))}"
    )


# ------- Этап 5. Списки -------


def titles_sorted_by_rating(movies):
    """Возвращает названия фильмов по убыванию рейтинга."""
    return [m["title"] for m in sorted(movies, key=lambda m: m["rating"], reverse=True)]


def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) с наибольшим рейтингом."""
    return sorted(
        [(movie["title"], movie["rating"]) for movie in movies],
        key=lambda m: m[1],
        reverse=True,
    )[:n]


# ------- Этап 6. Словари -------


def count_by_genre(movies):
    """Возвращает словарь {жанр: количество фильмов}."""
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    """Возвращает словарь {актёр: [названия фильмов]}."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, []) + [movie["title"]]
    return filmography


def above_average_ratings(movies):
    """Возвращает {title: rating} для фильмов с рейтингом выше среднего."""
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }


# ------- Этап 7. Множества -------


def all_genres(movies):
    """Возвращает множество всех уникальных жанров каталога."""
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """Возвращает множество актёров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры, которые есть в movies_a, но нет в movies_b."""
    return all_genres(movies_a) - all_genres(movies_b)


# ------- Этап 8. Итераторы и генераторы -------


def iter_high_rated(movies, min_rating=8.0):
    """Лениво отдаёт фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated(movies):
    """Печатает строки отчёта для фильмов из iter_high_rated."""
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def total_duration_high_rated(movies):
    """Считает суммарную длительность фильмов с рейтингом выше 7 (в минутах)."""
    return sum(m["duration_min"] for m in movies if m["rating"] > 7)


# ------- Этап 9. Итоговый отчёт -------


def build_report(movies):
    """Печатает итоговый отчёт по каталогу."""
    movies_by_title = {movie["title"]: movie for movie in movies}
    _, _, average_age = catalog_age_stats(movies)
    genre_counts = sorted(
        count_by_genre(movies).items(), key=lambda item: (-item[1], item[0])
    )

    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {average_age} лет")

    print("\nТоп-3 фильма:")
    for title, _ in top_n_by_rating(movies, 3):
        print(f"  {format_report_line(movies_by_title[title])}")

    print("\nФильмов по жанрам:")
    for genre, count in genre_counts:
        print(f"  {genre} — {count}")

    print(f"\nВсе жанры каталога: {', '.join(sorted(all_genres(movies)))}")


def demo(movies):
    """Демонстрирует функции этапов 3 и 8, которые печатают результат."""
    print("\nФильмы не жанра comedy:")
    print_non_comedies(movies)

    print("\nПоиск шедевра во всём каталоге:")
    find_first_masterpiece(movies)
    print("Поиск шедевра среди фильмов до 2020 года:")
    find_first_masterpiece([movie for movie in movies if movie["year"] < 2020])

    print(f"\nФильмов длиннее 120 минут: {count_long_movies(movies)}")

    print("\nФильмы с рейтингом от 8.0:")
    print_high_rated(movies)
    print(
        "Суммарная длительность фильмов с рейтингом выше 7: "
        f"{total_duration_high_rated(movies)} мин"
    )


if __name__ == "__main__":
    build_report(movies)
    demo(movies)
