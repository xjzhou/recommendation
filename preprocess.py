# -*- coding: utf-8 -*-
# Origin resource from MovieLens: http://grouplens.org/datasets/movielens/1m
import pandas as pd

class Channel:
    """
    simple processing for *.dat to *.csv
    """

    def __init__(self):
        self.origin_path = 'data/{}'

    def process(self):
        print('Process user data...')
        self._process_user_data()
        print('Process movies data...')
        self._process_movies_date()
        print('Process rating data...')
        self._process_rating_data()
        print('End.')

    def _process_user_data(self, file='users.dat'):
        f = pd.read_table(self.origin_path.format(file), sep='::', engine='python',
                          names=['userID', 'Gender', 'Age', 'Occupation', 'Zip-code'])
        f.to_csv(self.origin_path.format('users.csv'), index=False)

    # 数据过大，会直接OOM跳出
    def _process_rating_data(self, file='ratings.dat'):
        CHUNK_SIZE = 100000
        f = pd.read_table(self.origin_path.format(file), sep='::', engine='python', chunksize=CHUNK_SIZE, 
                          names=['UserID', 'MovieID', 'Rating', 'Timestamp'])

        df = f.get_chunk(CHUNK_SIZE)
        df.to_csv(self.origin_path.format('ratings.csv'), mode='w', header=True, index=False)
        while True:
            try:
                df = f.get_chunk(CHUNK_SIZE)
                df.to_csv(self.origin_path.format('ratings.csv'), mode='a', header=False, index=False)
            except StopIteration:
                print("Iteration is stopped.")
                break

    def _process_movies_date(self, file='movies.dat'):
        f = pd.read_table(self.origin_path.format(file), sep='::', engine='python',
                          names=['MovieID', 'Title', 'Genres'])
        f.to_csv(self.origin_path.format('movies.csv'), index=False)


if __name__ == '__main__':
    Channel().process()
