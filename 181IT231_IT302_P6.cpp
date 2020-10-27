// Let X denote the number of times a certain numerical control machine will malfunction: 1, 2, or 3 times on any given day. Let Y denote the number of times 
// a technician is called on an emergency call. Their joint probability distribution is given as Find the covariance of the random variables X and Y by using
// any one of the programming languages C/Python/Java/C++. Program should consider only valid runtime inputs. For invalid test case, it should display an error
// message on the terminal and the same should be stored on a separate output file with appropriate file name. For each valid test cases it should display 
// intermediate results as well as final output on terminal and also should store onto a separate output file with appropriate file name. For each test case 
// save the screenshot with appropriate filename.
#include <bits/stdc++.h>
using namespace std;

float mul(int a, int b)
{
    return a*b;
}
int main()
{
    int n = 1;
    string line, word;

    while (n <= 6)
    {

        string sampleoutput = "181IT231_IT302_P6_Output_TC";
        ofstream outfile;
        sampleoutput.append(to_string(n));
        outfile.open(sampleoutput + ".txt");
        string testno = "Test Case-" + n;
        cout<<endl;
        cout<<"TEST CASE NUMBER : "<<n<<endl;
        vector<int> x;
        vector<int> y;
        float inp[3][3];

        //TAKING INPUTS FOR X
        cout << "Enter the values for X" << endl;
        for (int i = 0; i < 3; i++)
        {
            int temp;
            cin >> temp;
            x.push_back(temp);
        }

        //TAKING INPUT FOR Y
        cout << "Enter the values for Y" << endl;
        for (int i = 0; i < 3; i++)
        {
            int temp;
            cin >> temp;
            y.push_back(temp);
        }

        //TAKING INPUT FOR CORRESPONDING X AND Y VALUES
        cout << "Enter the input values for the matrix row wise" << endl;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                cin >> inp[i][j];
            }
        }
        int nx = x.size();
        int ny = y.size();

        vector<float> g(nx, 0);
        vector<float> h(ny, 0);
        for (int i = 0; i < ny; i++)
        {
            for (int j = 0; j < nx; j++)
            {
                h[i] += inp[i][j];
                g[j] += inp[i][j];
            }
        }
        float miu_x = 0;
        float miu_y = 0;
        for (int i = 0; i < ny; i++)
        {
            miu_y += float(y[i]) * h[i];
        }


        for (int i = 0; i < nx; i++)
        {
            miu_x += float(x[i]) * g[i];
        }


        float exp = 0;
        for (int i = 0; i < ny; i++)
        {
            for (int j = 0; j < nx; j++)
            {
                exp +=  inp[i][j]*mul(x[j], y[i]);
            }
        }

        cout << "Test case No : " << n << endl;
        outfile << "Test case No : " << n << endl;

        cout << "The value of miu_x is : " << miu_x << endl;
        outfile << "The value of miu_x is : " << miu_x << endl;

        cout << "The value of miu_y is: " << miu_y << endl;
        outfile << "The value of miu_y is : " << miu_y << endl;

        cout << "Caluculated value of function E(x,y): " << exp << endl;
        outfile << "Calculated value of function E(x,y): " << exp << endl;

        cout << "FINAL OUTPUT -> " << exp - miu_x * miu_y<<endl;
        outfile<< "FINAL OUTPUT -> " << exp - miu_x * miu_y<<endl;
        outfile.close();
        n++;
    }
    void close();
    return 0;
}