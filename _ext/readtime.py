## System Imports
import bs4
import urllib


## Application Imports


## Library Imports


class HTMLReadableTextFetcher:
	
	@staticmethod
	def extract_text(url):
		html = urllib.urlopen(url).read()
		soup = bs4.BeautifulSoup(html, 'html.parser')
		texts = soup.findAll(text=True)
		return texts
	
	@staticmethod
	def is_visible(element):
		if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
			return False
		elif isinstance(element, bs4.element.Comment):
			return False
		elif element.string == "\n":
			return False
		return True
	
	"""
	@staticmethod
	def filter_visible_text(page_texts):
		return filter(is_visible, page_texts)
	
	@staticmethod
	def estimate_reading_time(url):
		texts = extract_url(url)
		filtered_text = filter_visible_text(texts)
		total_words = count_words_in_text(filtered_text, WORD_LENGTH)
		return total_words/WPM
	"""


class ReadTimeEstimation:

	WORDS_PER_MINUTE = 200
	WORD_LENGTH = 5
	
	@staticmethod
	def count_words_in_text(text_list, word_length):
		total_words = 0
		for current_text in text_list:
			total_words += len(current_text)/word_length
		return total_words
	
	@classmethod
	def estimate_reading_time(cls, content):
		total_words = cls.count_words_in_text(content, cls.WORD_LENGTH)
		
		return total_words / cls.WORDS_PER_MINUTE

