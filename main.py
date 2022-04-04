from random import sample
import requests
import os
import csv
from datetime import date

members = [
    'Brian',
    'Mags',
    'Sara'
]

roles = [
    'President',
    'Treasurer',
    'Secretary',
]

data = {
    "text": "A new officer election has been recorded!\n&nbsp;\n### Results:",
}

selected_members = sample(members, len(roles))

print(f'Results: {selected_members}')

for i in range(len(roles)):
    data['text'] += f'\n* **{roles[i]}**: {selected_members[i]}'

today = date.today()
year = today.year

file_path = f'./results/{year}.csv'

write_header = False

if not os.path.exists(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    write_header = True

with open(file_path, 'a+') as csv_file:
    csv_writer = csv.writer(csv_file)

    if write_header:
        csv_writer.writerow(['Date'] + roles)

    csv_writer.writerow([today.isoformat()] + selected_members)

requests.post(url=os.getenv("WEBHOOK_URL"), data=data)
