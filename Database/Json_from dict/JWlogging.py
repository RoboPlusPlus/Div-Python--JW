import logging

#Logsetting. Ikke nødvendig for json.
logging.basicConfig(filename='programlog.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S %p')


user_names = ["Joachim", "harold", "Bob", "Laila"]
# Logger hvor man er i programmet
users_logged = "Setup for {} users logged".format(len(user_names))
logging.debug(users_logged)
