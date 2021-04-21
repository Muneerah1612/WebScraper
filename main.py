from analyse import CheckUrl
from get import GetRequest
from top_words import GetWords
from barchart import BarChart


class Web:
    def WebScrape(self):
        ''' This function prompts the user to analyse any website of their choice '''

        while True:
            ask_to_scrape = input('Would you like to scrape a webiste (y/n) ')
            if ask_to_scrape == 'n':
                print('Thanks for analyzing! come back again')
                break
                
            elif ask_to_scrape == 'y':
                url= CheckUrl.ValidUrl()
                if url:
                    request_url = GetRequest().request(url)
                    if request_url:
                        pull = GetWords().pull_data(request_url)
                        print (f'The top word is: {pull[0][0]}')
                        bar = BarChart().plot_chart(pull)
                        print(bar)
                else:
                    print('The website url is not valid ')
                
            else:
                print (" 'y' means yes, 'n' means no ")

if __name__ == '__main__':
    Web().WebScrape()
    




