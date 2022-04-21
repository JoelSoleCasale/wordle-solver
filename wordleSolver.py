from win_manager import Manager
import requests

def main():
    url = 'https://www.nytimes.com/games/wordle/index.html'
    m = Manager()
    #m.openWordle()
    r = requests.get(url)
    print(r.json())

if __name__ == '__main__':
    main()