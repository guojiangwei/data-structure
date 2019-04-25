package com.gjw.datastructure;

import java.util.Iterator;

public class MyLinkedList<T> implements Iterable<T> {
	private int size = 0;
	private int modCount = 0;
	private Node<T> head;
	private Node<T> tail;

	public MyLinkedList() {
		doClear();
	}

	public void doClear() {
		head = new Node<T>(null, null, null);
		tail = new Node<T>(null, head, null);
		head.next = tail;
		this.size = 0;
		this.modCount++;
	}

	public int getSize() {
		return this.size;
	}

	public boolean isEmpty() {
		return this.size == 0;
	}

	public T get(int i) {
		return this.getNode(i).data;
	}

	///remove the item at the specified  position in this list 
	public T remove(int i) {
		Node<T> node = getNode(i);
		return remove(node);
	}
	//remove the first item from this link list;
	public T remove() {
		return remove(0);
	}

	private T remove(Node<T> node) {
		node.previous.next = node.next;
		node.next.previous = node.previous;
		this.size--;
		this.modCount--;
		return node.data;
	}

	// insert the specified item at the specified index;
	public boolean add(int i, T data) {
		addBefore(getNode(i, 0, this.size), data);
		return true;
	}

	/// add the specified item to the tail of this linklist
	public boolean add(T data) {
		return add(this.size, data);
	}

	private Node<T> getNode(int i) {
		return getNode(i, 0, size);
	}

	/// return a node at the specief position
	private Node<T> getNode(int index, int lower, int upper) {
		if (index < 0 || index > this.size)
			throw new IndexOutOfBoundsException();
		if (index < (this.size >> 1)) {
			Node<T> x = this.head;
			for (int i = 0; i <= index; i++) {
				x = x.next;
			}
			return x;
		} else {
			Node<T> x = this.tail;
			for (int i = this.size; i > index; i--) {
				x = x.previous;
			}
			return x;
		}
	}

	private void addBefore(Node<T> pNode, T data) {
		Node<T> node = new Node<T>(data, pNode.previous, pNode);
		pNode.previous.next = node;
		pNode.previous = node;
		this.size++;
		this.modCount++;
	}

	private static class Node<T> {
		public T data;
		public Node<T> previous;
		public Node<T> next;

		public Node(T c, Node<T> p, Node<T> n) {
			this.data = c;
			this.previous = p;
			this.next = n;
		}
	}

	@Override
	public Iterator<T> iterator() {
		// TODO Auto-generated method stub
		return null;
	}

}
