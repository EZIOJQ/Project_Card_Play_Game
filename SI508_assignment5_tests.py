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
		self.assertEqual(type(Deck().cards[0]),type(Card()))
		self.assertEqual(len(Deck().__str__().split("\n")),52)
		count_dic_suit = {"Diamonds":0,"Clubs":0,"Hearts":0,"Spades":0}
		for string in Deck().__str__().split("\n"):
			for suit in Card.suit_names:
				if suit  in string:
					count_dic_suit[suit] += 1
		for item in list(count_dic_suit.keys()):
			self.assertEqual(count_dic_suit[item],13) 

	def test_POP_test(self):
		new_Deck = Deck()
		new_Deck2 = Deck()
		item1 = new_Deck.pop_card()
		new_Deck.replace_card(item1)
		self.assertEqual(item1.__str__(),new_Deck.cards.pop(-1).__str__())
		for i in range(52):
			order = len(new_Deck2.cards)
			new_Deck2.pop_card(order-1)
		self.assertEqual(len(new_Deck2.cards),0)

	def test_shuffle_test(self):
		new_Deck = Deck()
		self.assertTrue(new_Deck.cards != new_Deck.shuffle())

	def test_replace_card(self):
		for card in Deck().cards:
			Deck().replace_card(Card())
			self.assertTrue(len(Deck().cards),52)
		new_Deck = Deck()
		new_Deck.pop_card()
		card_pop = new_Deck.pop_card()
		new_Deck.replace_card(card_pop)
		self.assertEqual(new_Deck.cards[-1],card_pop)

	def test_sort_card(self):
		if Deck().cards[0] == "Ace of Diamonds":
			Deck().shuffle()
		else:
			Deck().sort_cards()
		self.assertEqual(Deck().cards[0].__str__(),"Ace of Diamonds")

	def test_deal_hand(self):
		new_Deck = Deck()
		self.assertIsInstance(Deck().deal_hand(3),list)
		self.assertEqual(len(Deck().deal_hand(52)),52)
		self.assertEqual(type(Deck().deal_hand(3)[0]),type(Card()))
		for i in range(52):
			order = len(new_Deck.cards)
			card_pop = new_Deck.pop_card(order-1)
			self.assertTrue(card_pop in Deck().deal_hand(52))
		# self.assertEqual(len(new_Deck.deal_hand(40)),32)


class Play(unittest.TestCase):
	def test_game_winner(self):
		self.assertIsInstance(play_war_game(),tuple)

	def test_reuslt_value(self):
		self.assertIsInstance(play_war_game()[0],str)
		self.assertIsInstance(play_war_game()[1],int)
		self.assertIsInstance(play_war_game()[2],int)
		


















###########
if __name__ == "__main__":
    unittest.main(verbosity=2)