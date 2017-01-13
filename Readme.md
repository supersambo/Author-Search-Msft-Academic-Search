#Publication search
This is a very simple single purpose script to query the Microsoft Academic Search Api for publications based on a list of given author names.

In order to use this:

* Download this repository
* Get an Api key from [here](https://www.microsoft.com/cognitive-services/en-US/sign-up?ReturnUrl=/cognitive-services/en-us/subscriptions)
* Edit access_key.edit by filling in your own key and change the filename to access_key
* Create a text file containing a list of authors (one per line) you want to query. Take `test.txt` as a reference if needed.
* Run the script with the path to your input file as a command line argument e.g. like this 
`python query_authors.py test.txt`
* The script will save the raw results as a single json file for each author to the `output/` directory

- - - -
```
Note that this is everything but sophisticated and does not handle api errors.
If you run into API limits just stop the script and/or implement your own error handling. At least the console will tell you that there is something going wrong.
```

