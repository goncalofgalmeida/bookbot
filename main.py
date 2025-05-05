import sys
from stats import get_num_words, get_each_char_count, get_sorted_chars_list

def get_book_text(filepath):
	with open(filepath) as file:
		file_contents = file.read()
		return file_contents
	
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	filepath = sys.argv[1]
	file_content = get_book_text(filepath)
	num_words = get_num_words(file_content)
	found_chars_count = get_each_char_count(file_content)
	sorted_found_chars_list = get_sorted_chars_list(found_chars_count)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for entry in sorted_found_chars_list:
		print(f"{entry["char"]}: {entry["num"]}")
	print("============= END ===============")

main()