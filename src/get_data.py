import zipfile
import subprocess
import pandas as pd
import os

if os.path.isfile("data/creditcard.csv"):
    n = 1
else:
    subprocess.run(['kaggle', 'datasets', 'download', '-d', 'mlg-ulb/creditcardfraud'])
    
    with zipfile.ZipFile('./creditcardfraud.zip', 'r') as zip_ref:
        zip_ref.extractall('./data')
        
    os.remove("creditcardfraud.zip")





# git init
# dvc init

# dvc add data.csv
# git add .gitignore data.csv.dvc
# git commit -m "Add data"

# dvc remote add -d storage gdrive://1W4VEkftEoGvWedVK1LSUEQuwEkrxdBcJ
# git commit .dvc/config -m "Configure remote stroage"

# dvc push



# dvc run -n data -d get_data.py -o creditcard.csv --no-exec python get_data.py

# dvc repro

# visualize pipeline
# dvc dag


# git add .gitignore
# git commit -m "Add .gitignore file to ignore data folder"

# git push origin main
