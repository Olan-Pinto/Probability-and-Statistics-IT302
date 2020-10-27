// Assume that X and Y have the following joint probability function: Use any one of the programming languages C/Python/Java/C++ to compute (a) μX and μY, 
// (b) expected value of g (X, Y) = X2+Y2. Programshould consider given input file (.xlsx) that consists of set of test cases and it should consider one test
// case at time to compute the aforesaid. Further, it should stop only after completion of all test cases. For each test cases it should display intermediate
// results as well as final output on terminal and also should store onto a separate output file. For invalid test cases, it should display an error message on 
// terminal and the same should be stored on a separate output file.
#include<bits/stdc++.h>
using namespace std;
bool isempty(string line){
    if (line.compare(",,,,,,,,,,,,,,") == 0){
        return true;
    }
    return false;
}
float G(int x, int y){
    return pow(x, 2) + pow(y, 2);
}
int main(){
    int testcase = 1;
    string line, word;
    ifstream ip("Test-Cases-IT302-Lab-Program-5.csv");
    if(!ip.is_open()) cout<<"Error: File not opened";
    while(testcase<=6){
        string opfile = "181IT231_IT302_P5_Output_TC";
        ofstream outfile;
        opfile.append(to_string(testcase));
        outfile.open(opfile+".txt");

        //READING INPUT FROM CSV FILE
        string tok = "Test Case-" + testcase;
        while (getline(ip, line))
        {
            if(line.find(tok) != string::npos){
                break;
            }
            else continue;
        }
        vector<int> x;
        vector<int> y;
        vector<vector<float>> mat;
        getline(ip, line);
        stringstream s(line);
        while(getline(s, word, ',')){
            if(word[0]>='0' && word[0]<='9'){
                x.push_back(stoi(word));
            }
        }
        while(1){
            getline(ip, line);
            stringstream ss(line);
            bool flag = true;
            if(!isempty(line)){
                mat.push_back({});
                while(getline(ss, word, ',')){
                    if(word!="" and word!="y"){
                        if(flag){
                            if (word[0] >= '0' and word[0] <= '9')
                            {
                                y.push_back(stoi(word));
                            }
                            flag = false;
                        }
                        else{
                            mat[mat.size()-1].push_back(stof(word));
                        }
                    }
                }
            }
            else break;
        }
        
        //LOGIC OF THE PROGRAM BEGINS HERE
        int nx = x.size();
        int ny = y.size();
        vector<float> g(nx, 0);
        vector<float> h(ny, 0);
        for(int i = 0; i<ny; i++){
            for(int j = 0; j<nx; j++){
                h[i]+=mat[i][j];
                g[j]+=mat[i][j];
            }
        }

        float miu_x = 0;
        float miu_y = 0;
        for(int i = 0; i<nx; i++){
            miu_x += float(x[i])*g[i];
        }
        for(int i = 0; i<ny; i++){
            miu_y += float(y[i])*h[i];
        }
        float exp = 0;
        for(int i = 0; i<ny; i++){
            for(int j = 0; j<nx; j++){
                exp+= G(x[j], y[i])*mat[i][j];
            }
        }
        cout<<"miu_x: "<<miu_x<<endl;
        outfile<<"miu_x: "<<miu_x<<endl;
        cout<<"miu_y: "<<miu_y<<endl;
        outfile<<"miu_y: "<<miu_y<<endl;
        cout<<"Expected value of G(x,y) is : "<<exp<<endl;
        outfile<<"Expected value of G(x,y) is : "<<exp<<endl;
        outfile.close();
        testcase++;
    }
}