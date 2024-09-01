from pyo3_rattler_build import sum_as_string

def test_core():
    assert "2" == sum_as_string(1, 1)
    
