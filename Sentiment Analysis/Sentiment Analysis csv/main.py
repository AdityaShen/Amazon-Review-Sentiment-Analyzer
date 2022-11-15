import csv
import json
import requests

def request_analysis(text_to_analyze):
    payload = "text=" + str(text_to_analyze)
    response = requests.post("http://text-processing.com/api/sentiment/",
               data=payload)
    return response

def analyze_text(file):
    countpos = 0
    countneg = 0
    countneu = 0
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for row in reader:
                try:    
                    print('Analyzing: ' + str(row))
                    output = request_analysis(str(row))
                    output = output.json()
                    if 'pos' in output['label']:
                        print('Analyzed as positive')
                        countpos += 1
                    elif 'neg' in output['label']:
                        print('Analyzed as negative')
                        countneg += 1
                    else:
                        print('Analyzed as neutral')
                        countneu += 1
                    print()
                
                except UnicodeEncodeError as e:
                    continue  
        csvfile.close() 

def main():
    input1 = input("Enter CSV Directory: ")
    analyze_text(input1)

main()
