#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Grid {
    int width = 0;
    int height = 0;
    int capacity = 4;

    char** current = nullptr;
    char** next = nullptr;

    void allocate(int rows, int cols) {
        current = new char*[rows];
        next = new char*[rows];
        for (int i = 0; i < rows; ++i) {
            current[i] = new char[cols + 1];  // +1 for null terminator
            next[i] = new char[cols + 1];
        }
    }

    void deallocate() {
        for (int i = 0; i < height; ++i) {
            delete[] current[i];
            delete[] next[i];
        }
        delete[] current;
        delete[] next;
    }

    int countAliveNeighbors(int y, int x) {
        int count = 0;
        for (int dy = -1; dy <= 1; ++dy) {
            for (int dx = -1; dx <= 1; ++dx) {
                if (dy == 0 && dx == 0) continue; // skip self
                int ny = y + dy;
                int nx = x + dx;
                if (ny >= 0 && ny < height && nx >= 0 && nx < width) {
                    if (current[ny][nx] == 'O') {
                        count++;
                    }
                }
            }
        }
        return count;
    }

public:
    Grid() {
        allocate(capacity, capacity);
    }

    ~Grid() {
        deallocate();
    }

    void readGrid() {
        string line;
        int lineNum = 0;

        while (getline(cin, line)) {
            if (line == "x") break;

            if (lineNum >= capacity) {
                // Double capacity
                int newCap = capacity * 2;
                char** newCur = new char*[newCap];
                char** newNext = new char*[newCap];
                for (int i = 0; i < capacity; ++i) {
                    newCur[i] = current[i];
                    newNext[i] = next[i];
                }
                for (int i = capacity; i < newCap; ++i) {
                    newCur[i] = nullptr;
                    newNext[i] = nullptr;
                }
                delete[] current;
                delete[] next;
                current = newCur;
                next = newNext;
                capacity = newCap;
            }

            int len = line.length();
            if (width < len) width = len;

            current[lineNum] = new char[len + 1];
            next[lineNum] = new char[len + 1];

            for (int i = 0; i < len; ++i) {
                current[lineNum][i] = line[i];
                next[lineNum][i] = line[i];
            }
            current[lineNum][len] = '\0';
            next[lineNum][len] = '\0';

            ++lineNum;
        }

        height = lineNum;
    }

    void printGrid() const {
        for (int i = 0; i < width; ++i) cout << '|';
        cout << '\n';
        for (int i = 0; i < height; ++i) {
            cout << current[i] << '\n';
        }
        for (int i = 0; i < width; ++i) cout << '|';
        cout << '\n';
    }

    void updateGrid() {
        for (int y = 0; y < height; ++y) {
            for (int x = 0; x < width; ++x) {
                int alive = countAliveNeighbors(y, x);
                if (current[y][x] == 'O') {
                    if (alive < 2 || alive > 3)
                        next[y][x] = '.';
                    else
                        next[y][x] = 'O';
                } else {
                    if (alive == 3)
                        next[y][x] = 'O';
                    else
                        next[y][x] = '.';
                }
            }
        }

        // Swap pointers
        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                current[i][j] = next[i][j];
            }
        }
    }
};

int whitespace(char c) {
    return c == ' ' || c == '\n' || c == '\r' || c == '\t';
}

char getNext() {
    char c = getchar();
    while (whitespace(c)) c = getchar();
    return c;
}

int main() {
    Grid g;
    g.readGrid();

    char cmd;
    while (cin >> cmd) {
        if (cmd == 's') {
            g.updateGrid();
        } else if (cmd == 'p') {
            g.printGrid();
        }
    }

    return 0;
}
