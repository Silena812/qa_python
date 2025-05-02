# qa_python
тестирование метода add_new_book:
- test_add_new_book_add_one_book_added(self):  позитивная проверка добавления одной книги

тестирование метода set_book_genre:
- test_set_book_genre_add_comedy_added(self): позитивная проверка добавления жанра к существующей книге

тестирование метода get_book_genre:
- test_get_book_genre_get_horror_added(self, book_list): позитивная проверка определения жанра по названию существующей книги

тестирование метода get_books_with_specific_genre:
- test_get_books_with_specific_genre_positive_test(self, genre, result, book_list): позитивная проверка с использованием параметризации. Поиск книги по жанру.

тестирование метода get_books_genre:
- test_get_books_genre_positive_test(self, book_list): позитивная проверка списка книг в коллекции

тестирование метода get_books_for_children:
- test_get_books_for_children_positive_test(self, book_list): позитивная проверка списка книг без рейтинга

тестирование метода add_book_in_favorites:
- test_add_book_in_favorites_add_one_book_added(self, book_list): позитивная проверка добавления одной книги в избранные
        
тестирование метода delete_book_from_favorites:
- test_delete_book_from_favorites_remove_one_book_removed(self): позитивная проверка удаления существующей книги из избранных
- test_delete_book_from_favorites_remove_book_not_in_favorites_no_change_in_favorites(self): негативная проверка удаления несуществующей книги из избранных
        
тестирование метода get_list_of_favorites_books:
- test_get_list_of_favorites_books_no_books_in_favorites_empty_list(self): позитивная проверка пустого списка избранных книг
