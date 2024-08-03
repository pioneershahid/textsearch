'''Read the file and search for the specific text (e.g., "lorem ipsum").
Insert your name into the file at the found location.
Extract your name and display it.
Replace your name with "John Wick".
Write the modified content back to the file.
'''

import re

# Define the path to your .txt file
file_path = 'example.txt'

# Define your name
your_name = 'Shahid'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Search for the phrase "lorem ipsum" and insert your name
search_phrase = 'Lorem ipsum'
if search_phrase in content:
    # Insert your name after the search phrase
    new_content = re.sub(search_phrase, search_phrase + ' ' + your_name, content, count=1)
    
    # Extract your name from the file content
    extracted_name = re.search(rf'{your_name}', new_content)
    if extracted_name:
        print(f'Extracted Name: {extracted_name.group()}')
    
    # Replace your name with "John Wick"
    final_content = new_content.replace(your_name, 'John Wick')
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(final_content)
else:
    print(f'The phrase "{search_phrase}" was not found in the file.')
