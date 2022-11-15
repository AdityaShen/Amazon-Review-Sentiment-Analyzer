This is a Python script for conducting basic sentiment analysis of text
stored in .csv files. It uses the public
[text-processing.com](http://text-processing.com/docs/)
API to conduct the sentiment analysis. This is a very short script written as
practice in using APIs and Python libraries.

# Requirements

You will need Python 3.X and the
[Requests](http://docs.python-requests.org/en/latest/) library.

# Usage

Format your .csv file such that each block of text to analyze is on a separate
row. You will be prompted to enter a path to the file when the script runs, so
it might be simpler to move the file to the same directory as the script.

Then just run the script:

```
python3 main.py
```
Each block of text will be categorized as positive, negative, or neutral and
assigned a probability representing the strength of the classification.

Bear in mind that the sentiment analysis uses classifiers trained on Tweets and
movie reviews. Your results will be most accurate if your data is similar.
Blocks of text must be 80,000 characters or less.

# Future Improvements

* Validation of file formatting
* Check status of response to POST request and create error messages
* Write output to the .csv file or a separate file
* Write detailed output, including all probabilities

# License

This script is MIT license. The public
[text-processing.com](http://text-processing.com/docs/)
API restricts usage to non-commercial
purposes and limits daily requests to 1000.
