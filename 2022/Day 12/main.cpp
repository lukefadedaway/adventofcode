//
//  main.cpp
//  AdventOfCode
//
//  Created by Lukas Görtz on 12.12.22.
//

#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <list>
#include <vector>
#include <queue>

typedef long long ll;

using namespace std;
#define INF 0x3f3f3f3f

typedef pair<int, int> iPair;

class Graph {
    int V;
    list<pair<int, int> >* adj;
    
public:
    Graph(int V);
    void addEdge(int u, int v, int w);
    int shortestPath(int s, int d);
};

Graph::Graph(int V) {
    this->V = V;
    adj = new list<iPair>[V];
}

void Graph::addEdge(int u, int v, int w) {
    adj[u].push_back(make_pair(v, w));
//    adj[v].push_back(make_pair(u, w));
}

int Graph::shortestPath(int src, int dest) {
    priority_queue<iPair, vector<iPair>, greater<iPair> >
    pq;
    vector<int> dist(V, INF);
    pq.push(make_pair(0, src));
    dist[src] = 0;
    
    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        
        list<pair<int, int> >::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i) {
            int v = (*i).first;
            int weight = (*i).second;
            
            if (dist[v] > dist[u] + weight) {
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }
    return dist[dest];
}

bool isStepValid(char src, char dest) {
    char source, destination;
    if(src == 'S') {source = 'a';} else source = src;
    if(dest == 'E') {destination = 'z';} else destination = dest;
    return ((source - destination) > -2);
}

int main() {
    vector<string> nodes;
    string s;
    while (getline(cin, s)) {
        nodes.push_back(s);
    }
    
    int V = (int) (nodes.size() * nodes[0].length());
    Graph g(V);
    int posOfSource = 0;
    int posOfDest = 0;
    vector<int> starta;
    
    for(int i = 0; i<nodes.size(); i++){
        for (int j = 0; j<nodes[i].length(); j++) {
            if(nodes[i][j] == 'S') posOfSource = (int) (nodes[i].length() * i + j);
            if(nodes[i][j] == 'E') posOfDest = (int) (nodes[i].length() * i + j);
            if(nodes[i][j] == 'a') starta.push_back((int) (nodes[i].length() * i + j));
            if(i<nodes.size() - 1)
                if(isStepValid(nodes[i][j], nodes[i+1][j])) g.addEdge((int) (nodes[i].length() * i + j), (int) (nodes[i].length() * (i+1) + j), 1);
            if(i>0)
                if(isStepValid(nodes[i][j], nodes[i-1][j])) g.addEdge((int) (nodes[i].length() * i + j), (int) (nodes[i].length() * (i-1) + j), 1);
            if(j>0)
                if(isStepValid(nodes[i][j], nodes[i][j-1])) g.addEdge((int) (nodes[i].length() * i + j), (int) (nodes[i].length() * i + (j-1)), 1);
            if(j<nodes[i].length() - 1)
                if(isStepValid(nodes[i][j], nodes[i][j+1])) g.addEdge((int) (nodes[i].length() * i + j), (int) (nodes[i].length() * i + (j+1)), 1);
        }
    }
    int starts = g.shortestPath(posOfSource, posOfDest);
    cout << "Part 1: " << starts << endl;
    int min_starta = starts, besta = posOfSource;
    for(auto& x: starta) {
        starts = g.shortestPath(x, posOfDest);
        if(starts < min_starta) {
            min_starta = starts;
            besta = x;
        }
    }
    cout << "Part 2: " << min_starta << endl;
    return 0;
}
