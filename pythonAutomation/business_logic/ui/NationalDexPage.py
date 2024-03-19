import sys
# setting path
sys.path.append('../python_automation_with_pokemon')

from ui_elements.pokemon_app.NationalDexPage import NationalDex_ListPokemon
from support_classes.browser_factory import BrowserFactory

class NationalDexPage:

    name: str = ""
    brFactory = ""

    def __init__(self, wDriver):
        self.name = "NoName"
        self.brFactory = BrowserFactory()
        self.brFactory.driver = wDriver


    def DoesAPokemonWithThisNameExist(self, targetName: str):
        exist: bool = False
        selectorData = NationalDex_ListPokemon()["POKEMON_NAME_LINK"]
        testElements = self.brFactory.SearchElements(selectorData["format"], selectorData["selector"], 1, 5, True)
        amount: int = len(testElements)
        index: int = 0
        while index <= (amount-1):
            pkLabel: str = testElements[index].text
            if pkLabel == targetName:
                exist = True
                break
            index = index + 1
        return exist


    def DoesAPokemonWithThisNumberExist(self, targetNumber: int):
        exist: bool = False
        stringNumber: str = "#"+self.FormatNumber(targetNumber)
        selectorData = NationalDex_ListPokemon()["POKEMON_NUMBER_LABEL"]
        testElements = self.brFactory.SearchElements(selectorData["format"], selectorData["selector"], 1, 5, True)
        amount: int = len(testElements)
        index: int = 0
        while index <= (amount-1):
            pkLabel: str = testElements[index].text
            if pkLabel == stringNumber:
                exist = True
                break
            index = index + 1
        return exist


    def ReturnNameOfPokemonWithThisNumber(self, pkNumber: int):
        name: str = ""
        exist: bool = self.DoesAPokemonWithThisNumberExist(pkNumber)
        if exist:
            selectorData = NationalDex_ListPokemon()["POKEMON_NAME_LINK"]
            testElements = self.brFactory.SearchElements(selectorData["format"], selectorData["selector"], 1, 5, True)
            index: int = pkNumber - 1
            name = testElements[index].text
        else:
            print("ReturnNameOfPokemonWithThisNumber() could not find Name of Pokemon with Number: " + pkNumber)
        return name


    def ReturnNumberOfPokemonWithThisName(self, pkName: str):
        pkNumber: int = -1
        exist: bool = self.DoesAPokemonWithThisNameExist(pkName)
        if exist:
            selectorData = NationalDex_ListPokemon()["POKEMON_NAME_LINK"]
            testElements = self.brFactory.SearchElements(selectorData["format"], selectorData["selector"], 1, 5, True)
            amount: int = len(testElements)
            index: int = 0
            while index < (amount-1):
                locName: str = testElements[index].text
                if locName == pkName:
                    pkNumber = index + 1
                    break
                index = index + 1
        else:
            print("ReturnNumberOfPokemonWithThisName() could not find Name of Pokemon with Name: " + pkName)
        return pkNumber


    def LoadDetailPageOfPokemonWithThisName(self, pkName: str):
        exist: bool = self.DoesAPokemonWithThisNameExist(pkName)
        if exist:
            number: int = self.ReturnNumberOfPokemonWithThisName(pkName)
            selectorData = NationalDex_ListPokemon()["POKEMON_NAME_LINK"]
            testElements = self.brFactory.SearchElements(selectorData["format"], selectorData["selector"], 1, 5, True)
            testElements[number-1].click()
        else:
            print("LoadDetailPageOfPokemonWithThisName() could not find Name of Pokemon with Name: " + pkName)



    def FormatNumber(self, targetNumber: int):
        stringNumber: str = ""
        if targetNumber > 1 and targetNumber <= 9:
            stringNumber = "00" + str(targetNumber)
        elif targetNumber > 10 and targetNumber <= 99:
            stringNumber = "0"+str(targetNumber)
        elif targetNumber > 99:
            stringNumber = str(targetNumber)
        return stringNumber

