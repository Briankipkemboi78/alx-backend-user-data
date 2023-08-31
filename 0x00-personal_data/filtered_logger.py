import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(r'({0})=.*?({1})'.format('|'.join(fields), separator), r'\1={0}\2'.format(redaction), message)

# Example usage
fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))