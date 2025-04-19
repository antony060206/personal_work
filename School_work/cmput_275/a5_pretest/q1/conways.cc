#include <iostream>
#include <string>

using namespace std;

class GameOfLife {
private:
    char** grid;
    int rows;
    int cols;
    int capacity;  // current allocated rows

public:
    GameOfLife() {
        rows = 0;
        cols = 0;
        capacity = 4;
        grid = new char*[capacity];
    }

    ~GameOfLife() {
        for (int i = 0; i < rows; ++i)
            delete[] grid[i];
        delete[] grid;
    }

    void doubleCapacity() {
        int newCapacity = capacity * 2;
        char** newGrid = new char*[newCapacity];
        for (int i = 0; i < rows; ++i)
            newGrid[i] = grid[i];
        delete[] grid;
        grid = newGrid;
        capacity = newCapacity;
    }

    void readInitialGrid() {
        string line;
        while (getline(cin, line)) {
            if (line == "x")
                break;

            if (cols == 0)
                cols = line.length();
            else if (line.length() != static_cast<size_t>(cols))
                continue;  // skip invalid rows

            if (rows >= capacity)
                doubleCapacity();

            grid[rows] = new char[cols];
            for (int j = 0; j < cols; ++j)
                grid[rows][j] = line[j];
            ++rows;
        }
    }

    void printGrid() {
        for (int i = 0; i < cols; ++i)
            cout << '|';
        cout << '\n';

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j)
                cout << grid[i][j];
            cout << '\n';
        }

        for (int i = 0; i < cols; ++i)
            cout << '|';
        cout << '\n';
    }

    int countNeighbors(int r, int c) {
        int count = 0;
        for (int dr = -1; dr <= 1; ++dr) {
            for (int dc = -1; dc <= 1; ++dc) {
                if (dr == 0 && dc == 0)
                    continue;

                int nr = r + dr;
                int nc = c + dc;

                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    if (grid[nr][nc] == 'O')
                        ++count;
                }
            }
        }
        return count;
    }

    void step() {
        char** newGrid = new char*[rows];
        for (int i = 0; i < rows; ++i)
            newGrid[i] = new char[cols];

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                int neighbors = countNeighbors(i, j);
                if (grid[i][j] == 'O') {
                    if (neighbors < 2 || neighbors > 3)
                        newGrid[i][j] = '.';
                    else
                        newGrid[i][j] = 'O';
                } else {
                    if (neighbors == 3)
                        newGrid[i][j] = 'O';
                    else
                        newGrid[i][j] = '.';
                }
            }
        }

        // Free old grid
        for (int i = 0; i < rows; ++i)
            delete[] grid[i];
        delete[] grid;

        grid = newGrid;
    }

    void run() {
        string cmd;
        while (cin >> cmd) {
            if (cmd == "p") {
                printGrid();
            } else if (cmd == "s") {
                step();
            }
        }
    }
};

int main() {
    GameOfLife game;
    game.readInitialGrid();
    game.run();
    return 0;
}
