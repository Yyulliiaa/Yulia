#include "single_list.h"


int is_subsequence(std::string a, std::string b)
{
	List *q = new List();
	for (char el : a) {q -> Add((int)el);}
	for (char el : b) {
		if ((int)el == q -> HeadVal()) {
			q -> RemoveHead();
			if (q->Size() == 0) {return 1;}
		}
	}
	return 0;
}

int is_palindrome(std::string a) {
	List *stack = new List();
	for (char el : a) {stack -> AddNewHead((int)el);}
	for (char el : a) {
		if ((int)el != stack -> HeadVal()) { 
			return 0;
		}
		stack -> RemoveHead();
	}
	return 1;
}


void merge(List *a, List *b) {
	while (b->Size() > 0) {
		a -> EdgeInOrder(b->HeadVal());
		b ->RemoveHead();
	}
	a -> Print();
}




