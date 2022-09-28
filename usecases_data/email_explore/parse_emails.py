import re
import pandas as pd

emails = pd.read_csv("clinton_kaggle_emails/Emails.csv",
                     parse_dates=['MetadataDateSent'],
                     usecols=['MetadataSubject', 'MetadataTo',
                              'MetadataDateSent', 'MetadataFrom',
                              'RawText', 'Id'])


def get_body(rawtext):
    email_lines = rawtext.split('\n')
    start_line = [i for i, el in enumerate(email_lines)
                  if re.search('^From[: ]', el)]
    if not start_line:
        return ''
    start_line = start_line[0]
    end_line = [i for i, el in enumerate(email_lines)
                if re.search('UNCLASSIFIED', el) and i > start_line]
    end_line = len(email_lines) if not end_line else end_line[0]
    return '\n'.join(email_lines[start_line:end_line])


emails['ExtractedText'] = emails.RawText.apply(get_body)
emails.drop(columns='RawText', inplace=True)


extracted_raw_text = emails.RawText.apply(get_body)
get_body(emails.RawText[0])
