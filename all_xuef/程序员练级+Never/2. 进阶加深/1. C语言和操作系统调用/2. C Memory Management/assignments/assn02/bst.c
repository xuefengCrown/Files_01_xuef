#include <stdio.h>
#include <stdlib.h>
#include "bst.h"

/*
 * Creates a new node from a given value, allocating heap memory for it.
 */
node_t* make_tree(int val) {
  node_t* new_tree = malloc(sizeof(node_t));
  new_tree->val = val;
  new_tree->left = NULL;
  new_tree->right = NULL;
  return new_tree;
}

/*
 * Inserts a new value into a given binary search tree, allocating heap memory
 * for it.
 */
node_t* insert(int val, node_t* cur_root) {
  /* YOUR CODE HERE */
  node_t* p = make_tree(val);
  if(cur_root == NULL){
	  cur_root = p;
  }else if(val < cur_root->val){
	  cur_root->left = insert(val, cur_root->left);
  }else{
	  cur_root->right = insert(val, cur_root->right);
  }
  return cur_root;
}

bool find_val(int val, node_t* root) {
  /* YOUR CODE HERE */
  if(root == NULL){
	  return FALSE;
  }else if(val == root->val){
	  return TRUE;
  }else if(val < root->val){
	  return find_val(val, root->left);
  }else{
	  return find_val(val, root->right);
  }
}

/*
 * Given a pointer to the root, frees the memory associated with an entire tree.
 */
void delete_bst(node_t* root) {
  /* YOUR CODE HERE */
  if(root == NULL) return;
  node_t* left = root->left;
  node_t* right = root->right;
  free(root);
  delete_bst(left);
  delete_bst(right);
}

/* Given a pointer to the root, prints all o fthe values in a tree. */
void print_bst(node_t* root) {
  if (root != NULL) {
    printf("%d ", root->val);
    print_bst(root->left);
    print_bst(root->right);
  }
  return;
}
