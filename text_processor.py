"""
Text Processing System
This program demonstrates string operations, slicing, and methods through text processing.
"""

def initialize_data():
    """
    Initialize the text data with predefined strings.
    
    Returns:
        tuple: A tuple containing text data examples
    """
    # Create sample texts
    plain_text = "The quick brown fox jumps over the lazy dog."
    formatted_text = "Name: John Doe\nAge: 30\nOccupation: Software Engineer"
    code_snippet = "def hello_world():\n    print('Hello, World!')\n\nhello_world()"
    csv_data = "id,name,email,department\n1,Alice,alice@example.com,Engineering\n2,Bob,bob@example.com,Marketing\n3,Carol,carol@example.com,Finance"
    json_data = '{"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Carol"}]}'
    log_entry = "[2023-03-15 08:45:32] INFO: User login successful - username=admin"
    
    # Create text samples with special characteristics
    palindrome = "A man, a plan, a canal: Panama"
    whitespace_text = "    This text has    irregular spacing    "
    mixed_case = "ThIs TeXt HaS mIxEd CaSe"
    with_numbers = "There are 3 apples, 5 oranges, and 10 bananas"
    url = "https://www.example.com/path/to/resource?param1=value1&param2=value2"
    
    return (plain_text, formatted_text, code_snippet, csv_data, json_data, 
            log_entry, palindrome, whitespace_text, mixed_case, with_numbers, url)

def count_characters(text):
    """
    Count the number of characters in the text.
    
    Args:
        text (str): Text to analyze
    
    Returns:
        int: Number of characters
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    return len(text)

def count_words(text):
    """
    Count the number of words in the text.
    
    Args:
        text (str): Text to analyze
    
    Returns:
        int: Number of words
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    # Split by whitespace and count non-empty words
    words = [word for word in text.split() if word]
    return len(words)

def extract_substring(text, start, end):
    """
    Extract a substring using slicing.
    
    Args:
        text (str): Text to slice
        start (int): Starting index
        end (int): Ending index
    
    Returns:
        str: Extracted substring
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end must be integers")
    
    if start < 0 or start >= len(text):
        raise ValueError(f"Start index {start} out of range")
    
    if end < 0 or end > len(text):
        raise ValueError(f"End index {end} out of range")
    
    if start > end:
        raise ValueError("Start index must be less than or equal to end index")
    
    return text[start:end]

def find_all_occurrences(text, substring):
    """
    Find all occurrences of a substring in the text.
    
    Args:
        text (str): Text to search in
        substring (str): Substring to find
    
    Returns:
        list: List of starting indices of all occurrences
    """
    if text is None or substring is None:
        raise ValueError("Text and substring cannot be None")
    
    if not substring:
        raise ValueError("Substring cannot be empty")
    
    positions = []
    start = 0
    
    while True:
        pos = text.find(substring, start)
        if pos == -1:  # No more occurrences
            break
        positions.append(pos)
        start = pos + 1  # Continue search from next position
    
    return positions

def replace_substring(text, old, new):
    """
    Replace all occurrences of a substring.
    
    Args:
        text (str): Text to modify
        old (str): Substring to replace
        new (str): Replacement string
    
    Returns:
        str: Text with replacements
    """
    if text is None or old is None or new is None:
        raise ValueError("Text, old, and new values cannot be None")
    
    if not old:
        raise ValueError("Old substring cannot be empty")
    
    return text.replace(old, new)

def split_text(text, delimiter=None):
    """
    Split text using a delimiter.
    
    Args:
        text (str): Text to split
        delimiter (str, optional): Delimiter to use. Defaults to None (whitespace).
    
    Returns:
        list: List of text parts
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    return text.split(delimiter)

def join_text(parts, delimiter=""):
    """
    Join text parts using a delimiter.
    
    Args:
        parts (list): Text parts to join
        delimiter (str, optional): Delimiter to use. Defaults to "".
    
    Returns:
        str: Joined text
    """
    if parts is None:
        raise ValueError("Parts list cannot be None")
    
    return delimiter.join(parts)

def to_uppercase(text):
    """
    Convert text to uppercase.
    
    Args:
        text (str): Text to convert
    
    Returns:
        str: Uppercase text
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    return text.upper()

def to_lowercase(text):
    """
    Convert text to lowercase.
    
    Args:
        text (str): Text to convert
    
    Returns:
        str: Lowercase text
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    return text.lower()

