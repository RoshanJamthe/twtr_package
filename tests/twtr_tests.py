import pandas as pd
tweet = ['@pro_player I was a great player', '@lcoal Michalle sang in 1940, really great','@mania Why! so great']
rank = [1,2,3]
sample = pd.DataFrame(list(zip(rank,tweet)),columns=['Rank','text'])

import warnings
warnings.filterwarnings("ignore")

import unittest

import twtr

class Testtwtr(unittest.TestCase):
    def test_clean_process(self):
        self.assertEqual(twtr.process(sample,'text').to_list()[0], "great player")
        self.assertEqual(twtr.process(sample,'text').to_list()[2], "great")

if __name__ == '__main__':
    unittest.main()
