# Covid Data Parser

Proof-of-concept Python script which prints Covid-related data (confirmed, deaths and recovered) for each country. It's
just a small-scale prototype of another project. But hey, somebody might find it useful. The original dataset can be found
[here](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset).


**Usage:** for Linux and macOS users: create a virtual environment and install dependencies from `requirements.txt`

```bash
# Create a virtual environment
$ python3 -m venv venv

# Activate a virtual environment and confirm you're in it
$ source venv/bin/activate
$ which python

# Install dependencies
$ pip3 install -r requirements.txt
```

Gain help about the two arguments you can use `--help`

```
$ python3 main.py --help                             
usage: main.py [-h] [--country COUNTRY] [--data DATA]

optional arguments:
  -h, --help         show this help message and exit
  --country COUNTRY  Country for which you wish to receive data
  --data DATA        Data you wanna receive, possible arguments are "confirmed", "deaths" and "recovered"
```

Anyways, here's a sample output

```
python3 main.py --country=Slovenia --data=recovered
RECOVERED data for Slovenia
(Country    Slovenia
1/22/20           0
1/23/20           0
1/24/20           0
1/25/20           0
             ...   
12/2/20       37218
12/3/20       37260
12/4/20       37260
12/5/20       37393
12/6/20       37685
Name: 155, Length: 321, dtype: object, Index(['1/22/20', '1/23/20', '1/24/20', '1/25/20', '1/26/20', '1/27/20',
       '1/28/20', '1/29/20', '1/30/20', '1/31/20',
       ...
       '11/27/20', '11/28/20', '11/29/20', '11/30/20', '12/1/20', '12/2/20',
       '12/3/20', '12/4/20', '12/5/20', '12/6/20'],
      dtype='object', length=320))
```
