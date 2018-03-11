import xml.etree.ElementTree as ET

tree = ET.parse('menu.xml')
root = tree.getroot()

#for child in root:
#    print(child.tag, child.attrib)

#for child in root:
#    for i in range (0,1):
print(root[0][0].text)
print(root[0][1].text)
print(root[0][2].text)
print(root[0][3].text)
print(root[1][0].text)
print(root[1][1].text)
print(root[1][2].text)
print(root[1][3].text)

for food in root.iter('food'):
    print(food.attrib)

for food in root.findall('food'):
    description = food.find('description').text
    name = food.get('name')
    print(name, description)
