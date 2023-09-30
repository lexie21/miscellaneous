# from PIL import Image

# img = Image.open(r"C:\Users\MrLinh\Project\CV\dog.jpg")
# new = img.resize((800,800))
# print(new.size)

import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG) #threshold level for printing
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')