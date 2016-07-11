/*************************************************************************
	> File Name: read_file.cpp
	> Author: Arcs
	> Mail: lizhifeng2009@126.com
	> Created Time: Tue 19 Jan 2016 06:14:51 PM CST
 ************************************************************************/

#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<unistd.h>
#include<sstream>
#include<stdio.h>
using namespace std;

void get_patentid_ipcs(string filename, map< string, set<int> > &id_ipcs)
{
    fstream f(filename.c_str());

    int ipc;

    string patent_id;
    f >> patent_id;
       
    while(!f.eof())
    {
        f >> ipc;
        id_ipcs[patent_id].insert(ipc);

        if(f.peek() == '\n')
        {
            f >> patent_id;
        }
    }
}

int main(int argc, char **argv)
{

    FILE *fp;
    char buffer[1000];
    fp = popen("ls ./", "r");
    size_t len = fread(buffer,sizeof(char), sizeof(buffer), fp);
    cout << len << endl;
    pclose(fp);

    stringstream ss;
    ss << buffer;

    string filename;
    string target("file");
    vector<string>  file_list;
    while(ss >> filename)
    {
        if(filename.compare(0, target.length(), target ) == 0)
            file_list.push_back(filename);
    }

    map< string, set<int> > id_ipcs;

    for(auto v: file_list)
    {
        get_patentid_ipcs(v, id_ipcs);
    }

    for(auto v: id_ipcs)
    {
        
        cout << v.first << " : ";
        for(auto ipc: v.second)
        {
            cout << ipc  << " ";
        }

        cout << endl;
    }

    int nvecs = id_ipcs.size();
    int nnz = 0;

    cout << nvecs << endl;


    set<int> ipc_set;
    for(auto patent_vec : id_ipcs)
    {
        for(auto v : patent_vec.second)
        {
            ipc_set.insert(v);
            nnz++;
        }
    }
    
    map<int, int> ipc_index;
    int index = 0;
    for(auto v : ipc_set)
    {
        ipc_index[v] = index;
        index++;
    }

    cout << nnz << endl;

    float *h_feat = new float[nnz];
    for(int i=0; i<nnz; ++i)
    {
        h_feat[i] = 1.0;
    }

    int *h_featCsrColIndex = new int[nnz];
    int *h_featCsrPtr = new int[nvecs + 1];
    h_featCsrPtr[0] = 0;
    int row = 1;
    int *p = h_featCsrColIndex;
    for(auto patent_vec : id_ipcs)
    {
        int num = 0;
        for(auto v : patent_vec.second)
        {
            *p = ipc_index[v];
            p++;
            num++;
        }
        cout << "num is " << num << endl;
        h_featCsrPtr[row] = h_featCsrPtr[row-1] + num;
        row++;
    }

    for(int i=1; i <= nvecs; ++i)
    {

        for(int j=h_featCsrPtr[i-1];j<h_featCsrPtr[i];++j)
        {
            cout << h_featCsrColIndex[j] << " "  ;
        }
        cout << endl;
    }

    return 0;


}
