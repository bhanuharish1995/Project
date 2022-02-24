%%file hw01.py
from mrjob.job import MRJob

class avgwords(MRJob):
    @staticmethod
    def count(values):
        wordcnt_list = []
        wordcnt = 0
        for i in values:
            wordcnt += i
            wordcnt_list.append(i)
        return len(wordcnt_list),wordcnt
    def mapper(self, _, line):
        data= line.split(',')
        text=data[4]
        words_split = text.split()
        word_count = len(words_split)
        if words_split != 'text':
            yield  "wordcount",word_count

    def reducer(self, key,values):
        rowcount,total_wordcount = self.count(values)
        yield "Average words in each review = ",(total_wordcount/rowcount)
if __name__ == '__main__':
    avgwords.run()

!curl https://raw.githubusercontent.com/bhanuharish1995/homework/main/yelp.csv -o yelp.csv
  
import hw01

mr_job = hw01.avgwords(args=['yelp.csv'])

with mr_job.make_runner() as runner:
    runner.run()
    for key, value in mr_job.parse_output(runner.cat_output()):
        print(key, value)
