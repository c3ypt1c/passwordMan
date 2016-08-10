import hashlib, time, random

h = hashlib.new("SHA512", b"passwrod")
hh = h.hexdigest()
hhh = int ( hh, 16 )

def textToCryArr(text, hashAsInt): #Saves a hash ready for save
    btext = text.encode("UTF-32")
    btextar = list(btext)
    btextarr = []
    btextar = btextar[1:] #Removing first byte (255 is useless)

    return [ hex(int(x*hashAsInt)) for x in btextar ] #Wonderful
    
def cryArrToText(cryArr, hashAsInt):
    return ImportError

def genStrongPass(lengh=16,
        charRange={
        0:" ",1:"a",27:"A",2:"b",28:"B",3:"c",29:"C",4:"d",30:"D",5:"e",31:"E",6:"f",32:"F",7:"g",33:"G",8:"h",34:"H",9:"i",35:"I",10:"j",36:"J",11:"k",37:"K",12:"l",38:"L",13:"m",39:"M",14:"n",40:"N",15:"o",41:"O",16:"p",32:"P",17:"q",33:"Q",18:"r",34:"R",19:"s",35:"S",20:"t",36:"T",21:"u",37:"U",22:"v",38:"V",23:"w",39:"W",24:"x",40:"X",25:"y",41:"Y",26:"z",42:"Z",
        43:"!",
        #44:'"',
        #Speeches cause problems for this causing a \ to apear in from of it.
        #May be challenged for deletion... uncomment if you know what you are doing.
        45:"£",46:"$",47:"%",48:"^",49:"&",50:"*",51:"(",52:")",53:"-",54:"_",55:"=",56:"+",57:"[",58:"]",59:";",60:":",
        #61:"'",
        62:"@",63:"#",64:"~",65:"{",66:"}",
        67:"0",68:"1",69:"2",70:"3",71:"4",72:"5",73:"6",74:"7",75:"8",76:"9"}):#Sloppy layout... sorry..

    pas = ""
    for x in range(lengh):
        while True:
            try:
                hhh = charRange[random.randrange(100)]
                break
            except: pass #Badly coded for a reason.
        pas = str ( pas ) + str ( hhh )

    return pas


