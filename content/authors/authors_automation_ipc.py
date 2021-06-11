from pathlib import Path
import csv

file_names = Path('/home/luca/Desktop/ipc.csv')
authors_path = Path('/home/luca/Repositories/stag21/content/authors')
author_page = """---
# Display name
title: {} {}

# Is this the primary user of the site?
superuser: false

# Role/position
# role: Administation


# Organizations/Affiliations
organizations:
- name: {}


#social:
#- icon: envelope
#  icon_pack: fas
#  link: 'mailto:comito@di.uniroma1.it'


# Enter email to display Gravatar (if Gravatar enabled in Config)
# email: ""

# Organizational groups that you belong to (for People widget)
#   Set this to `[]` or comment out if you are not using People widget.
user_groups:
- International program committee (tentative)

---
"""
with file_names.open() as f:
    csv_reader = csv.reader(f, delimiter=',')

    for row in csv_reader:
        name = row[0].strip()
        surname = row[1].strip()
        email = row[2].strip()
        affiliation = row[3].strip()
        role = row[4].strip()
        if not name or not surname or not affiliation:
            continue

        author_folder_name =  authors_path / f'ipc_{name.lower()}_{surname.lower()}'
        author_folder_name.mkdir(exist_ok=True)

        author_page_formatted = author_page.format(surname, name, affiliation)

        author_file_name = author_folder_name / '_index.md'
        author_file_name.write_text(author_page_formatted)
