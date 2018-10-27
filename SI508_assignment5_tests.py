## Do not change import statements.
import unittest
from SI508_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code. (That's okay!)
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)
class Card_class(unittest.TestCase):

	def test_varible(self):
		self.assertEqual(Card.suit_names,["Diamonds","Clubs","Hearts","Spades"])
		self.assertEqual(Card.rank_levels,[1,2,3,4,5,6,7,8,9,10,11,12,13])
		self.assertEqual(Card.faces[1],"Ace")
		self.assertEqual(Card.faces[11],"Jack")
		self.assertEqual(Card.faces[12],"Queen")
		self.assertEqual(Card.faces[13],"King")

class Consructor(Card_class):

	def test_Check_default(self):
		self.assertEqual(Card().suit,"Diamonds")
		self.assertEqual(Card().rank,2)

	def test_check_value(self):
		for suit in range(len(Card.suit_names)):
			for rank in Card.rank_levels:
				self.example = Card(suit,rank)
				self.assertEqual(self.example.__str__(),"{} of {}".format(self.example.faces[rank],self.example.suit))

class Deck_class(unittest.TestCase):

	def test_varible(self):
		self.assertIsInstance(Deck().cards,list)
		self.assertEqual(len(Deck().__str__().split("\n")),52)

	def test_POP_test(self):
		for i in range(52):
			Deck().pop_card(i)
		self.assertEqual(Deck().cards,[])

	def test_shuffle_test(self):
		self.assertIsInstance(Deck().shuffle(),list)
		self.assertTrue(Deck().cards != Deck().shuffle())

	def test_replace_card(self):
		for card in Deck().cards:
			Deck().replace_card(Card())
			self.assertTrue(len(Deck().cards),52)

	def test_sort_card(self):
		Deck().sort_cards()
		self.assertIsInstance(Deck().sort_cards(),list)
		self.assertEqual(Deck().cards[0],"Ace of Diamonds")

	def test_deal_hand(self):
		self.assertIsInstance(Deck().deal_hand(3),list)
		self.assertEqual(len(Deck().deal_hand(3)),3)
		self.assertEqual(type(Deck().deal_hand(3)[0]),type(Card()))
		Deck().pop_card(22)
		self.assertEqual(len(Deck().deal_hand(40)),32)


class Play(unittest.TestCase):
	def test_
















###########
if __name__ == "__main__":
    unittest.main(verbosity=2)