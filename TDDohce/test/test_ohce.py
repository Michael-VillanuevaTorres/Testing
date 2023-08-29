import pytest

from app.ohce import *



def test_ohce():
    
    assert ohce1("ohce michael") == "Buenas tardes michael !"
    assert ohce1("ohce") == "echo"
    assert ohce1("oto") == "oto"+"\n"+"¡Bonita palabra!"
    assert ohce1("ohce michael") == "Buenas tardes michael !"
    assert ohce1("michael") == "leahcim"
