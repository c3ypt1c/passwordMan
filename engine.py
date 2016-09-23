import hashlib;
import random;

##Test program constants.
h = hashlib.new("SHA512", b"passwrod");
hh = h.hexdigest();
hhh = int ( hh, 16 );

class sets():
    encoding = "UTF-32";
    fileName = "passwords";
    cArrow = "> ";

class pa():
    
    class b64():
        Base64Chars = #Formatting test against charRange in genStrongPass in pa.
        {
    0:      "A",    16:     "Q",        32:     "g",    48:     "w",
    1:      "B",    17:     "R",        33:     "h",    49:     "x",
    2:      "C",    18:	    "S", 	34: 	"i", 	50: 	"y",
    3: 	    "D",    19:     "T", 	35: 	"j", 	51: 	"z",
    4: 	    "E",    20:     "U", 	36: 	"k", 	52: 	"0",
    5: 	    "F",    21:     "V", 	37: 	"l", 	53: 	"1",
    6: 	    "G",    22:     "W", 	38: 	"m", 	54: 	"2",
    7: 	    "H",    23:     "X", 	39: 	"n", 	55: 	"3",
    8: 	    "I",    24:     "Y", 	40:	"o", 	56: 	"4",
    9: 	    "J",    25:     "Z", 	41: 	"p", 	57: 	"5",
    10:     "K",    26:     "a", 	42: 	"q", 	58: 	"6",
    11:     "L",    27:     "b", 	43: 	"r", 	59: 	"7",
    12:     "M",    28:     "c", 	44: 	"s", 	60: 	"8",
    13:     "N",    29:     "d", 	45: 	"t", 	61: 	"9",
    14:     "O",    30:     "e",	46: 	"u", 	62: 	"+",
    15:     "P",    31:     "f", 	47: 	"v", 	63: 	"/"
            };
        def to(val):
            return NotImplementedError;
        def fm(val):
            return NotImplementedError;
        
    
    def textToCryArr(text, hashAsInt):      #Saves a hash ready for save
        return [ hex(int(x*hashAsInt)) for x in list(text) ]; #Wonderful :3
        
    def cryArrToText(cryArr, hashAsInt):
        return bytes([ int ( int( x, 16 ) / hashAsInt ) for x in cryArr ]); #Much coding skill

    def genStrongPass(lengh=16,
            charRange={
            0:" ",1:"a",27:"A",2:"b",28:"B",3:"c",29:"C",4:"d",30:"D",5:"e",31:"E",6:"f",32:"F",7:"g",33:"G",8:"h",34:"H",9:"i",35:"I",10:"j",36:"J",11:"k",37:"K",12:"l",38:"L",13:"m",39:"M",14:"n",40:"N",15:"o",41:"O",16:"p",32:"P",17:"q",33:"Q",18:"r",34:"R",19:"s",35:"S",20:"t",36:"T",21:"u",37:"U",22:"v",38:"V",23:"w",39:"W",24:"x",40:"X",25:"y",41:"Y",26:"z",42:"Z",
            43:"!",45:"£",46:"$",47:"%",48:"^",49:"&",50:"*",51:"(",52:")",53:"-",54:"_",55:"=",56:"+",57:"[",58:"]",59:";",60:":",62:"@",63:"#",64:"~",65:"{",66:"}",
            67:"0",68:"1",69:"2",70:"3",71:"4",72:"5",73:"6",74:"7",75:"8",76:"9"}):

        pas = "";
        for x in range(lengh):
            while True:
                try:
                    hhh = charRange[random.randrange(100)];  #Would this really post a security threat?
                    break;
                except: pass; #Badly coded for a reason. (takes longer to gen)

        return str ( pas ) + str ( hhh );

class IO():
    def fread(file):
        f = open(file, "rb");
        ff = f.read();
        f.close();
        del f;
        return ff;

    def fright(file, dataAsB):   #See what I did there?
        f = open(file, "wb");
        f.write(dataAsB);
        f.close();
        del f;
        return True;
                      
class menu():
    def menu():
        return """
1. View passwords (check your back)
2. Generate a password and add it
3. Add a password manually
4. Exit
""";

    def pasGen():
        return """
1. Default (16 chars, random)
2. Choose lengh
""";
    
    def c(arrow):
        return str ( input ( arrow ) );

#remember eval()

##Loading

try:
    data = fread(sets.fileName);
except:
    data = b"";

encPass = []; #[Passwords] Passwords = [byte, byte, byte... [site and info]]

while True:
    print ( menu.menu() );
    c = menu.c(sets.cArrow);
    try:
        if   c == "1": #Add a password
            ##addAPassword()
            pass;
        elif c == "2": #Generate a password and add it.
            while True:
                try:
                    while True:
                        print ( menu.pasGen() );
                        c = menu.c(sets.cArrow);
                        if c == "" or c == "1":
                            p = pa.genStrongPass();
                            l = 16;
                            break;
                        elif c == "2":
                            print ( "How long?" );
                            l = int ( menu.c(sets.cArrow) );
                            p = pa.genStrongPass(l);
                            break;
                        else:
                            print ( "What?" );
                            
                    try:
                        while True:
                            print ( p );
                            
                            print ( "Happy? Y/N?" );
                            c = menu.c(sets.cArrow).lower();
                            if c == "n" or c == "":
                                p = pa.genStrongPass(l);
                            elif c == "y":
                                break;
                            else:
                                print ( "What?" );
                                
                    except KeyboardInterrupt:
                        pass;
                    if c == "y":
                        while True:
                            print ( "Add a comment to the password:", p );
                            try:
                                c = menu.c(sets.cArrow);
                                if c == "":
                                    print ( "Are you sure you want to leave that blank?" );
                                    c = menu.c(sets.cArrow).lower();
                                    if c == "y":
                                        c = "";
                                        break;
                                    elif c == "n" or c == "":
                                        pass;
                                    else:
                                        print ( "What?" );
                                else:
                                    break;
                                
                            except KeyboardInterrupt:
                                pass;

                        encPass.append([pa.textToCryArr(p.encode(sets.encoding),hhh),c]);   
                        break;
                except KeyboardInterrupt:
                    pass;

        elif c == "3":
            #Some stuff here
            pass;
            
        elif c == "4": #Exit
            break;
        else:
            print ( "What?" );
        
    except KeyboardInterrupt:
        pass;

