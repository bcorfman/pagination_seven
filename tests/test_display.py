from paging.display import PageList


def test_display_1_of_4_pages():
    lst = PageList(1, 4)
    assert lst.display() == '(1) 2 3 4'


def test_display_3_of_5_pages():
    lst = PageList(3, 5)
    assert lst.display() == '1 2 (3) 4 5'
