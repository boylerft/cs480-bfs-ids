/*
Authors : Jorge Bautista & Ryan Boyle
*/
#include <time.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <algorithm>
class Node 
{
	public: 
	  Node(int *perm, int par): permutation(perm), parent(par) {} 
	  int getParent()       { return parent; }
	  int *getPermutation() { return permutation; }
	private:
          int parent;
	  int *permutation;
}; 

//const int size = 9;
int maxStack = 1;
void bfs(int *, int const size);
void ids(int *, int, int const size);
void printPath(std::vector<Node *> , int const size);
void printArray(int *arr, int const size);
bool dfs(Node *, int,std::vector<Node *>&, int const size);
bool generateChilds(std::vector<Node *> &, std::queue<Node *> &, std::stack<Node *> &,int, int const size);
bool inOrder(int *, int const size);
bool notEqual(int *, int* , int const size);
int *flip(int *,int, int, int const size);
std::vector<int> getInput();
int convert(std::string x);

int main()
{
  //int vals[size] = {8,7,2,6,9,3,1,5,4};
  std::vector<int> vals = getInput();
  /*
  for (int i = 0; i < vals.size(); i++){
      std::cout << vals[i];
      
  }
  */
  int vals2[vals.size()] = {};
  for (int i = 0; i < vals.size(); i++){
      vals2[i] = vals[i];
  }
  /*
  for (int i = 0; i < sizeof(vals2)/sizeof(vals2[0]); i++){
      std::cout << vals2[i] << "," << std::endl;
      
  }
  */
  //std::cout << std::endl;
  std::cout << "\nRunning bfs... \n";
  bfs(vals2, sizeof(vals2)/sizeof(vals2[0]));
  std::cout << "\nRunning ids... \n";
  //ids(vals2, sizeof(vals2)/sizeof(vals2[0]), sizeof(vals2)/sizeof(vals2[0]));
  return 0;
}

void ids(int *permutation, int maxDepth, int const size)
{
  double cpu0 = clock();
  for(int i = 0 ; i < maxDepth; i ++){
    std::vector<Node *> pointers;
    Node *node = new Node(permutation, -1);
    pointers.push_back(node);
    if(dfs(node, i, pointers, size))
    {
      double cpu1 = clock();
      printPath(pointers, size);
      std::cout << "Total cpu time for ids: " << (cpu1 - cpu0) /CLOCKS_PER_SEC << " seconds \n";
      std::cout << "Total numer of visited states: " << pointers.size() << std::endl;
      std::cout << "Max size of Queue: " << maxStack << std::endl;
      return;
    }
  }
  std::cout << "Could not find.. max depth should increase\n";
  
}

bool dfs(Node *node,int n,std::vector<Node *> &pointers, int const size)
{
  if(n == 0)
    return false;
  
  std::stack<Node *> myStack;
  std::queue<Node *> myQueue;

  pointers.push_back(node);
  myStack.push(node);
  
  if(generateChilds(pointers, myQueue, myStack,0, size))
    return true;
  if(maxStack < myStack.size())
	  maxStack = myStack.size();
  for(int i = 0; i < myStack.size(); i++)
  {
    node = myStack.top();
    myStack.pop();
    if (dfs(node, n - 1,pointers, size))
      return true;
  }
  return false;
}
int convert(std::string x){
    return atoi(x.c_str());
}
std::vector<int> getInput() { 
  std::string xin;
  std::cout << "please enter values to sort: "; 
  std::getline(std::cin,xin);
  std::stringstream stream(xin);
  std::vector<int> vals;
  for (int i = 0; i < xin.length(); i++){
        std::string token;
        while(isdigit(xin[i])){
            char x = xin[i];
            token += x;
            i++;
        }
      //std::cout << token << std::endl;
      int new_int = convert(token);
      //std::cout << new_int << std::endl;
      vals.push_back(new_int);
      
  }
    return vals;
}

void bfs(int *permutation, int const size)
{
  std::vector<Node *> pointers;
  std::queue<Node *> myQueue;
  std::stack<Node *> myStack;
  Node *node = new Node(permutation, -1);
  double cpu0 = clock();
  int maxSize = 1;
  pointers.push_back(node);
  myQueue.push(node);

  while (!myQueue.empty()) {
    if(generateChilds(pointers, myQueue, myStack , 1, size))
    {
      double cpu1 = clock();
      printPath(pointers, size);
      std::cout << "Total cpu time for bfs: " << (cpu1 - cpu0) /CLOCKS_PER_SEC << "seconds \n";
      std::cout << "Total numer of visited states: " << pointers.size() << std::endl;
      std::cout << "Max size of Queue: " << maxSize << std::endl;
      return;
    }

    if(myQueue.size() > maxSize)
       maxSize = myQueue.size();
  }
}

bool generateChilds(std::vector<Node *> &pointers, std::queue<Node *> &myQueue, std::stack<Node *> &myStack,int ch, int const size)
{
  Node *node;
  if(ch == 1) {
    node = myQueue.front();
    myQueue.pop(); }
  else{
    node = myStack.top();
    myStack.pop(); }

  int parentIdx = find(pointers.begin(), pointers.end(), node) - pointers.begin();
  int nodeParent = node->getParent();
  int *pPerm;
  if(nodeParent != -1) {
	Node *pNode = pointers.at(nodeParent);
	pPerm = pNode->getPermutation(); }

  int *perm = node->getPermutation();
  for(int i = 1 ; i < size; i++) {
    for(int j = 0 ; j < size ; j ++) {	
      if( (j + i ) > size - 1) 
	break;

      int *newPerm = flip(perm, i + j, j, size);

      if(notEqual(pPerm,newPerm, size)) {
	Node *leaf = new Node(newPerm, parentIdx);
	pointers.push_back(leaf);

	if(inOrder(newPerm, size))
          return true;

        if(ch == 1)
	  myQueue.push(leaf);
        else
	  myStack.push(leaf);

      }
    }
  }
  return false;
}

int *flip(int *permutation, int endIdx,int startingIdx, int const size)
{
  int *tempArr = (int *)malloc(sizeof(int)* size); 
  for(int i = 0; i < size; i ++) 
    tempArr[i] = permutation[i]; 
	
  int tempVal = 0;
  while(startingIdx < endIdx) {	
    tempVal = tempArr[startingIdx];
    tempArr[startingIdx] = tempArr[endIdx]; 
    tempArr[endIdx] = tempVal;
    endIdx --;
    startingIdx ++;
   }	
   return tempArr;
}

bool inOrder(int *arr, int const size)
{
  for(int i = 0; i < size - 1; i++)
    if(arr[i] > arr[i + 1])
      return false;
  return true;
}


void printArray(int *arr, int const size)
{
  for(int i = 0; i < size; i ++)
    std::cout << arr[i] << ",";
}

void printPath(std::vector<Node *> pointers, int const size)
{
  std::vector<int *> vals;
  Node *node = pointers.at(pointers.size() - 1);
  while(node->getParent() != -1)
  {
    //printArray(node->getPermutation());
    vals.push_back(node->getPermutation());
    node = pointers.at(node->getParent());
  }
  //printArray(node->getPermutation());
  vals.push_back(node->getPermutation());
  for(int i = vals.size() - 1; i > -1 ; i--)
  {
    printArray(vals.at(i), size);
    std::cout << "-> ";
  }
  std::cout<< "\n";

}

bool notEqual(int *aOne, int *aTwo, int const size)
{
  for(int i = 0 ; i < size; i ++)
    if (aOne[i] != aTwo[i])
      return true;
  return false;
}