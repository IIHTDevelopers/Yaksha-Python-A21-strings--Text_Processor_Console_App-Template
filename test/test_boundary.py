import pytest
from test.TestUtils import TestUtils
from text_processor import *

@pytest.fixture
def test_obj():
    return TestUtils()

def test_boundary_scenarios(test_obj):
    """Test boundary scenarios for string operations"""
    try:
        # Test with empty strings
        empty_string = ""
        
        # Character and word counting with empty string
        assert count_characters(empty_string) == 0, "Character count of empty string should be 0"
        assert count_words(empty_string) == 0, "Word count of empty string should be 0"
        
        # Test with single character
        single_char = "a"
        assert count_characters(single_char) == 1, "Character count of single char should be 1"
        assert count_words(single_char) == 1, "Word count of single char should be 1"
        
        # Test substring extraction at boundaries
        text = "boundary"
        assert extract_substring(text, 0, 1) == "b", "First character extraction should work"
        assert extract_substring(text, 7, 8) == "y", "Last character extraction should work"
        
        # Test find all occurrences with single char
        assert find_all_occurrences("aaa", "a") == [0, 1, 2], "Should find all occurrences at every position"
        
        # Test with whitespace-only string
        whitespace = "   "
        assert strip_whitespace(whitespace) == "", "Stripping whitespace-only string should return empty string"
        assert count_words(whitespace) == 0, "Word count of whitespace-only string should be 0"
        
        # Test join with empty list
        assert join_text([], ",") == "", "Joining empty list should return empty string"
        
        # Test join with single element
        assert join_text(["single"], ",") == "single", "Joining single element should return that element"
        
        # Test split with empty string
        assert split_text("", ",") == [''], "Splitting empty string should return list with empty string"
        
        # Test palindrome with single character
        assert is_palindrome("a") == True, "Single character should be a palindrome"
        
        # Test vowel/consonant counting with empty string
        vowels, consonants = count_vowels_and_consonants("")
        assert vowels == 0 and consonants == 0, "Empty string should have 0 vowels and 0 consonants"
        
        # Test email extraction with no emails
        assert extract_email_addresses("No emails here") == [], "Should return empty list when no emails found"
        
        # Test date extraction with no dates
        assert extract_dates("No dates here") == [], "Should return empty list when no dates found"
        
        # Test with very long string
        long_string = "a" * 1000
        assert count_characters(long_string) == 1000, "Should handle very long strings"
        
        # Test format text table with minimal data
        min_headers = ["H"]
        min_rows = [["D"]]
        min_table = format_text_table(min_headers, min_rows)
        assert "H" in min_table and "D" in min_table, "Table formatting should work with minimal data"
        
        test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
        pytest.fail(f"Boundary scenarios test failed: {str(e)}")

def test_edge_case_handling(test_obj):
    """Test edge cases for string operations"""
    try:
        # Test with strings containing special characters
        special_chars = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/"
        
        # Should not throw exceptions with special characters
        count_characters(special_chars)
        count_words(special_chars)
        to_uppercase(special_chars)
        to_lowercase(special_chars)
        
        # Test with mixed whitespace - FIXED: Changed expected count to 5
        mixed_whitespace = "  word  another\t\tword\nyet\r\nanother"
        assert count_words(mixed_whitespace) == 5, "Should handle mixed whitespace correctly"
        
        # Test replace with special cases
        assert replace_substring("hello", "hello", "") == "", "Replacing entire string with empty string should work"
        assert replace_substring("aaa", "a", "b") == "bbb", "Replacing all occurrences should work"
        
        # Test substring extraction with same start and end
        assert extract_substring("test", 2, 2) == "", "Extraction with same start and end should return empty string"
        
        # Test palindrome with special cases
        assert is_palindrome("") == True, "Empty string should be considered a palindrome"
        assert is_palindrome("a") == True, "Single character should be a palindrome"
        assert is_palindrome(".,") == False, "Non-alphanumeric characters should be handled properly"
        
        # Test with strings containing numbers
        with_numbers = "abc123def"
        assert count_characters(with_numbers) == 9, "Should count numbers as characters"
        
        # Test email extraction edge cases
        almost_email = "user@domain"  # Missing TLD
        assert extract_email_addresses(almost_email) == [], "Should not extract incomplete emails"
        
        # Test date extraction edge cases
        almost_date = "2023-13-01"  # Invalid month
        valid_date = "2023-12-01"  # Valid date
        text_with_dates = f"{almost_date} and {valid_date}"
        dates = extract_dates(text_with_dates)
        assert almost_date not in dates, "Should not extract invalid dates"
        assert valid_date in dates, "Should extract valid dates"
        
        
        test_obj.yakshaAssert("TestEdgeCaseHandling", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestEdgeCaseHandling", False, "boundary")
        pytest.fail(f"Edge case handling test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])