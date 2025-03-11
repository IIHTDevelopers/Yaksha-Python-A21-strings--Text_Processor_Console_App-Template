import pytest
import inspect
import importlib
from test.TestUtils import TestUtils
from text_processor import *

@pytest.fixture
def test_obj():
    return TestUtils()

def test_function_signatures(test_obj):
    """Test that the required function signatures are present"""
    try:
        # Import the module
        module = importlib.import_module("text_processor")
        
        # Check function definitions
        assert "def count_characters(text)" in inspect.getsource(module), "count_characters function is required"
        assert "def count_words(text)" in inspect.getsource(module), "count_words function is required"
        assert "def extract_substring(text, start, end)" in inspect.getsource(module), "extract_substring function is required"
        assert "def find_all_occurrences(text, substring)" in inspect.getsource(module), "find_all_occurrences function is required"
        assert "def replace_substring(text, old, new)" in inspect.getsource(module), "replace_substring function is required"
        assert "def split_text(text, delimiter=None)" in inspect.getsource(module), "split_text function is required"
        assert "def join_text(parts, delimiter=\"\")" in inspect.getsource(module), "join_text function is required"
        assert "def to_uppercase(text)" in inspect.getsource(module), "to_uppercase function is required"
        assert "def to_lowercase(text)" in inspect.getsource(module), "to_lowercase function is required"
        
        # Verify predefined texts in initialize_data
        plain_text, formatted_text, code_snippet, csv_data, json_data, log_entry, _, _, _, _, _ = initialize_data()
        assert "quick brown fox" in plain_text, "plain_text must contain correct content"
        assert "Name:" in formatted_text and "Age:" in formatted_text, "formatted_text must contain correct content"
        assert "def" in code_snippet and "print" in code_snippet, "code_snippet must contain correct content"
        assert "id,name,email" in csv_data, "csv_data must contain correct content"
        assert "users" in json_data and "name" in json_data, "json_data must contain correct content"
        assert "INFO" in log_entry and "login" in log_entry, "log_entry must contain correct content"
        
        test_obj.yakshaAssert("test_function_signatures", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_function_signatures", False, "functional")
        pytest.fail(f"Function signatures test failed: {str(e)}")

def test_string_operations(test_obj):
    """Test all string operations"""
    try:
        # Test basic string operations
        sample_text = "Hello, World! How are you today?"
        
        # Test character count
        assert count_characters(sample_text) == len(sample_text), "Character count should match string length"
        
        # Test word count
        assert count_words(sample_text) == 6, "Word count should be correct"
        
        # Test substring extraction
        assert extract_substring(sample_text, 0, 5) == "Hello", "Extract substring should return correct slice"
        assert extract_substring(sample_text, 7, 12) == "World", "Extract substring should handle middle slices"
        
        # Test find all occurrences
        assert find_all_occurrences("banana", "a") == [1, 3, 5], "Should find all occurrences of substring"
        assert find_all_occurrences("hello", "x") == [], "Should return empty list for non-existent substring"
        
        # Test replace substring
        assert replace_substring("hello world", "world", "there") == "hello there", "Should replace substring correctly"
        assert replace_substring("apple apple", "apple", "orange") == "orange orange", "Should replace all occurrences"
        
        # Test split text
        assert split_text("a,b,c", ",") == ["a", "b", "c"], "Should split text by delimiter"
        assert len(split_text("hello world")) == 2, "Should split by whitespace when delimiter is None"
        
        # Test join text
        assert join_text(["a", "b", "c"], ",") == "a,b,c", "Should join texts with delimiter"
        assert join_text(["hello", "world"]) == "helloworld", "Should join without delimiter when empty"
        
        # Test case conversion
        assert to_uppercase("hello") == "HELLO", "Should convert to uppercase"
        assert to_lowercase("HELLO") == "hello", "Should convert to lowercase"
        assert capitalize_text("hello world") == "Hello World", "Should capitalize first letter of each word"
        
        # Test whitespace handling
        assert strip_whitespace("  hello  ") == "hello", "Should strip whitespace"
        
        # Test palindrome detection
        assert is_palindrome("radar") == True, "Should identify palindrome correctly"
        assert is_palindrome("hello") == False, "Should identify non-palindrome correctly"
        assert is_palindrome("A man, a plan, a canal: Panama") == True, "Should handle complex palindromes"
        
        # Test vowel and consonant counting
        vowels, consonants = count_vowels_and_consonants("hello")
        assert vowels == 2, "Should count vowels correctly"
        assert consonants == 3, "Should count consonants correctly"
        
        # Test email extraction
        emails = extract_email_addresses("Contact us at support@example.com or info@test.com")
        assert "support@example.com" in emails, "Should extract email addresses"
        assert "info@test.com" in emails, "Should extract multiple email addresses"
        
        # Test date extraction
        dates = extract_dates("Meeting on 2023-05-15 and follow-up on 2023-06-30")
        assert "2023-05-15" in dates, "Should extract dates in yyyy-mm-dd format"
        assert "2023-06-30" in dates, "Should extract multiple dates"
        
        # Test CSV parsing
        csv_line = "id,name,email"
        assert parse_csv_line(csv_line) == ["id", "name", "email"], "Should parse CSV line correctly"
        
        # Test text table formatting
        headers = ["Name", "Age"]
        rows = [["John", "30"], ["Alice", "25"]]
        table = format_text_table(headers, rows)
        assert "Name" in table and "Age" in table, "Table should include headers"
        assert "John" in table and "Alice" in table, "Table should include row data"
        assert "-+-" in table, "Table should include separator line"
        
        test_obj.yakshaAssert("test_string_operations", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_string_operations", False, "functional")
        pytest.fail(f"String operations test failed: {str(e)}")

def test_implementation_techniques(test_obj):
    """Test implementation of string operation techniques"""
    try:
        # Check string operation implementations
        source = inspect.getsource(count_characters)
        assert "len(" in source, "count_characters should use len()"
        
        source = inspect.getsource(find_all_occurrences)
        assert ".find(" in source, "find_all_occurrences should use string find method"
        
        source = inspect.getsource(replace_substring)
        assert ".replace(" in source, "replace_substring should use string replace method"
        
        source = inspect.getsource(to_uppercase)
        assert ".upper(" in source, "to_uppercase should use string upper method"
        
        source = inspect.getsource(to_lowercase)
        assert ".lower(" in source, "to_lowercase should use string lower method"
        
        source = inspect.getsource(capitalize_text)
        assert ".title(" in source, "capitalize_text should use string title method"
        
        source = inspect.getsource(strip_whitespace)
        assert ".strip(" in source, "strip_whitespace should use string strip method"
        
        source = inspect.getsource(is_palindrome)
        assert "[::-1]" in source or "reversed(" in source, "is_palindrome should check reversed string"
        
        source = inspect.getsource(extract_substring)
        assert "[" in source and ":" in source and "]" in source, "extract_substring should use slicing"
        
        # Check immutability 
        original_text = "hello world"
        result = to_uppercase(original_text)
        assert original_text == "hello world", "Original string should not be modified"
        assert result == "HELLO WORLD", "New string should have correct transformation"
        
        test_obj.yakshaAssert("test_implementation_techniques", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_implementation_techniques", False, "functional")
        pytest.fail(f"Implementation techniques test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])