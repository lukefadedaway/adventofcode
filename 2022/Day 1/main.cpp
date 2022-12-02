//
//  main.cpp
//  AdventOfCode
//
//  Created by Lukas Görtz on 01.12.22.
//

#include <map>
#include <string>
#include <iostream>
#include <sstream>

typedef long long ll;

using namespace std;

void print_map(const std::map<ll, int>& m)
{
    // iterate using C++17 facilities
    for (const auto& [key, value] : m)
        std::cout << '[' << key << "] = " << value << "; " << '\n';
}

int main(int argc, const char * argv[]) {
    
    std::map<ll, int> elves;
    int elf = 0;
    ll calories = 0;
    
    string line;
    while (getline(cin, line)) {
        if(line.empty()){
//            elves.insert({calories,elf});
            elves[calories] = elf;
//            cout << "calories: " << calories << ", elf: " << elf << endl;
            calories = 0;
            elf++;
            continue;
        }
        if(stoll(line) < 0) break;
        calories += stoll(line);
    }
//    print_map(elves);
    auto it=elves.end();
    it--;
    ll maxcal = it->first;
    int theelf = it->second;
    cout << "Part 1:" << endl;
    cout << "Calories: " << maxcal << " by Elf: " << theelf << endl;
    it--;
    maxcal += it->first;
    int the2elf = it->second;
    it--;
    maxcal += it->first;
    int the3elf = it->second;
    cout << "Part 2:" << endl;
    cout << "Calories: " << maxcal << " by Elves: " << theelf << ", " << the2elf << ", " << the3elf << endl;
    
    return 0;
}
