#include <iostream>

using namespace std;

int main(){
    int a = 0, b = 0;
    cin >> a >> b;
    int ans = (a + b) % 12;
    cout << (ans ? ans : 12);
    return 0;
}