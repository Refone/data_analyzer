#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

#define MAX_SIZE 1000

using namespace std;

int t[MAX_SIZE];

// .cdf input.dat privacy
int main(int argc, char**argv)
{
	int n = 0;
	int p = 0;
	int i;
	FILE *input;
	//FILE *output;

	if (argc != 4) {
		//cout<<"Usage: ./cdf input.data  data_numer  privacy.\n"<<endl;
		printf("Usage: ./cdf input.data  data_numer  privacy.\n");
		return 0;
	}

	n = atoi(argv[2]);
	p = atoi(argv[3]);


	if((input = fopen(argv[1],"r"))==NULL) {  
			printf("file cannot be opened/n");   
			return -1;
	}  

	//ifstream infile(argv[1]);
	char line[20];
    //string line;

	for (i=0; i<n; i++) {
		//getline(infile,line);
		//t[i] = atoi(line.c_str());
		getline(input,line);
		t[i] = atoi(line);
	}

	for (i=0; 1<n; i++) {
		//cout<<t[i]<<" ";
		printf("%d ", t[i]);
	}

	//cout<<endl;
	printf("\n");

	return 0;
}
