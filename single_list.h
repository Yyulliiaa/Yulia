#include <iostream>
using namespace std;


class List 
{
private:
	struct ListMember
	{
		double num;
		ListMember *next;
		ListMember();
		~ListMember();
	};
	ListMember *head;
	int size;	
public:
	
	List();
	~List();	

	void Add(double x); //добавление в конец списка
	void AddNewHead(double x);
	int Size() const;
	void Edge(double x, int place);
	void Print();
	
	
	
	void Loop(int place);
	bool IsLoop();
	void Reverse();
	double Middle();
	
};
