import os.path
#load_filepath = "pinglist.txt"
#addresses = []
#descriptions = []
#data = []

def load_ping_list(load_filepath =  "pinglist.txt"):
    addresses = []
    descriptions = []
    data = []
    """
    Funksjonen tar argument som er filepath for fil som skal lastes
    Filen skal være kommaseparert med adresse til venstre, og beskrivelse
    til høyre.

    Funksjonen returnerer:
    list(adresser fra liste), list(beskrivelse fra liste), bool(load_error)

    
    """
    load_error = False
    addresses = []
    descriptions = []
    data = []
    if not os.path.isfile(load_filepath):


        try:
            f = open(load_filepath,'w')
            f.close()
        except OSError as err:
            print("OS error: {0}".format(err))
            load_error = True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            load_error = True
            raise
            
    if os.path.isfile(load_filepath):
        try:
            with open(load_filepath,'r') as f:
                data = f.readlines()
             
            for line in data:
                words = line.split(",")
                address, *description = words
                addresses.append(address)
                descriptions.append(description)
        except OSError as err:
            print("OS error: {0}".format(err))
            load_error = True
        except ValueError:
            print("ValueError loading {}".format("pinglist.txt"))
            load_error = True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            load_error = True
            raise
    return addresses, descriptions, load_error


#if __name__ == "__main__":
 #   addresses, descriptions, load_error = load_ping_list(load_filepath)
  #  print(addresses)
   # print(descriptions)
