from selene import browser
from selene import be, have



def test_yes(test_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Py'))



def test_no(test_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('nonoваыуа_ ваьл123654789@#^_^#@:)').press_enter()
    browser.element('[class="card-section"]').should(have.text('По этому запросу нет результатов! '))
