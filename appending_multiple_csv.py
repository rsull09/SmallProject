import pandas as pd
import os
import glob
os.chdir("/path/to/validations")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames], sort = False)

combined_csv.to_csv("validations.csv", index=False, encoding='utf-8-sig')
