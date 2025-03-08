#include <cassert>
#include "single_list.h"


void test_middle() {
	List *A = new List();
	for (int i = 0; i < 2; i++) {
		A->Add(i);
	}
	assert(A->Middle() == 0);
	for (int i = 2; i < 13; i++) {
		A->Add(i);
	}
	assert(A->Middle() == 6);
	
}

void test_cycle() {
	List *A = new List();
	for (int i = 0; i < 12; i++) {
		A->Add(i);
	}
	assert(A->IsLoop() == 0);
	A->Loop(2);
	assert(A->IsLoop() == 1);
	
}

void test_subsequence() {
	std::string a = "abc";
	std::string b = "avbcn";
	std::string c = "acnnn";
	assert(is_subsequence(a, b) == 1);
	assert(is_subsequence(a, c) == 0);
}

void test_palindrome() {
	std::string a = "abcba";
	std::string b = "avbcn";
	assert(is_palindrome(a) == 1);
	assert(is_palindrome(b) == 0);
}

int main() {
	List *A = new List();
	for (int i = 0; i < 12; i++) {
		A->Add(i);
	}
	A->Print();
	cout << "перевернем: \n";
	A -> Reverse();
	A -> Print();
	cout << "удалим 3: \n";
	A -> RemoveEl(3);
	A -> Print();
	cout << "удалим 15 (такого элемента нет): \n";
	A -> RemoveEl(15);
	A -> Print();
	//delete A;
	

	
	List *B = new List();
	for (int i = 0; i < 12; i+= 3) {
		B->Add(i);
	}
	List *C = new List();
	for (int i = 1; i < 17; i+= 4) {
		C->Add(i);
	}
	cout << "Отсортированные списки:\n";
	B -> Print();
	C -> Print();
	cout << "Их слияние:\n";

	merge(B, C);	
	
	
	test_middle();
	test_cycle();
	test_subsequence();
	test_palindrome();
	cout << "прошли все тесты \n";
	return 0;
}
