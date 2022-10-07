#Defang ip address
#convert the '.' in ip to "[.]"

def defang_ip(address):
    new_address=""
    split_address=address.split(".")
    separator="[.]"
    new_address=separator.join(split_address)
    return new_address

defangip= defang_ip('1.1.2.4')
print(defangip)