import matplotlib.pyplot as barchart


class BarChart:
    def plot_chart(self,web_data):
        ''' This method plots a bar chart showing the top 7 words in a website '''
        get_len = web_data[:7]
        x = [word[0] for word in get_len]
        y = [count[1] for count in get_len]
        barchart.bar(x,y)
        barchart.title('Top words')
        barchart.xlabel('Words')
        barchart.ylabel('Count')
        barchart.show()

