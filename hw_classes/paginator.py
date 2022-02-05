"""
https://www.codewars.com/kata/515bb423de843ea99400000a

Завершити написання класу PaginationHelper, який є корисний для запиту інформації зі списку по сторінках.
Цей клас приймає послідовність елементів та число, яке вказує на кількість елементів на одній сторінці.
class PaginationHelper:
   def __init__(self, collection, items_per_page):
       pass

   # Повертає загальну кількість елементів у колекції
   def item_count(self):
       pass

   # Повертає кількість сторінок
   def page_count(self):
       pass

   # Повертає кількість елементів на сторінці або -1 якщо такої сторіни немає
   def page_item_count(self, page_index):
       pass

   # Повертає номер сторінки на якій знаходиться цей елемент або -1 якщо елементу з таким індексом не існує
   def page_index(self, item_index):
       pass


Приклади застосування цього класу:
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid

"""

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        import math
        return math.ceil(self.item_count() / self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        return len(self.collection[page_index * self.items_per_page: (page_index + 1) * self.items_per_page]) or -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        import math

        if self.item_count() == 0 or self.item_count() - 1 < item_index or item_index < 0:
            return -1
        if item_index == 0:
            return 0
        return math.ceil(item_index / self.items_per_page) - 1


if __name__ == "__main__":
    collection = range(1, 25)
    helper = PaginationHelper(collection, 10)
    page_count = helper.page_count()
    page_index = helper.page_index(23)
    item_count = helper.item_count()
    assert page_count == 3, 'page_count is returning incorrect value.'
    assert page_index == 2, 'page_index returned incorrect value'
    assert item_count == 24, 'item_count returned incorrect value'
