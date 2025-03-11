import pytest
from test.TestUtils import TestUtils
from text_processor import *

@pytest.fixture
def test_obj():
    return TestUtils()

def test_input_validation(test_obj):
    """Test input validation and error handling for None values"""
    try:
        # Test with None inputs for critical functions
        functions_to_test = [
            (count_characters, [None]),
            (count_words, [None]),
            (extract_substring, [None, 0, 5]),
            (extract_substring, ["text", None, 5]),
            (extract_substring, ["text", 0, None]),
            (find_all_occurrences, [None, "substring"]),
            (find_all_occurrences, ["text", None]),
            (replace_substring, [None, "old", "new"]),
            (replace_substring, ["text", None, "new"]),
            (replace_substring, ["text", "old", None]),
            (split_text, [None]),
            (join_text, [None]),
            (to_uppercase, [None]),
            (to_lowercase, [None]),
            (capitalize_text, [None]),
            (strip_whitespace, [None]),
            (is_palindrome, [None]),
            (count_vowels_and_consonants, [None]),
            (extract_email_addresses, [None]),
            (extract_dates, [None]),
            (parse_csv_line, [None]),
            (format_text_with_variables, [None])
        ]
        
        # Test all functions with None inputs
        for func, args in functions_to_test:
            with pytest.raises(ValueError):
                func(*args)
        
        # Test with invalid parameter values
        # Test substring extraction with invalid indices
        with pytest.raises(ValueError):
            extract_substring("test", -1, 3)  # Negative start
        
        with pytest.raises(ValueError):
            extract_substring("test", 0, 10)  # End beyond length
        
        with pytest.raises(ValueError):
            extract_substring("test", 3, 1)  # Start > end
        
        # Test find_all_occurrences with empty substring
        with pytest.raises(ValueError):
            find_all_occurrences("test", "")
        
        # Test replace_substring with empty old string
        with pytest.raises(ValueError):
            replace_substring("test", "", "replacement")
        
        # Test format_text_with_variables with missing variables
        with pytest.raises(ValueError):
            format_text_with_variables("Hello, {name}!")  # Missing 'name' variable
        
        test_obj.yakshaAssert("TestInputValidation", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInputValidation", False, "exception")
        pytest.fail(f"Input validation test failed: {str(e)}")

def test_error_handling(test_obj):
    """Test specific error handling scenarios"""
    try:
        # Test handling invalid indices
        sample_text = "hello"
        
        # String index out of range
        with pytest.raises(ValueError):
            extract_substring(sample_text, 10, 15)
        
        # Test with invalid data types
        with pytest.raises(ValueError):
            extract_substring(sample_text, "start", 3)  # Wrong type for start
        
        with pytest.raises(ValueError):
            extract_substring(sample_text, 0, "end")  # Wrong type for end
        
        # Test immutability - original string should not change
        original_text = "hello world"
        result = to_uppercase(original_text)
        assert original_text == "hello world", "Original string should not be modified"
        assert result == "HELLO WORLD", "New string should have correct transformation"
        
        # Test with non-string inputs
        with pytest.raises(AttributeError, match=".*'int' object has no attribute.*"):
            to_uppercase(123)  # Integer should cause AttributeError
        
        # Test CSV line with inconsistent data
        csv_headers = ["id", "name", "email"]
        csv_rows = [
            ["1", "John", "john@example.com"],
            ["2", "Alice"]  # Missing email - should raise exception in format_text_table
        ]
        
        # Ensure format_text_table handles rows with different lengths
        with pytest.raises(ValueError):
            format_text_table(csv_headers, csv_rows)
        
        # Test format_text_with_variables with correct usage
        template = "Hello, {name}! You are {age} years old."
        formatted = format_text_with_variables(template, name="John", age=30)
        assert formatted == "Hello, John! You are 30 years old.", "Variable formatting should work correctly"
        
        test_obj.yakshaAssert("TestErrorHandling", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestErrorHandling", False, "exception")
        pytest.fail(f"Error handling test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])