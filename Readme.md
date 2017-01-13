#Publication search
This is a very simple single purpose script to query the Microsofts Academic Search Api for publications based on a list of given author names.

To use this:

1. Download this repository

2. Get an Api key from [here](https://www.microsoft.com/cognitive-services/en-US/sign-up?ReturnUrl=/cognitive-services/en-us/subscriptions)

3. Edit access_key.edit by filling in your own key and change the filename to access_key
4. Create a file text file containing a list of authors (one per line) you want to query. Take `test.txt` as a reference if needed.

5. Run the script with the path to your input file as a command line argument e.g. like this `python msft_api.py test.txt`

6. The script will save the raw results as a single json file for each author to the `output/` directory


```
Note that this is everything than sophisticated and does not handle api errors.
 If you run into API limits just stop the script or implement your own error handling.
```

