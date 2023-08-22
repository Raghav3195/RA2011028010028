import requests
import json

def getNumbers(urls):
  number = []
  for i in urls:
    response = requests.get(i)
    if response.status_code == 200:
      number.extend(json.loads(response.content)["numbers"])
  return number

def sortAndRemoveDuplicates(number):
  return sorted(set(number))

def main():
  urls = ["http://20.244.56.144/numbers/primes", "http://20.244.56.144/numbers/fibo", "http://20.244.56.144/numbers/odd", "http://20.244.56.144/numbers/rand"]
  number = getNumbers(urls)
  number = sortAndRemoveDuplicates(number)

  print('{\n  "numbers":'+ " "+ json.dumps(number)+"\n}")
  
if __name__ == "__main__":
  main()
