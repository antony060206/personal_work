#include "intSet.h"
#include <iostream>

using namespace std;

intSet::intSet() : data(new int[4]), size(0), capacity(4) {}

intSet::~intSet() {
    delete[] data;
}

intSet::intSet(const intSet& is) : data(new int[is.capacity]), size(is.size), capacity(is.capacity) {
    for (int i = 0; i < size; ++i) {
        data[i] = is.data[i];
    }
}

intSet::intSet(intSet&& is) : data(is.data), size(is.size), capacity(is.capacity) {
    is.data = nullptr;
    is.size = 0;
    is.capacity = 0;
}

intSet& intSet::operator=(const intSet& is) {
    if (this != &is) {
        delete[] data;
        capacity = is.capacity;
        size = is.size;
        data = new int[capacity];
        for (int i = 0; i < size; ++i) {
            data[i] = is.data[i];
        }
    }
    return *this;
}

intSet& intSet::operator=(intSet&& is) {
    if (this != &is) {
        delete[] data;
        data = is.data;
        size = is.size;
        capacity = is.capacity;
        is.data = nullptr;
        is.size = 0;
        is.capacity = 0;
    }
    return *this;
}

bool intSet::contains(int e) const {
    for (int i = 0; i < size; ++i) {
        if (data[i] == e) return true;
    }
    return false;
}

void intSet::add(int e) {
    if (contains(e)) return;
    if (size == capacity) {
        capacity *= 2;
        int* newData = new int[capacity];
        for (int i = 0; i < size; ++i)
            newData[i] = data[i];
        delete[] data;
        data = newData;
    }
    data[size++] = e;
}

void intSet::remove(int e) {
    for (int i = 0; i < size; ++i) {
        if (data[i] == e) {
            data[i] = data[size - 1];
            --size;
            return;
        }
    }
}

bool intSet::isSubset(const intSet &s) const {
    for (int i = 0; i < s.size; ++i) {
        if (!contains(s.data[i])) return false;
    }
    return true;
}

intSet intSet::operator|(const intSet &other) const {
    intSet result;
    for (int i = 0; i < size; ++i)
        result.add(data[i]);
    for (int i = 0; i < other.size; ++i)
        result.add(other.data[i]);
    return result;
}

intSet intSet::operator&(const intSet &other) const {
    intSet result;
    for (int i = 0; i < size; ++i) {
        if (other.contains(data[i])) {
            result.add(data[i]);
        }
    }
    return result;
}

bool intSet::operator==(const intSet &other) const {
    if (size != other.size) return false;
    for (int i = 0; i < size; ++i) {
        if (!other.contains(data[i])) return false;
    }
    return true;
}

std::ostream& operator<<(std::ostream& out, const intSet& is) {
    if (is.size == 0) {
        out << "()";
        return out;
    }

    // Copy and sort manually (insertion sort) since we can't use STL
    int* temp = new int[is.size];
    for (int i = 0; i < is.size; ++i)
        temp[i] = is.data[i];

    for (int i = 1; i < is.size; ++i) {
        int key = temp[i];
        int j = i - 1;
        while (j >= 0 && temp[j] > key) {
            temp[j + 1] = temp[j];
            j--;
        }
        temp[j + 1] = key;
    }

    out << "(";
    for (int i = 0; i < is.size; ++i) {
        out << temp[i];
        if (i < is.size - 1)
            out << ", ";
    }
    out << ")";
    delete[] temp;
    return out;
}
