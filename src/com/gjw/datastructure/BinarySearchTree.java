package com.gjw.datastructure;

public class BinarySearchTree<T extends Comparable<? super T> > {
	private TreeNode<T> root;
	public BinarySearchTree() {
		root=null;
	}
	
	public void makeEmpty() {
		root=null;
	}
	public boolean isEmpty() {
		return this.root==null;
	}
	public boolean contains(T d) {
		return contains(d,root);
	}
	/*find an item from the tree
	 * 
	*/
	private boolean contains(T d,TreeNode<T> r) {
		if(r==null)return false;
		int compareResult=d.compareTo(r.data);
		if(compareResult<0) return contains(d,r.left);
		else if(compareResult>0) return contains(d,r.right);
		else return true;
	}
	/**
	 * remove the specified item from this tree
	 */
	 public void remove(T data) {
		 root=remove(data,root);
	 }
	 private TreeNode<T> remove(T data,TreeNode<T> n) {
		 if(n==null)return null;
		 int com=data.compareTo(n.data);
		 if(com<0) {
			 n.left=remove(data,n.left);
		 }else if(com>0) n.right=remove(data,n.right);
		 else if(n.right!=null&&n.left!=null){
			 n.data=findMin(n.right).data;
			 remove(n.data,n.right);
		 }else {
			 n=n.left!=null?n.left:n.right;
			 
		 }
		 return n;
	 }
	/*insert the specified item to this tree
	 * 
	 * */
	public void insert(T data) {
		root=insert(data,root);
	}
	private TreeNode<T> insert(T data,TreeNode<T> root){
		if(root==null) return new TreeNode<T>(data);
		int com=data.compareTo(root.data);
		if(com<0)root.left=insert(data,root.left);
		else if(com>0) root.right=insert(data,root.right);
		return root;
	}
	/*return the max item
	 * 
	 * */
	public T findMax() {
		if(isEmpty()) return null;
		return findMax(root).data;
	}
	private TreeNode<T> findMax(TreeNode<T> node) {
		if(node.right==null) return node;
		return findMax(node.right);
	}
	/*return the min item
	 * 
	 * */
	public T findMin() {
		if(isEmpty()) return null;
		return findMin(root).data;
	}
	private TreeNode<T> findMin(TreeNode<T> node) {
		if(node.left==null)return node;
		return findMin(node.left);
	}
	
	private static class TreeNode<T>{
		public T data;
		public TreeNode<T> left;
		public TreeNode<T> right;
		public TreeNode(T data) {
			this(data,null,null);
		}
		public TreeNode(T data,TreeNode left,TreeNode right) {
			this.data=data;
			this.left=left;
			this.right=right;
		}
	}



}
