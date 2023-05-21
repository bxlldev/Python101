
#Read and Write File (Text)

## encoding='utf-8' >> Support Thai language

## Writing to JSON file

import json

def writedata():

    dict_profile = {
            'Name':'Thanachart Saejueng',
            'Phone':'0643959165'
        }
    
    with open('testfile.json','w',encoding='utf-8') as myfile:
        json.dump(dict_profile,myfile)

        
#writedata()

        

## Appending to a file

### JSON file no need to appending to file, only edit in dict() is fine
        


    
## Reading JSON file 

def readdata():
    with open('testfile.json', encoding='utf-8') as myfile:
        data = json.load(myfile)
        
    print(data)
    

#readdata()
