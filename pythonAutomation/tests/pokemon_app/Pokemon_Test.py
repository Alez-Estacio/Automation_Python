import sys

# setting path
sys.path.append('../python_automation_with_pokemon')

from business_logic.api.PokemonLogic import PokemonLogic
from support_classes.browser_factory import BrowserFactory
from business_logic.ui.MainPage import MainPageLogic
from business_logic.ui.NationalDexPage import NationalDexPage
from support_classes.system_enums import TargetBrowser


def test_exampleForAPI():
    apiLogic = PokemonLogic()
    pkNumber: int = apiLogic.ReturnNumberOfPokemonWithThisName("Pikachu")
    pkName: str = apiLogic.ReturnNameOfPokemonWithThisNumber(25)
    assert pkNumber == 25
    assert pkName == "pikachu"



def test_exampleForUI():
    browserClass = BrowserFactory()
    browserClass.SetBrowserByEnum(TargetBrowser.Chrome)
    browserClass.MaximizeBrowser()
    browserClass.NavigateToThisPage("https://pokemondb.net/")

    mainPage = MainPageLogic(browserClass.driver)
    mainPage.NavigateToPokedexFromQuickLinksMenu()

    nationPage = NationalDexPage(browserClass.driver)
    namePresent: bool = nationPage.DoesAPokemonWithThisNameExist("Pikachu")
    numPresent: bool = nationPage.DoesAPokemonWithThisNumberExist(25)
    name: str = nationPage.ReturnNameOfPokemonWithThisNumber(25)
    dexNum: int = nationPage.ReturnNumberOfPokemonWithThisName("Pikachu")
    assert namePresent == True
    assert numPresent == True
    assert name == "Pikachu"
    assert dexNum == 25

