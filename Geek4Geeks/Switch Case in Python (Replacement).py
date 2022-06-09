#https://www.geeksforgeeks.org/switch-case-in-python-replacement/

# Function to convert number into string
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")


# Driver program
if __name__ == "__main__":
    argument = 0
    print(numbers_to_strings(argument))

'''
#include<bits/stdc++.h>
using namespace std;
 
// Function to convert number into string
string numbers_to_strings(int argument){
    switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";
    };
};
 
// Driver program
int main()
{
    int argument = 0;
    cout << numbers_to_strings(argument);
    return 0;
}
'''