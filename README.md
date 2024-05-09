# CSVeader
Yes, that is an intentional typo because I wanted to have a ✨catchy✨ repository name. The goal of this project is to provide a Command Line application to read, sort, and run commands on a csv file. Emphasis on **sort** because I wanted to get practice with data structures and algorithms in Python.

## To run locally
The dataset is [us housing listings from kaggle](https://www.kaggle.com/datasets/austinreese/usa-housing-listings) download this dataset or any csv file and add it to the /data directory or you can point the app to a csv using its absolute path as the first arg.

If you have the kaggle set from above in the /data dir then from the program root run:
```
python src/main.py data/housing.csv
```

Available commands are: `"print", "sortby", "add", "exit"`
