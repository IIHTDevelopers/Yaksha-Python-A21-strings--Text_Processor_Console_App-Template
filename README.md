# System Requirements Specification
# Text Processing System (String Operations Focus)
Version 1.0

## TABLE OF CONTENTS

1. Project Abstract
2. Business Requirements
3. Constraints
   3.1 Input Requirements
   3.2 Operation Constraints
   3.3 Output Constraints
4. Template Code Structure
5. Execution Steps to Follow

## 1. PROJECT ABSTRACT

TextMaster Systems requires a comprehensive string processing application to manipulate, analyze, and format text data. The system will perform character-level operations, content extraction, transformation, and formatting functions on various text sources. This tool will enable users to work with plain text, structured data formats, and semi-structured content while demonstrating core string manipulation capabilities.

## 2. BUSINESS REQUIREMENTS

1. System needs to process different text formats (plain text, formatted text, code, CSV, JSON)
2. System must support basic text analysis operations (character counting, word counting, pattern detection)
3. Console should handle different string operations:
   - String slicing and indexing (accessing specific parts of text)
   - String methods (upper/lower case conversion, strip, join, split)
   - String analysis (palindrome detection, vowel/consonant counting)
   - Pattern extraction (email addresses, dates, urls)
   - Text formatting and tabulation

## 3. CONSTRAINTS

### 3.1 INPUT REQUIREMENTS

1. Text Data Types:
   - Must work with various text data types
   - Example: `plain_text = "The quick brown fox jumps over the lazy dog."`

2. Sample Datasets:
   - Must include these predefined text samples:
     - Plain text paragraph
     - Formatted text with newlines
     - Code snippet
     - CSV data
     - JSON data
     - Text with special characteristics (palindromes, whitespace, mixed case)

3. User Inputs:
   - Must handle user-provided text for processing
   - Must validate text inputs before operations

4. Sample Input Testing:
   - Must work with both predefined samples and custom inputs
   - Must allow selection between samples

### 3.2 OPERATION CONSTRAINTS

1. String Access:
   - Must use proper string indexing
   - Example: `char = text[index]` or `substring = text[start:end]`

2. String Iteration:
   - Must iterate through strings correctly
   - Example: `for char in text:` or `for i in range(len(text)):`

3. String Methods:
   - Must use standard string methods
   - Example: `upper()`, `lower()`, `strip()`, `split()`, `join()`, `replace()`

4. String Analysis:
   - Must use appropriate string operations for analysis
   - Example: `len(text)`, `text.count(substring)`, `text.find(substring)`

5. String Transformations:
   - Must implement case conversion, whitespace handling
   - Must handle replacements with proper validation

6. String Formatting:
   - Must use string formatting techniques
   - Example: `f-strings`, `.format()`, or template formatting

7. Error Handling:
   - Must validate text inputs and handle exceptions
   - Must handle invalid index access, empty inputs, None values

8. Immutability:
   - Must respect string immutability principles
   - Example: Creating new strings for results rather than trying to modify inputs

9. String Extraction:
   - Must implement substring extraction, pattern finding
   - Must extract emails and dates using string operations only

### 3.3 OUTPUT CONSTRAINTS

1. Display Format:
   - Show text analysis results with clear formatting
   - Display before/after states for transformations
   - Each analysis result must be displayed on a new line

2. Required Output Format:
   - Must show in this order:
     - Show "===== TEXT PROCESSING SYSTEM ====="
     - Show available samples
     - Display original text when showing results
     - Show "Text Analysis: {analysis_type}" before results
     - Format tables with proper alignment and separators

## 4. TEMPLATE CODE STRUCTURE

1. Data Management Functions:
   - `initialize_data()` - creates the initial text data samples

2. String Processing Functions:
   - `count_characters(text)` - counts total characters
   - `count_words(text)` - counts words in text
   - `extract_substring(text, start, end)` - extracts substring using slicing
   - `find_all_occurrences(text, substring)` - finds all occurrences of substring
   - `replace_substring(text, old, new)` - replaces substrings
   - `split_text(text, delimiter)` - splits text by delimiter
   - `join_text(parts, delimiter)` - joins text parts with delimiter
   - `to_uppercase(text)` - converts to uppercase
   - `to_lowercase(text)` - converts to lowercase
   - `capitalize_text(text)` - capitalizes words
   - `strip_whitespace(text)` - removes whitespace
   - `format_text_with_variables(template, **variables)` - formats with variables
   - `is_palindrome(text)` - checks if text is palindrome
   - `count_vowels_and_consonants(text)` - counts vowels and consonants
   - `extract_email_addresses(text)` - extracts emails using string methods
   - `extract_dates(text)` - extracts dates in yyyy-mm-dd format
   - `parse_csv_line(line)` - parses CSV line into fields
   - `format_text_table(headers, rows)` - formats text as table

3. Display Functions:
   - `display_text_analysis(text, analysis_type, result)` - displays analysis results

4. Program Control:
   - `main()` - main program function

## 5. EXECUTION STEPS TO FOLLOW

1. Run the program
2. View the main menu
3. Select operations:
   - Option 1: Basic Text Analysis
   - Option 2: Text Transformation
   - Option 3: Text Extraction
   - Option 4: Text Formatting
   - Option 5: Custom Text Input
   - Option 0: Exit
4. Perform operations on selected text
5. View results after each operation
6. Exit program when finished