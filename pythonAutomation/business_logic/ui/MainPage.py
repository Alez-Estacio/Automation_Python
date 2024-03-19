import sys
# setting path
sys.path.append('../python_automation_with_pokemon')

from ui_elements.pokemon_app.MainPage import ReturnMenuElements
from support_classes.browser_factory import  BrowserFactory

class MainPageLogic:

    name: str = ""
    brFactory = ""

    def __init__(self, wDriver):
        self.name = "NoName"
        self.brFactory = BrowserFactory()
        self.brFactory.driver = wDriver


    def NavigateToPokedexFromQuickLinksMenu(self):
        selectorData = ReturnMenuElements()["NATIONAL_DEX_LINK"]
        testElements = self.brFactory.SearchElements(selectorData["format"], selectorData["selector"], 1, 5, True)
        if len(testElements) != 1:
            print("Function NavigateToPokedexFromQuickLinksMenu() failed because element was invalid")
        else:
            testElements[0].click()


