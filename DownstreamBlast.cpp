//This script merge result file
// usage:  g++ DownstreamBlast.cpp -o DownstreamBlast
// ./DownstreamBlast outtabular.txt result.txt
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <dirent.h>
#include <vector>
#include <sstream>

using namespace std;

int main(int argc, char *argv[])
{
int checkFile(ifstream &input); 

if (argc!=3){
	cout<<"usage: ./DownstreamBlast yourTabularFile.txt outpurFile.txt"<< endl <<flush;
	return 1;
}
//open file
ifstream inputTable;
inputTable.open(argv[1]);
checkFile(inputTable);
string table;
string temp;

//file for result
ofstream myfile;
myfile.open (argv[2]);

while(getline(inputTable,table))
{
	if(table.substr(0,1)==("#")) continue;
	if(table=="") continue;
	istringstream ss (table);
	//this add data into the column (second number)
	vector <string> record;
		while (ss)
		{
			string s1;
			if(!getline(ss,s1,'	')) break;
			if(s1!=""){
				record.push_back(s1);
			}
		}
		//write result file
		if (temp!=record[0]){
			temp=record[0];
			myfile << table +"\n";
		}		

}//while
inputTable.close();




return 0;
}
//this is end of main

// check openfile
int checkFile(ifstream &input)
{
	if(input.fail()){                           //    Check open
       cerr << "Can't open file\n";
       exit(EXIT_FAILURE);
       //return 1;
	}else{return 0;}
}
