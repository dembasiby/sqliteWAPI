import csv


def process_for_db(csvFile):
    elements = []
    with open(csvFile, 'r') as f:
        data = list(csv.reader(f))

    header = data[0]
    for row in data[1:]:
        elements.append({h: row[idx] for idx, h in enumerate(header)})

    return elements
