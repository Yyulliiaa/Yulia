#include "single_list.h"
void reverse(List *B);

int main() {
	List *A = new List();
	for (int i = 0; i < 12; i++) {
		A->Add(i);
	}
	//A->Loop(2);
	A->Print();
	
	
	if (A->IsLoop()) cout<< "Yes\n";
	else cout << "No\n";
	
	reverse(A);
	A -> Print();
	cout << A -> Middle() << endl;

	return 0;

}


void reverse(List* B) {
	B -> Reverse();
}
