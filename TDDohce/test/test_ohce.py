import pytest

from app.ohce import *



def test_ohce():
    
    assert ohce("ohce michael") == "Buenas tardes michael !"
    assert ohce("ohce") == "echo"
    assert ohce("ohw") == "who"
    assert ohce("oto") == "oto"+"\n"+"¡Bonita palabra!"
