def solution(text: str) -> str:
    """
    Calculate the sum of numbers in the text where each number is
    specified as a word (one, two, etc.) followed by a digit.
    Example: "two 3, then three 4" -> 2*3 + 3*4 = 18
    """
    
    # Remove all 's' characters
    text = text.replace("s", "")
    
    # Split text by ', then'
    parts = text.split(", then")
    
    # Mapping number words to digits
    number_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }
    
    total = 0
    
    for part in parts:
        part = part.strip()  # Remove leading/trailing spaces
        multiplier = 0
        
        # Find number word in part
        for word, value in number_words.items():
            if word in part:
                multiplier = value
                part = part.replace(word, "").strip()
                break
        
        # Convert remaining part to integer and multiply
        try:
            number = int(part)
            total += number * multiplier
        except ValueError:
            # Ignore parts that cannot be converted to integer
            pass
    
    return str(total)


# Example usage
if __name__ == "__main__":
    test_text = "two 3, then three 4, then five 2"
    print(solution(test_text))  # Output: 24
