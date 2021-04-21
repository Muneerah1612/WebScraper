from validator_collection import checkers


class CheckUrl:
    
    @classmethod
    def ValidUrl(cls):
        ''' This method checks if the user input is a valid url '''
        web_valid = input('Enter a website to analyse: ')
        checkers.is_url(web_valid)
        if checkers.is_url(web_valid):
            return web_valid
        else:
            return False
            

