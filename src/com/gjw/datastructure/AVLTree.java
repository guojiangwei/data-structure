package com.gjw.datastructure;

public class AVLTree<T extends Comparable<? super T> > {
	private AVLNode<T> root;
	private int ALLOWED_BALANCE=1;
	public AVLTree() {
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
	private boolean contains(T d,AVLNode<T> r) {
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
	 private AVLNode<T> remove(T data,AVLNode<T> n) {
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
		 n=balance(n);
		 return n;
	 }
	 
	 public MyLinkedList<T> scanTreeMid() {
		 MyLinkedList<T> list=new  MyLinkedList<T>();
		 scanTreeMid(root,list);
		 return list;
		 
	 }
	 private void scanTreeMid(AVLNode<T> node,MyLinkedList<T> list) {
		 if(node==null) {
			 return;
		 }
		 scanTreeMid(node.left,list) ;
		 list.add(node.data);
		 scanTreeMid(node.right,list) ;
		 
	 }
	/*insert the specified item to this tree
	 * 
	 * */
	public void insert(T data) {
		root=insert(data,root);
	}
	private AVLNode<T> insert(T data,AVLNode<T> root){
		if(root==null) return new AVLNode<T>(data);
		int com=data.compareTo(root.data);
		if(com<0)root.left=insert(data,root.left);
		else if(com>0) root.right=insert(data,root.right);
		root=balance(root);
		return root;
	}
	
	
	private AVLNode<T> balance(AVLNode<T> node){
		if(node==null)return node;
		if(getHeight(node.left)-getHeight(node.right)>ALLOWED_BALANCE) {
		  if(getHeight(node.left.left)>=getHeight(node.left.right)) {
			  node= rotateLeftChild(node);
		  }else node=doubleRotateLeftChild(node);
		}else if(getHeight(node.right)-getHeight(node.left)>ALLOWED_BALANCE) {
			if(getHeight(node.right.right)>=getHeight(node.right.left)) {
				node=rotateRightChild(node);
			}else  node=doubleRotateRightChild(node);
		}
		return node;
	}
	private AVLNode<T> rotateLeftChild(AVLNode<T> node){
		AVLNode<T> node1=node.left;
		node.left=node1.right;
		node1.right=node;
		node.height=Math.max(getHeight(root.left), getHeight(root.right))+1;
		node1.height=Math.max(node.height, getHeight(node1.left))+1;
		return node1;
	}
	private  AVLNode<T> rotateRightChild(AVLNode<T> node){
		AVLNode<T> node1=node.right;
		node.right=node1.left;
		node1.left=node;
		node.height=Math.max(getHeight(root.left), getHeight(root.right))+1;
		node1.height=Math.max(node.height, getHeight(node1.left))+1;
		return node1;
	}
	private AVLNode<T> doubleRotateLeftChild(AVLNode<T> node){
		AVLNode<T> node1=rotateRightChild(node);
		return rotateLeftChild(node1);
	}
	private AVLNode<T> doubleRotateRightChild(AVLNode<T> node){
		AVLNode<T> node1=rotateLeftChild(node);
		return rotateRightChild(node1);
	}
	/*return the max item
	 * 
	 * */
	public T findMax() {
		if(isEmpty()) return null;
		return findMax(root).data;
	}
	private AVLNode<T> findMax(AVLNode<T> node) {
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
	private AVLNode<T> findMin(AVLNode<T> node) {
		if(node.left==null)return node;
		return findMin(node.left);
	}
	private int getHeight(AVLNode<T> node) {
		return node==null?-1:node.height;
	}
	
	private static class AVLNode<T>{
		 T data;
		 AVLNode<T> left;
		 AVLNode<T> right;
		 int height;
		
		public AVLNode(T data) {
			this(data,null,null);
		}
		public AVLNode(T data,AVLNode left,AVLNode right) {
			this.data=data;
			this.left=left;
			this.right=right;
		}

	}



}
