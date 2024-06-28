#Author: Minh To
#Description: This script searches through all of the pdfs in the folder and find any instances of the word "Table" and returns 250 words after. 
#Then, the script will generate a json dataset with the instruction, the input as the 250 words, and empty output to be manually labeled after.

import fitz  # PyMuPDF
import json
import os

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    text = ""

    # Iterate through the pages
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()

    return text


def find_all_following_words(text, filename, search_word, num_words):
    # Split the text into words
    words = text.split()

    results = []
    start_index = 0

    # Find all instances of the search word
    while start_index < len(words):
        try:
            start_index = words.index(search_word, start_index)
        except ValueError:
            break

        # Calculate the end index
        end_index = start_index + num_words + 1  # +1 to include the search word itself

        # Extract the following words
        following_words = words[start_index + 1:end_index]

        # Join the words back into a string and store in results
        result = ' '.join(following_words)
        results.append(result)

        # Move to the next word after the current search word
        start_index += 1

    return results

def to_json(output_name, instance_list):
    dictionary_list = []

    curIndex = 0
    for item in instance_list:
        thedict = dict(id = curIndex, file = item[1], instruction = "Extract a potential table from the input text, if there is no table, output NO TABLE", input = item[0], ouput = "")
        curIndex += 1
        dictionary_list.append(thedict)

    out_file = open(output_name, "w")

    json.dump(dictionary_list, out_file, indent=4)

    out_file.close()

    return curIndex

def main():
    # Path to your PDF file
    pdf_path = 'D:\\Code\\python\\extract-paper\\pdfs\has-tables'

    # Define the word to search for
    search_word = "Table"

    # Define the number of words to extract after the search word
    num_words = 250
    output_name = "dataset.json"

    # List all files and directories in the given directory
    items = os.listdir(pdf_path)

    # Filter out only the files
    filenames = [item for item in items if os.path.isfile(os.path.join(pdf_path, item))]

    allInstances = []
    for name in filenames:
        # Extract text from the PDF
        text = extract_text_from_pdf(os.path.join(pdf_path, name))
        withoutFileName = find_all_following_words(text, name, search_word, num_words)
        for instance in withoutFileName:
            allInstances.append((instance, name))


    # Find and print the following words for all instances
    for i, result in enumerate(allInstances):
        print(f"Instance {i + 1}:\n{result}\n")

    input_name = os.path.basename(pdf_path)

    to_json(output_name, allInstances)


if __name__ == "__main__":
    main()
import fitz  # PyMuPDF

