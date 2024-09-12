elements = [
    {"id": 1, "value": "red"},
    {"id": 2, "value": "green"},
    {"id": 3, "value": "blue"},
]


def get_by_id(elements, id):
    for element in elements:
        if element.get('id') == id:
            return element
        return None
