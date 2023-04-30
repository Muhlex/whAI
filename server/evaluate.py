import os
import openai
from dotenv import load_dotenv


def evaluate_translation(original, translation):
	load_dotenv()

	openai.api_key = os.environ["OPENAI_API_KEY"]

	prompt = f'''Rate the machine translation of:
                 {original}
                 to:
                 {translation}
                 on a scale of 1 to 100. Just the number.'''

	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "user", "content": prompt}
		]
	)

	return completion.choices[0].message.content


def translate_chat_gpt(original: str, lang: str, emoji: bool):
	load_dotenv()

	openai.api_key = os.environ["OPENAI_API_KEY"]

	prompt = f'''
	 I want you to act as an {lang} translator, spelling corrector and improver.
	I will speak to you in any language and you will detect the language, translate it and answer in the corrected
	and improved version of my text, in {lang}. I want you to replace my simplified A0-level words and sentences with
	more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary.
	I want you to only reply the correction, the improvements and nothing else, do not write explanations.
	My first sentence is '{original}'
	'''

	if emoji:
		prompt = f"""
	I want you to translate the sentences I wrote into emojis. I will write the sentence, and you will express it with
	emojis. I just want you to express it with emojis. I don't want you to reply with anything but emoji. When I need
	 to tell you something in English, I will do it by wrapping it in curly brackets like {{like this}}. {original}"
	"""

	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "user", "content": prompt}
		]
	)

	return completion
