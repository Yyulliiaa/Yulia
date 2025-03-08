#include "single_list.h"

using namespace std;

List::ListMember::ListMember()
{
	next = nullptr;
}


List::ListMember::~ListMember() {delete next; next = nullptr;}


List::List()
{
	size = 0; head = nullptr;

}


List::~List() 
{
	while (head) {
		ListMember *p = head;
		head = head->next;
        	delete p;
    	}
 }



int List::Size() const {return size;}
	

void List::Add(double x)
{
	ListMember *p = new ListMember;
	p->num = x;
	++size;
	if (!head) {head = p; return;} 
	ListMember *cur = head;
	while (cur->next != nullptr) {
		cur = cur->next;
	}
	cur->next = p;
	//delete p;
}


void List::AddNewHead(double x)
{
	ListMember *p = new ListMember;
	p->num = x;
	++size;

	if (!head) { head = p; } 
	else {
		p->next = head;
       		head = p;
    	}
    	//delete p;
}


void List::Edge(double x, int place)
{
	ListMember *p = new ListMember;
	p->num = x;
	++size;
	if (!head) {head = p; return;} 
	ListMember *cur = head;
	while (cur->next != nullptr && place > 0) {
		cur = cur->next;
		place--;
	}
	p->next = cur->next;
	cur->next = p;
	//delete p;
}




void List::Print()
{
	int len = 0;
	ListMember *cur = head;
	while (len < size) {
		std::cout << cur->num << " ";
		cur = cur->next;
		len++;
	}
	std::cout << std::endl;
}


void List::Loop(int place)
{
	ListMember *cur = head;
	while (cur->next != nullptr && place > 0) {
		cur = cur->next;
		place--;
	}
	ListMember *end = cur;
	while (cur->next != nullptr) {
		cur = cur->next;
	}
	cur->next = end;
}


bool List::IsLoop()
{
	if (size == 1) return 1;
	ListMember *slow = head;
	ListMember *fast = head->next;
	while (fast != slow) {
		if ( fast == nullptr || fast->next == nullptr) return 0;
		slow = slow -> next;
		fast = fast -> next -> next;
	}
	return 1;
}

double List::Middle()
{
	if (size == 1) return head->num;
	ListMember *slow = head;
	ListMember *fast = head->next;
	while (fast != nullptr && fast->next != nullptr) {
		slow = slow -> next;
		fast = fast -> next -> next;
	}
	return slow -> num;
}

void List::Reverse()
{
	ListMember *cur = head;
	ListMember *next = new ListMember();
	ListMember *prev = new ListMember();	
	while (cur != nullptr) {
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	head = prev;
	//delete next, prev;
}

void List::RemoveEl(double x) 
{
	ListMember *dummy = new ListMember();
	dummy->next = head;
	ListMember *prev = dummy;
	ListMember *cur = head;
	while (cur != nullptr) {
		if (abs(cur->num - x) <= 1e-5) {
			prev->next = cur->next;
			size--;
		}
		else {prev = cur;}
		cur = cur->next;	
	}
	head = dummy->next;
	//delete dummy;
}


void List::RemoveHead() 
{
	size--;
	head = head->next;
}

double List::HeadVal() {return head->num;}


