from bs4 import BeautifulSoup
import re
from collections import Counter
from utils import common_words


class GetWords:
    def pull_data(self,r):
        ''' This method uses beautiful soup to extract texts from the website,remove unneccasary words and get top words'''
        data_pull = BeautifulSoup(r,'html.parser')
        find = data_pull.findAll('body')
        
        for texts in find:
            content = texts.text
            words = content.split()
        pattern = re.compile('[A-Za-z]+[A-Za-z]$')
        generate_word = (word for word in words if pattern.match(word))
        word_list= list(generate_word)
        word_count = Counter([word for word in word_list if word not in common_words])
        top_word= word_count.most_common()
        return top_word




    
       





