#include<iostream>
#include <vector>

struct Tree {
    int val;
    Tree *left;
    Tree *right;
}

void insert(Tree *root, int x) {
    if (root == NULL) 
        Tree ;
    if (root->val < x) 
        return insert(root->left, x);
    else
        return insert(root->right, x); 
}

void delete(Tree *root, int x) {
    if (root->val == x) {
        
    }
}

class stack() {
    vector<int> st;
    void Push(int x) {
        st.push_back(x);
    }
    void Pop() {
        int v = st.back();
        st.pop_back();
        return v;
    }
    void Display() {
        for (int i = 0; i < st.size(); i++)
            printf("%d ", st[i]);
        printf("\n");
    }
}