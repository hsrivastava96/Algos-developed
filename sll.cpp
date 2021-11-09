#include<iostream>
using namespace std;

class L
{
    public:
    
    struct Node
    {
        int data;
        Node *next;
    };
    typedef struct Node node;
    
    node *head;
    
    L()
    {
        head = NULL;
    }
    
    void push(int val)
    {
        node *newNode;
        newNode = new node;
        newNode->data = val;
        newNode->next = NULL;
        
        if(head == NULL)
            head = newNode;
        else
        {
            node *temp;
            temp = new node;
            temp = head;
            while(temp->next != NULL)
                temp = temp->next;
            temp->next = newNode;
        }
    }
    
    void printForwards()
    {
        node *temp;
        temp = new node;
        temp = head;
        while(temp != NULL)
        {
            cout<<temp->data;
            temp = temp->next;
        }
    }
    
    void printBackwardsRecursively(node *Temp)
    {
        if(Temp->next == NULL)
        {
            cout<<Temp->data;
            return;
        }
        else
            printBackwardsRecursively(Temp->next);
        cout<<Temp->data;
        return;
    }
};

int main()
{
    L ob;
    int i = 1;
    while(i < 11)
    {
        ob.push(i);
        i++;
    }
    ob.printBackwardsRecursively(ob.head);
    cout<<"\n";
    ob.printForwards();
}










