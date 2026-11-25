from celery import shared_task
from .models import BookReading

@shared_task
def count_words_in_book(reading_id):
    reading = BookReading.objects.get(id=reading_id)
    # Считаем количество слов в тексте книги
    words_count = len(reading.text.split())
    print(f"В книге ID={reading_id} насчитано {words_count} слов.")
    return words_count