import argparse
import re
from hanjatagger import Hanjaro

def modify_text(text):
    # Replace ( with [
    text = text.replace('(', '[')
    
    # Replace ) with ]
    text = text.replace(')', ']')
    
    return text

def detect_and_swap(text):
    # This function processes each pair of brackets and swaps the characters accordingly
    def swap(match):
        outside_text = match.group(1)
        inside_text = match.group(2)

        # Calculate the minimum length to avoid index errors
        min_length = min(len(outside_text), len(inside_text))

        # Create the swapped text
        swapped = ''.join(f'{inside_text[i]}[{outside_text[i]}]' for i in range(min_length))

        # Add remaining characters if the lengths are different
        if len(outside_text) > min_length:
            swapped += ''.join(f'[{outside_text[i]}]' for i in range(min_length, len(outside_text)))
        elif len(inside_text) > min_length:
            swapped += ''.join(f'{inside_text[i]}' for i in range(min_length, len(inside_text)))

        return swapped

    # Regular expression to match pattern like a(A) bc(BC) efg(EFG)
    return re.sub(r'(\w+)\[(\w+)\]', swap, text)

def main():
    parser = argparse.ArgumentParser(description="Modify text based on specific rules.")
    parser.add_argument("text", type=str, help="The input text to be modified")
    args = parser.parse_args()
    
    input_text = args.text
    
    # Query Hanjaro for tagging
    with Hanjaro() as hjr:
        raw_result = hjr.query(input_text)
        
        # Add a space before the result from Hanjaro
        spaced_result = ' ' + raw_result
        
        # Apply text modifications
        modified_text = modify_text(spaced_result)
        final_text = detect_and_swap(modified_text)
        
        # Only print the final result
        print(final_text)

if __name__ == "__main__":
    main()
