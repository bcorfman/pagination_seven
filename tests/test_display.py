from paging.display import Pages


def test_display_selected_1_of_4_pages():
    pages = Pages(selected=1, total=4)
    assert pages.display() == '(1) 2 3 4'


def test_display_selected_3_of_5_pages():
    pages = Pages(selected=3, total=5)
    assert pages.display() == '1 2 (3) 4 5'


def test_display_selected_8_of_9_pages():
    pages = Pages(selected=8, total=9)
    assert pages.display() == '1 ... 5 6 7 (8) 9'


def test_display_selected_42_of_100_pages():
    pages = Pages(selected=42, total=100)
    assert pages.display() == '1 ... 41 (42) 43 ... 100'


def test_display_selected_5_of_9_pages():
    pages = Pages(selected=5, total=9)
    assert pages.display() == '1 ... 4 (5) 6 ... 9'


def test_display_selected_6_of_9_pages():
    pages = Pages(selected=6, total=9)
    assert pages.display() == '1 ... 5 (6) 7 8 9'


def test_display_selected_2_of_9_pages():
    pages = Pages(selected=2, total=9)
    assert pages.display() == '1 (2) 3 4 5 ... 9'


def test_display_selected_4_of_9_pages():
    pages = Pages(selected=4, total=9)
    assert pages.display() == '1 2 3 (4) 5 ... 9'
