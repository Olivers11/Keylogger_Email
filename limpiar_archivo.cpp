#include <iostream>
#include <string>
#include <fstream>
using namespace std;


int main()
{
	FreeConsole();
	ofstream archivo;
	archivo.open("bad_file.txt", ios::out);
	if(archivo.fail())
	{
		cout << "Deja de ser pendejo xd" << endl;
		exit(3);
	}
	else
	{
		archivo << "" << endl;
	}
	archivo.close();
}
