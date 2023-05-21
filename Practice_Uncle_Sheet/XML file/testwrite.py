
#Read and Write File (Text)

## encoding='utf-8' >> Support Thai language

## Writing to XML file

from lxml import etree

def writedata():
    
    root = etree.Element("root")
    a = etree.Element("a")
    
    a.text = "Hello, my name is Thanachart Saejueng"
    root.append(a)
    
    tree = etree.ElementTree(root)
    tree.write("testfile.xml")

        
#writedata()

        
    
## Reading XML file 

def readdata():

    tree = etree.parse("testfile.xml")
    
    print(etree.tostring(tree))
    

readdata()
