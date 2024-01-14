import json
import xml.etree.ElementTree as ET


class NameException(Exception):
    def __str__(self):
        return "Net nazvaniy"


class Cinematography:
    def __init__(self, name, duration, genre):
        if name == "":
            raise NameException
        self.name = name
        if duration <= 0:
            raise ValueError("Продолжительность не может не быть")
        self.duration = duration
        self.genre = genre

    def to_dict(self):
        js = {"Type": type(self).__name__}
        for key, value in vars(self).items():
            js[key] = str(value)
        return js


class Film(Cinematography):
    def __init__(self, name, duration, genre, part):
        super().__init__(name, duration, genre)
        self.part = part

    def str(self):
        return f"Film: {self.name}, Duration: {self.duration}, Genre: {self.genre}, Part: {self.part}"


class Serial(Cinematography):
    def __init__(self, name, duration, genre, seasons):
        super().__init__(name, duration, genre)
        self.seasons = seasons

    def str(self):
        return f"Serial: {self.name}, Duration: {self.duration}, Genre: {self.genre}, Seasons: {self.seasons}"


def read_jsonfile(filename: str):
    with open(filename, "r") as file:
        text = file.read()
        return json.loads(text)


def write_json(filename: str, items):
    with open(filename, "w") as my_file:
        my_file.write(json.dumps(items, indent=4))


def read_xmlfile(filename: str):
    result = []
    tree = ET.parse(filename)
    root = tree.getroot()
    for arts in root:
        element = dict()
        for art in arts:
            element[art.tag] = art.text
        result.append(element)
    return result


def write_xml(elements, filename):
    root = ET.Element('root')
    for element in elements:
        art = ET.SubElement(root, 'art')
        for key, value in element.items():
            ET.SubElement(art, key).text = element[key]
    tree = ET.ElementTree(root)
    tree.write(filename)


film = Film("", 142, "Drama", 1)
write_json("film_kas.json", film.to_dict())
print(read_jsonfile("film_kas.json"))
serial = Serial("Oleg v ser", 52, "Comedy", 4)

chto_posmotret = [film.to_dict()]
write_xml(chto_posmotret, "chto_posmotret.xml")
print(read_xmlfile("chto_posmotret.xml"))
