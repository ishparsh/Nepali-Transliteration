import re
import os
from ntr.bhandar import dict_value


def nep_to_rom(text):
    
    def nep_rom(text):
        con=text
        if type(text) == float:
            return
        cond=0
        for key,value in dict_value.items():
            #print(value)
            text=text.replace(key,value)
            #print(text)
        # Check if last character is 't'
        if len(con)!=1: #for one word letter like ra la 
            if con[-1] != 'ा':
                if con[-2]!='्':
                    
                    if text[-1]=='a':
                        text = text[:-1]
                        
            if con[-1]=='र' and con[-2]=='े':
                text=text+'a'
            if con[-2]=='ए':
                text=text+'a'
            #if con[-2]=='ा':
                #text=text[:-1]+'a'+text[-1:]
            
        return text

  
    output=''
    a=re.findall(r'\S+|\n',text)      #split using space and stores as list 
    for value in a:
        output=output+' '+nep_rom(value)

    return(output)
