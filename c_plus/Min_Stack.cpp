#include<iostream>
#include<vector>
using namespace std;

class MinStack {
    vector<int> stack;
    vector<int> min_stack;
public:
    /** initialize your data structure here. */
    MinStack() {

    }
    
    void push(int val) {
        stack.push_back(val);
        if (min_stack.size() == 0) {
            min_stack.push_back(val);
            return;
        }
        if (val <= min_stack.back()) {
            min_stack.push_back(val);
        } else {
            min_stack.push_back(min_stack.back());
        }
    }
    
    void pop() {
        if (stack.size() > 0) {
            min_stack.pop_back();
            stack.pop_back();
        }
            
    }
    
    int top() {
        return stack.back();
        
    }
    
    int getMin() {
        return min_stack.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */