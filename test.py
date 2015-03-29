import unittest
from application import Storage

class TestSuite(unittest.TestCase):
  def test(self):
    storage = Storage()
    storage.populate()
    score = storage.score()
    self.failIf(score != 1234)

def main():
  unittest.main()

if __name__ == "__main__":
  main()
