import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# capitalize

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123", "123"),               
   ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),    
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected





# trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" 123", "123"),
    (" hello world", "hello world"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                     
    (" ", ""),                     
    ("skypro   ", "skypro   "),   
    ("   skypro   ", "skypro   "),
  ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [                  
    ("  skypro", "skypro"),   
  ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(None) == expected  # BUG-001 не обрабатывает None


# contains

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("Sky Pro", "Pro", True),                   
    ("123", "2", True),                     
    ("SkyPro", "", True),                   
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("Sky Pro", "s", False),        
    ("", "a", False),             
    (" ", "a", False),             
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected




# delete_symbol

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaabbbaaa", "a", "bbb"),
    ("aaa", "a", ""),
    ("123", "2", "13"),                     
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "Z", "SkyPro"),     
    ("", "a", ""),                
    (" ", "a", " "),              
    ("SkyPro", "s", "SkyPro"),     
    ("SkyPro", "", "SkyPro"),     
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


