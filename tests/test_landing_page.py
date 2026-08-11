from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Welcome to AceReads")


def test_has_header_books(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    books = page.locator("li")

    expected_value = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott'
    ]

    actual_value = books.all_inner_texts()
    assert actual_value == expected_value


def test_create_new_book(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"