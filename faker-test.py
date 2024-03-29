# configuring logger
import logging
import sys

file_handler = logging.FileHandler(filename='default.log')
stdout_handler = logging.StreamHandler(stream=sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)

logger = logging.getLogger(__name__)

import csv
from datetime import datetime as dt
from faker import Faker
import pandas as pd

pd.set_option('display.max_colwidth', None)
Faker.seed(0)
fake = Faker()


_rows_to_generate = 10000
logger.info('Generating %s rows ...', _rows_to_generate)
_headers = ['Name', 'Address', 'Job', 'Email', 'Nationality', 'Score']
_rows = [
    [fake.name(), fake.street_address(), fake.job(), fake.free_email(), fake.country(), fake.pyint()] 
    for _ in range(_rows_to_generate)
]


logger.info('Populating Pandas DataFrame ...')
df = pd.DataFrame(data=_rows, columns=_headers)


_csv_path = 'data/fake_data.csv'
logger.info('Writing CSV %s', _csv_path)

df.to_csv(index=False, path_or_buf=_csv_path, sep=";", quoting=csv.QUOTE_NONNUMERIC)
logger.info('Done')
