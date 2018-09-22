'''
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year updated="yes">2010</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year updated="YES">8888888888</year>
        <gdppc>8888</gdppc>
        <neighbor direction="N" name="Malaysia" />
    <NewElement age="20" name="NewElement">This is a new element</NewElement></country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year updated="yes">2013</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
'''

#修改country为Singapore的节点year为8888888888,并且添加标签属性attrib为 updated="YES"
#修改Singapore 的gdppc为888 
#在country为Singapore的节点中添加tag <NewElement age="20" name="NewElement">This is a new element</NewElement></country>

import xml.etree.ElementTree as ET

tree = ET.parse('xml_lesson')
root = tree.getroot()
for i in root:
    if i.attrib['name'] == 'Singapore':
        for y in i.findall('year'):
            y.text = str(8888888888)
            y.set('updated', 'YES')
        for y in i.findall('gdppc'):
            y.text = str(8888)
        newEle = ET.Element("NewElement")
        newEle.attrib = {"name": "NewElement", "age": "20"}
        newEle.text = "This is a new element"
        i.append(newEle)
tree.write('output.xml')

#只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.attrib, node.text)
'''
year {'updated': 'yes'} 2010
year {'updated': 'YES'} 8888888888
year {'updated': 'yes'} 2013
'''







