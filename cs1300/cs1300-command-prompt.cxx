#include <iostream>
#include <string>
#include <direct.h>
using namespace std;

int main(int argc, char* argv[])
{
    char buffer[1000];
    string command;
    
    _getcwd(buffer, 1000);
    command = "cmd.exe /K \"";
    command += buffer;
    command += "\\gocs.bat\" ";
    command += buffer;
    system(command.c_str( ));
    
    return 0;
}
