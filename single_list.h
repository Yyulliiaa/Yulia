#include <iostream>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
using namespace std;

int is_subsequence(std::string a, std::string b);
int is_palindrome(std::string a);


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
	void AddNewHead(double x); //добавление в начало списка
	int Size() const; //размер списка
	double HeadVal(); //возвращает значение головы
	void Edge(double x, int place); //добавляет элемент со значением на место
	void Print(); // вывод списка
	void RemoveHead(); //удаление головы
	void Loop(int place); //создание петли (зациклится на позиции)
	bool IsLoop(); // проверяет цикличность
	void Reverse(); // переворачивает
	double Middle(); // возвращает элемент из середины
	void RemoveEl(double x); // удаляет элемент
	
};
