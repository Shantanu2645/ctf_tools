from hashlib import md5

var = input("Enter your string for type juggling hash gen:")
i = 0 
while ( True ):
    plaintext = var+str(i) 
    plain =  plaintext.encode()
    m = md5()
    m.update(plain)
    h = m.hexdigest()

    if h.startswith('0e'):
        if h[2:].isdigit():
            print (plaintext, h)
            break

    i += 1 
