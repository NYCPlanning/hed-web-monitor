from bs4 import BeautifulSoup
from messenger import send_alert
import sys

phases = ['https://forward.ny.gov/phase-two-industries', 'https://forward.ny.gov/phase-three-industries',
                'https://forward.ny.gov/phase-four-industries']

file_name = ['phase_two.txt', 'phase_three.txt', 'phase_four.txt']

app_secret = sys.argv[1]

if __name__ == "__main__":

    for i,page in enumerate(phases):
        
        getPage = requests.get(page)

        getPage.raise_for_status()

        soup = BeautifulSoup(getPage.content, 'html.parser')

        headers = soup.find_all('h2')
        
        l = []

        for h in headers:
            
            sector = h.get_text().strip()

            l.append(sector)

        print(l)
        
        with open(file_name[i], 'r') as filehandle:
            stored_ls = json.load(filehandle)
            
        change = set(l).symmetric_difference(set(stored_ls))
        
        c = bool(set(l).symmetric_difference(set(stored_ls)))
        
        if c:
            send_alert(file_name[i], phases[i], change, app_secret)
            
            with open(file_name[i], 'w') as filehandle:
                json.dump(l, filehandle)
        else:
            print('no update')