def capitalize_text(text):
    """
    Capitalize the first character of each word.
    
    Args:
        text (str): Text to capitalize
    
    Returns:
        str: Capitalized text
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    return text.title()

def strip_whitespace(text):
    """
    Remove leading and trailing whitespace.
    
    Args:
        text (str): Text to strip
    
    Returns:
        str: Stripped text
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    return text.strip()

def format_text_with_variables(template, **variables):
    """
    Format text using variable substitution.
    
    Args:
        template (str): Template text with placeholders
        **variables: Variable keyword arguments to substitute
    
    Returns:
        str: Formatted text
    """
    if template is None:
        raise ValueError("Template cannot be None")
    
    try:
        return template.format(**variables)
    except KeyError as e:
        raise ValueError(f"Missing required variable: {e}")

def is_palindrome(text):
    """
    Check if text is a palindrome (reads the same forward and backward).
    
    Args:
        text (str): Text to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    # Empty string is considered a palindrome
    if not text:
        return True
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    
    # If there are no alphanumeric characters, it's not a palindrome
    if not cleaned:
        return False
    
    return cleaned == cleaned[::-1]

def count_vowels_and_consonants(text):
    """
    Count vowels and consonants in text.
    
    Args:
        text (str): Text to analyze
    
    Returns:
        tuple: (vowel_count, consonant_count)
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    text = text.lower()
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)

