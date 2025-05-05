def get_num_words(book_content):
	words = book_content.split()
	count = len(words)
	return count

def get_each_char_count(book_content):
	lowercase_words = book_content.lower().split()
	found_chars = {}
	for word in lowercase_words:
		for char in word:
			if char in found_chars:
				found_chars[char] += 1
			else:
				found_chars[char] = 1
	return found_chars

def sort_on(dict):
    return dict["num"]

def get_sorted_chars_list(unsorted_chars_dict):
	dicts_list = []
	for char in unsorted_chars_dict:
		current_letter_dict = {}
		if char.isalpha():
			current_letter_dict["char"] = char
			current_letter_dict["num"] = unsorted_chars_dict[char]
			dicts_list.append(current_letter_dict)
	dicts_list.sort(reverse=True, key=sort_on)
	return dicts_list