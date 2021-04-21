import requests


class GetRequest:
    def request(self,website):
        ''' this method requests for the url content '''
        try:
            get_page = requests.get(website)
            if get_page.status_code == 200:
                return get_page.text
            else:
                print('The website is not accessible')

        except requests.exceptions.RequestException:
            print (' There is an error,retry or check that it is a valid url')
            return False
            