def extract_email_addresses(text):
    """
    Extract email addresses from text using string methods.
    
    Args:
        text (str): Text to analyze
    
    Returns:
        list: List of extracted email addresses
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    words = text.split()
    emails = []
    
    for word in words:
        # Simple email extraction logic using string methods
        clean_word = word.strip(',.;:\'\"()[]{}')
        
        # Check for @ symbol with text before and after
        if '@' in clean_word:
            parts = clean_word.split('@')
            if len(parts) == 2 and parts[0] and parts[1] and '.' in parts[1]:
                # Validate domain has at least one dot
                domain_parts = parts[1].split('.')
                if len(domain_parts) >= 2 and all(domain_parts):
                    emails.append(clean_word)
    
    return emails

def extract_dates(text):
    """
    Extract dates in yyyy-mm-dd format from text.
    
    Args:
        text (str): Text to analyze
    
    Returns:
        list: List of extracted dates
    """
    if text is None:
        raise ValueError("Text cannot be None")
    
    words = text.split()
    dates = []
    
    for word in words:
        # Clean the word
        clean_word = word.strip(',.;:\'\"()[]{}')
        
        # Check if it matches date format yyyy-mm-dd
        if len(clean_word) == 10 and clean_word[4] == '-' and clean_word[7] == '-':
            year_part = clean_word[0:4]
            month_part = clean_word[5:7]
            day_part = clean_word[8:10]
            
            # Check if all parts are digits
            if (year_part.isdigit() and month_part.isdigit() and day_part.isdigit()):
                # Basic validation of month and day
                year = int(year_part)
                month = int(month_part)
                day = int(day_part)
                
                if 1 <= month <= 12 and 1 <= day <= 31:
                    dates.append(clean_word)
    
    return dates

def parse_csv_line(line):
    """
    Parse a CSV line into fields.
    
    Args:
        line (str): CSV line to parse
    
    Returns:
        list: List of fields
    """
    if line is None:
        raise ValueError("Line cannot be None")
    
    return line.split(',')

def format_text_table(headers, rows):
    """
    Format data as a text table.
    
    Args:
        headers (list): List of column headers
        rows (list): List of row data (each row is a list)
    
    Returns:
        str: Formatted text table
    """
    if headers is None or rows is None:
        raise ValueError("Headers and rows cannot be None")
    
    # Validate that all rows have the same length as headers
    for row in rows:
        if len(row) != len(headers):
            raise ValueError(f"Row length {len(row)} doesn't match header length {len(headers)}")
    
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Format header row
    header_row = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    separator = "-+-".join("-" * w for w in col_widths)
    
    # Format data rows
    data_rows = []
    for row in rows:
        data_rows.append(" | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))
    
    # Combine all parts
    table = f"{header_row}\n{separator}\n" + "\n".join(data_rows)
    return table

def display_text_analysis(text, analysis_type, result):
    """
    Display text analysis results.
    
    Args:
        text (str): Original text
        analysis_type (str): Type of analysis performed
        result: Analysis result
    """
    print(f"\nText Analysis: {analysis_type}")
    print(f"Original text: {text}")
    print(f"Result: {result}")

def main():
    """Main program function."""
    (plain_text, formatted_text, code_snippet, csv_data, json_data, 
     log_entry, palindrome, whitespace_text, mixed_case, with_numbers, url) = initialize_data()
    
    # Create a dictionary for easy access to text samples
    text_samples = {
        "1": ("Plain Text", plain_text),
        "2": ("Formatted Text", formatted_text),
        "3": ("Code Snippet", code_snippet),
        "4": ("CSV Data", csv_data),
        "5": ("JSON Data", json_data),
        "6": ("Log Entry", log_entry),
        "7": ("Palindrome", palindrome),
        "8": ("Whitespace Text", whitespace_text),
        "9": ("Mixed Case", mixed_case),
        "10": ("Text with Numbers", with_numbers),
        "11": ("URL", url)
    }
    
    while True:
        print("\n===== TEXT PROCESSING SYSTEM =====")
        print("Available Samples:")
        for key, (name, _) in text_samples.items():
            print(f"{key}. {name}")
        
        print("\nMain Menu:")
        print("1. Basic Text Analysis")
        print("2. Text Transformation")
        print("3. Text Extraction")
        print("4. Text Formatting")
        print("5. Custom Text Input")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == "0":
            print("Thank you for using the Text Processing System!")
            break
        
        elif choice == "1":
            print("\nText Analysis Options:")
            print("1. Character Count")
            print("2. Word Count")
            print("3. Check if Palindrome")
            print("4. Count Vowels and Consonants")
            analysis_choice = input("Select analysis option (1-4): ")
            
            sample_key = input("Enter sample number (1-11) or 'c' for custom text: ")
            
            if sample_key.lower() == 'c':
                text = input("Enter your text: ")
            elif sample_key in text_samples:
                _, text = text_samples[sample_key]
            else:
                print("Invalid sample number.")
                continue
            
            if analysis_choice == "1":
                count = count_characters(text)
                display_text_analysis(text, "Character Count", count)
            
            elif analysis_choice == "2":
                count = count_words(text)
                display_text_analysis(text, "Word Count", count)
            
            elif analysis_choice == "3":
                result = is_palindrome(text)
                display_text_analysis(text, "Palindrome Check", "Yes" if result else "No")
            
            elif analysis_choice == "4":
                vowels, consonants = count_vowels_and_consonants(text)
                display_text_analysis(text, "Vowels and Consonants", f"Vowels: {vowels}, Consonants: {consonants}")
            
            else:
                print("Invalid analysis option.")
        
        elif choice == "2":
            print("\nText Transformation Options:")
            print("1. Convert to Uppercase")
            print("2. Convert to Lowercase")
            print("3. Capitalize Words")
            print("4. Strip Whitespace")
            print("5. Replace Substring")
            transform_choice = input("Select transformation option (1-5): ")
            
            sample_key = input("Enter sample number (1-11) or 'c' for custom text: ")
            
            if sample_key.lower() == 'c':
                text = input("Enter your text: ")
            elif sample_key in text_samples:
                _, text = text_samples[sample_key]
            else:
                print("Invalid sample number.")
                continue
            
            if transform_choice == "1":
                result = to_uppercase(text)
                display_text_analysis(text, "Uppercase Conversion", result)
            
            elif transform_choice == "2":
                result = to_lowercase(text)
                display_text_analysis(text, "Lowercase Conversion", result)
            
            elif transform_choice == "3":
                result = capitalize_text(text)
                display_text_analysis(text, "Word Capitalization", result)
            
            elif transform_choice == "4":
                result = strip_whitespace(text)
                display_text_analysis(text, "Whitespace Stripping", result)
            
            elif transform_choice == "5":
                old = input("Enter substring to replace: ")
                new = input("Enter replacement string: ")
                try:
                    result = replace_substring(text, old, new)
                    display_text_analysis(text, f"Replace '{old}' with '{new}'", result)
                except ValueError as e:
                    print(f"Error: {e}")
            
            else:
                print("Invalid transformation option.")
        
        elif choice == "3":
            print("\nText Extraction Options:")
            print("1. Extract Substring")
            print("2. Find All Occurrences")
            print("3. Split Text")
            print("4. Extract Email Addresses")
            print("5. Extract Dates")
            extraction_choice = input("Select extraction option (1-5): ")
            
            sample_key = input("Enter sample number (1-11) or 'c' for custom text: ")
            
            if sample_key.lower() == 'c':
                text = input("Enter your text: ")
            elif sample_key in text_samples:
                _, text = text_samples[sample_key]
            else:
                print("Invalid sample number.")
                continue
            
            if extraction_choice == "1":
                try:
                    start = int(input("Enter start index: "))
                    end = int(input("Enter end index: "))
                    result = extract_substring(text, start, end)
                    display_text_analysis(text, f"Substring [{start}:{end}]", result)
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif extraction_choice == "2":
                substring = input("Enter substring to find: ")
                try:
                    positions = find_all_occurrences(text, substring)
                    if positions:
                        display_text_analysis(text, f"Find '{substring}'", f"Found at positions: {positions}")
                    else:
                        display_text_analysis(text, f"Find '{substring}'", "Not found")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif extraction_choice == "3":
                delimiter = input("Enter delimiter (press Enter for whitespace): ")
                delimiter = delimiter if delimiter else None
                result = split_text(text, delimiter)
                display_text_analysis(text, f"Split by '{delimiter}'", result)
            
            elif extraction_choice == "4":
                emails = extract_email_addresses(text)
                if emails:
                    display_text_analysis(text, "Email Extraction", emails)
                else:
                    display_text_analysis(text, "Email Extraction", "No emails found")
            
            elif extraction_choice == "5":
                dates = extract_dates(text)
                if dates:
                    display_text_analysis(text, "Date Extraction", dates)
                else:
                    display_text_analysis(text, "Date Extraction", "No dates found")
            
            else:
                print("Invalid extraction option.")
        
        elif choice == "4":
            print("\nText Formatting Options:")
            print("1. Join Text Parts")
            print("2. Format with Variables")
            print("3. Parse CSV Line")
            print("4. Create Text Table")
            formatting_choice = input("Select formatting option (1-4): ")
            
            if formatting_choice == "1":
                parts_str = input("Enter text parts separated by commas: ")
                parts = [part.strip() for part in parts_str.split(',')]
                delimiter = input("Enter join delimiter: ")
                result = join_text(parts, delimiter)
                display_text_analysis(parts, f"Join with '{delimiter}'", result)
            
            elif formatting_choice == "2":
                template = input("Enter template with {placeholders}: ")
                variables = {}
                
                while True:
                    var_name = input("Enter variable name (or 'done' to finish): ")
                    if var_name.lower() == 'done':
                        break
                    var_value = input(f"Enter value for {var_name}: ")
                    variables[var_name] = var_value
                
                try:
                    result = format_text_with_variables(template, **variables)
                    display_text_analysis(template, "Variable Formatting", result)
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif formatting_choice == "3":
                if "4" in text_samples:
                    csv_lines = text_samples["4"][1].split('\n')
                    line_idx = int(input(f"Enter line number to parse (0-{len(csv_lines)-1}): "))
                    
                    if 0 <= line_idx < len(csv_lines):
                        line = csv_lines[line_idx]
                        fields = parse_csv_line(line)
                        display_text_analysis(line, "CSV Parsing", fields)
                    else:
                        print("Invalid line number.")
                else:
                    print("CSV sample not available.")
            
            elif formatting_choice == "4":
                headers = input("Enter headers separated by commas: ").split(',')
                headers = [h.strip() for h in headers]
                
                rows = []
                while True:
                    row_str = input("Enter row values separated by commas (or 'done' to finish): ")
                    if row_str.lower() == 'done':
                        break
                    row = [cell.strip() for cell in row_str.split(',')]
                    
                    if len(row) != len(headers):
                        print(f"Error: Row must have {len(headers)} values to match headers.")
                        continue
                    
                    rows.append(row)
                
                if rows:
                    table = format_text_table(headers, rows)
                    print("\nFormatted Table:")
                    print(table)
                else:
                    print("No rows provided.")
            
            else:
                print("Invalid formatting option.")
        
        elif choice == "5":
            custom_text = input("Enter your custom text: ")
            
            print("\nCustom Text Analysis:")
            print(f"1. Length: {count_characters(custom_text)} characters")
            print(f"2. Words: {count_words(custom_text)} words")
            vowels, consonants = count_vowels_and_consonants(custom_text)
            print(f"3. Contains: {vowels} vowels, {consonants} consonants")
            
            if is_palindrome(custom_text):
                print("4. This text is a palindrome")
            
            emails = extract_email_addresses(custom_text)
            if emails:
                print(f"5. Found email addresses: {', '.join(emails)}")
            
            dates = extract_dates(custom_text)
            if dates:
                print(f"6. Found dates: {', '.join(dates)}")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()