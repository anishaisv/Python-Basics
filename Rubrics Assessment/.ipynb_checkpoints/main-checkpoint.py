import requests

def main():
    print("Hello learners!")
    n=int(input("Enter a number:"))
    trivia_fetch(n)
    print(n)
    
def trivia_fetch(num):
    response=requests.get(f'http://numbersapi.com/{num}?json')
    return response.json() 

if __name__=="__main__":
  main()