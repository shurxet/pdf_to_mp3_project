from pathlib import Path
from art import tprint
from gtts import gTTS
import pdfplumber


def pdf_to_mp3(file_path='file_test.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Please wait, file conversion is in progress...... ')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        audio_file = gTTS(text=text, lang=language)
        name_file = Path(file_path).stem
        audio_file.save(f'{name_file}.mp3')

        return f'' \
               f'[+]{name_file}.mp3 saved!' \
               f'Status ok!' \
               f'Have a nice day!'
    else:
        return 'File not exists, check the file' \
               'Sorry, but something went wrong!'


def main():
    tprint('PROGRAMM START'
           'PDF>>>TO>>>PDF', font='bulbhead'
           )
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
