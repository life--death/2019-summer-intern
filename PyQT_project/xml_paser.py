from xml.dom import minidom

with open('notepad1.exe.xml', encoding='utf-8') as f:
    dom = minidom.parse(f)
    root = dom.documentElement
    print(root.nodeName)
