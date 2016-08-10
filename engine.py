import hashlib

h = hashlib.new("SHA512", b"passwrod")
hh = h.hexdigest()
hhh = int ( hh, 16 )

def textToCryArr(text, hashAsInt): #Saves a hash ready for save
    btext = text.encode("UTF-32")
    btextar = list(btext)
    btextarr = []
    btextar = btextar[1:] #Removing first byte (255 is useless)
    
    for x in btextar: btextarr.append(hex(int(x*hashAsInt)))
    return btextarr #Reduce to one line later... Too tired
    
        
def cryArrToText(cryArr, hashAsInt):
    return ImportError

