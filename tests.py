import pytest

from conftest import book_list
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_one_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Проверяем метод добавления книги')
        assert collector.books_genre == {'Проверяем метод добавления книги': ''}

    def test_set_book_genre_add_comedy_added(self):
        collector = BooksCollector()
        collector.books_genre['Книга для добавления жанра'] = ''
        collector.set_book_genre('Книга для добавления жанра', 'Комедии')
        assert collector.get_book_genre('Книга для добавления жанра') == 'Комедии'

    def test_get_book_genre_get_horror_added(self, book_list):
        collector = BooksCollector()
        collector.books_genre.update(book_list)
        assert collector.get_book_genre('Это ужасная книга 1') == 'Ужасы'

    @pytest.mark.parametrize(
        'genre, result', [
            ('Мультфильмы', ['Это мультфильмная книга 1', 'Это мультфильмная книга 2']),
            ('Фантастика', ['Это фантастическая книга 1', 'Это фантастическая книга 2']),
            ('Комедии', ['Это смешная книга 1', 'Это смешная книга 2']),
            ('Ужасы', ['Это ужасная книга 1', 'Это ужасная книга 2']),
            ('Детективы', ['Это детективная книга 1' , 'Это детективная книга 2'])
        ])
    def test_get_books_with_specific_genre_positive_test(self, genre, result, book_list):
        collector = BooksCollector()
        collector.books_genre.update(book_list)
        assert collector.get_books_with_specific_genre(genre) == result

    def test_get_books_genre_positive_test(self, book_list):
        collector = BooksCollector()
        collector.books_genre.update(book_list)
        assert collector.get_books_genre() == book_list

    def test_get_books_for_children_positive_test(self, book_list):
        collector = BooksCollector()
        collector.books_genre.update(book_list)
        assert collector.get_books_for_children() == [
        'Это фантастическая книга 1',
        'Это мультфильмная книга 1',
        'Это смешная книга 1',
        'Это фантастическая книга 2',
        'Это мультфильмная книга 2',
        'Это смешная книга 2']

    def test_add_book_in_favorites_add_one_book_added(self, book_list):
        collector = BooksCollector()
        collector.books_genre.update(book_list)
        collector.add_book_in_favorites('Это смешная книга 1')
        assert collector.favorites == ['Это смешная книга 1']

    def test_delete_book_from_favorites_remove_one_book_removed(self):
        collector = BooksCollector()
        collector.favorites = ['Книга для удаления из избранных']
        collector.delete_book_from_favorites('Книга для удаления из избранных')
        assert 'Книга для удаления из избранных' not in collector.favorites

    def test_delete_book_from_favorites_remove_book_not_in_favorites_no_change_in_favorites(self):
        collector = BooksCollector()
        collector.favorites = ['Книга есть избранных']
        collector.delete_book_from_favorites('Книги нет в избранных')
        assert collector.favorites == ['Книга есть избранных']

    def test_get_list_of_favorites_books_no_books_in_favorites_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []


