import pandas as pd
import xml.etree.ElementTree as ET

def xml_panda(file):
    tree = ET.parse(file)
    data = dict()
    attribs = ['id', 'published-at', 'title']
    data['text'] = list()
    root = tree.getroot()
    for i, article in enumerate(root.findall('article')):
        if len(article.attrib.keys()) != 3:
            for key in attribs:
                if key not in article.attrib.keys():
                    data[key].append("")
                else:
                    data[key].append(article.attrib[key])
        else:
            for key, value in article.attrib.items():
                if key not in data.keys():
                    data[key] = list()
                    data[key].append(value)
                else:
                    data[key].append(value)
        temp = ""
        for j, para in enumerate(article.findall('p')):
            if para.text is None:
                continue
            temp += para.text
        data['text'].append(temp)
    return pd.DataFrame(data=data)

def xml_panda_gt(file):
    tree = ET.parse(file)
    data = dict()
    attribs = ['hyperpartisan', 'id', 'labeled-by','url']
    root = tree.getroot()
    for i, article in enumerate(root.findall('article')):
        for key, value in article.attrib.items():
            if key not in data.keys():
                data[key] = list()
                data[key].append(value)
            else:
                data[key].append(value)
    return pd.DataFrame(data=data)


