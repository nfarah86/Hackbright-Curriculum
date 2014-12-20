import unittest
import stacksQueueDequeue

class Test_stacksQueueDequeue(unittest.TestCase):

	def setUp(self):
		pass

	def test_revstring(self):
		case1 = stacksQueueDequeue.revstring('elppa')
		self.assertTrue(case1)
		case2 = stacksQueueDequeue.revstring('x')
		self.assertTrue(case2)

	def test_checkToSeeIfParanBalance(self):
		case1 = stacksQueueDequeue.checkToSeeIfParanBalance('(()))')
		self.assertFalse(case1)
		case2 = stacksQueueDequeue.checkToSeeIfParanBalance('(')
		self.assertTrue(case2)

	def test_checkMultipleTypesBrackets(self):
		case1 = stacksQueueDequeue.checkMultipleTypesBrackets('()')
		self.assertTrue(case1)
		case2 = stacksQueueDequeue.checkMultipleTypesBrackets('()[')
		self.assertFalse(case2)

if __name__ == '__main__':
	unittest.main()
