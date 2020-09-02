def hxhx(message):
#    message = message.replace('him', 'them')
#    message = message.replace('his', 'their')
#    message = message.replace('he', 'they')
#    message = message.replace('she', 'they')
    message = message.replace('?safe', '')
    message = message.replace('?safe ', '')
    
    message = message.replace('woman', 'person')
    message = message.replace('man', 'person')
    message = message.replace('son', 'child')
    message = message.replace('daughter', 'child')

    message = message.replace('a', 'x')
    message = message.replace('A', 'X')
    message = message.replace('e', 'x')
    message = message.replace('E', 'E')
    message = message.replace('i', 'x')
    message = message.replace('I', 'X')
    message = message.replace('o', 'x')
    message = message.replace('O', 'X')
    message = message.replace('u', 'x')
    message = message.replace('U', 'X')
    
    message = message.replace('pxrchxld', 'perchild')
    message = message.replace('chxld', 'child')
    
    return message
