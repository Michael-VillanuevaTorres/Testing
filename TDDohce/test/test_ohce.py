import pytest

from app.ohce import *



def test_ohce():
    
    assert ohce("ohce michael") == "Buenas tardes michael !"
def test_palabra():
    assert ohce("ohce") == "echo"
    assert ohce("ohw") == "who"
def test_palindromo():
    assert ohce("oto") == "oto"+"\n"+"¡Bonita palabra!"
def test_Stop():
    assert ohce("Stop!") == "Adios michael"

