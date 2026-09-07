# 🧠 Data Structures & Algorithms in Python

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Topic](https://img.shields.io/badge/Topic-Data%20Structures%20%26%20Algorithms-orange?style=for-the-badge)](https://github.com/namaysingh3925/dsa-code-)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=for-the-badge)](https://github.com/namaysingh3925/dsa-code-/pulls)

<p align="center">
  <strong>A clean, beginner-friendly collection of foundational Data Structures and Algorithms implemented from scratch in Python with interactive CLI menus.</strong>
</p>

[Explore Files](#-repository-structure) • [Data Structures](#-implemented-data-structures) • [Complexity Table](#-time--space-complexity) • [Getting Started](#-getting-started)

---

</div>

## 📖 Overview

This repository contains robust, modular Python implementations of core **Data Structures and Algorithms**. Each implementation is built from the ground up to emphasize fundamental computer science concepts, memory pointers, pointer manipulation, algorithmic workflows, and interactive terminal-based interfaces.

---

## 🗂️ Repository Structure

```plaintext
dsa/
├── 📊 Arrays & Matrices
│   ├── 1d_array.py                 # 1D Array statistics (Sum, Min, Max, Average)
│   ├── 2d_array.py                 # 2D Matrix addition & subtraction
│   └── matrix_multiplication.py    # Matrix multiplication & transposition
│
├── 🔗 Linked Lists
│   ├── singly_linked_list.py       # Full Singly Linked List (SLL) with CLI menu
│   ├── link_list.py                # Singly Linked List baseline demonstration
│   └── double_link_list.py         # Doubly Linked List (DLL) with bidirectional traversal
│
├── 🥞 Stacks & Applications
│   ├── stackk.py                   # Dynamic List-based Stack implementation
│   ├── stack_linked_list.py        # Linked List-based Stack with CLI menu
│   ├── parenthesess.py             # Balanced parenthesis validator using stack
│   ├── infix_to_postfix.py         # Shunting-yard Infix to Postfix expression converter
│   └── postfiix.py                 # Postfix (Reverse Polish Notation) arithmetic evaluator
│
├── 📬 Queues
│   ├── queue_using_list.py         # Standard Queue (FIFO) using Python lists
│   ├── queue_linked_list.py        # Queue using Singly Linked List (O(1) Enqueue/Dequeue)
│   └── circular_queue.py           # Circular Queue with fixed capacity & modulo wrap-around
│
├── 🌳 Trees
│   └── binry_tree.py               # Binary Tree with Preorder, Inorder & Postorder traversals
│
├── 🕸️ Graphs
│   └── graph_list.py               # Graph representation via Adjacency Matrix & Adjacency List
│
└── 🛠️ Utilities
    └── simple_cal.py               # Menu-driven terminal calculator
```

---

## 🚀 Implemented Data Structures & Algorithms

### 1. 📊 Arrays & Matrices
- **1D Array Analysis** ([`1d_array.py`](1d_array.py)): Calculates sum, arithmetic mean, minimum, and maximum in $O(n)$ time.
- **2D Matrix Arithmetic** ([`2d_array.py`](2d_array.py)): Row/column element-wise matrix addition and subtraction.
- **Matrix Multiplication & Transpose** ([`matrix_multiplication.py`](matrix_multiplication.py)): Dimension validation check ($C_1 == R_2$) followed by standard matrix multiplication and matrix transposition.

### 2. 🔗 Linked Lists
- **Singly Linked List (SLL)** ([`singly_linked_list.py`](singly_linked_list.py)):
  - Node definition: `data`, `next` pointer
  - Operations: `insertAtBeginning()`, `insertAtLast()`, `removeAtBeginning()`, `removeAtLast()`, `traversal()`
- **Doubly Linked List (DLL)** ([`double_link_list.py`](double_link_list.py)):
  - Node definition: `data`, `prev` pointer, `next` pointer
  - Bidirectional node linking with boundary handling for head and tail operations.

### 3. 🥞 Stacks & Stack Applications
- **Stack Implementations** ([`stackk.py`](stackk.py), [`stack_linked_list.py`](stack_linked_list.py)):
  - LIFO (Last-In-First-Out) operations: `push()`, `pop()`, `peek()`, `is_empty()`, `traversal()`.
- **Expression Parsing & Matching**:
  - **Balanced Parentheses** ([`parenthesess.py`](parenthesess.py)): Validates nested bracket symbols `()`, `[]`, `{}`.
  - **Infix to Postfix** ([`infix_to_postfix.py`](infix_to_postfix.py)): Converts arithmetic expressions using operator precedence and stack buffering.
  - **Postfix Evaluator** ([`postfiix.py`](postfiix.py)): Evaluates RPN mathematical expressions via stack operand unwinding.

### 4. 📬 Queues
- **Linear Queue** ([`queue_using_list.py`](queue_using_list.py), [`queue_linked_list.py`](queue_linked_list.py)):
  - FIFO (First-In-First-Out) queueing with front & rear pointers.
- **Circular Queue** ([`circular_queue.py`](circular_queue.py)):
  - Memory-efficient circular buffer utilizing modulo arithmetic `(rear + 1) % MAX_CAPACITY` to prevent false overflow conditions.

### 5. 🌳 Trees
- **Binary Tree** ([`binry_tree.py`](binry_tree.py)):
  - Node struct with `left`, `right`, and `parent` references.
  - Depth-First Search (DFS) traversals:
    - **Preorder:** Root $\rightarrow$ Left $\rightarrow$ Right
    - **Inorder:** Left $\rightarrow$ Root $\rightarrow$ Right
    - **Postorder:** Left $\rightarrow$ Right $\rightarrow$ Root

### 6. 🕸️ Graphs
- **Graph Representations** ([`graph_list.py`](graph_list.py)):
  - **Adjacency Matrix:** 2D grid matrix mapping vertex connectivity.
  - **Custom Adjacency List:** Linked list of vertices where each vertex node points to a linked list of incident edges.

---

## ⚡ Time & Space Complexity

| Data Structure / Algorithm | Operation | Time Complexity | Space Complexity |
| :--- | :--- | :---: | :---: |
| **Singly Linked List** | Insert / Delete at Head | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Singly Linked List** | Insert / Delete at Tail | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| **Doubly Linked List** | Insert at Head / Tail | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Stack (Array / Linked List)** | Push / Pop / Peek | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ |
| **Queue (Linked List)** | Enqueue / Dequeue | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ |
| **Circular Queue** | Enqueue / Dequeue | $\mathcal{O}(1)$ | $\mathcal{O}(k)$ (fixed size) |
| **Binary Tree Traversals** | Preorder / Inorder / Postorder | $\mathcal{O}(n)$ | $\mathcal{O}(h)$ ($h$ = height) |
| **Parentheses Matcher** | Validation | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Infix to Postfix** | Expression Conversion | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Matrix Multiplication** | $R_1 \times C_1$ and $R_2 \times C_2$ | $\mathcal{O}(R_1 \cdot C_1 \cdot C_2)$ | $\mathcal{O}(R_1 \cdot C_2)$ |

---

## 🛠️ Getting Started

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

```bash
python --version
```

### Installation & Cloning

1. Clone the repository:
   ```bash
   git clone https://github.com/namaysingh3925/dsa-code-.git
   cd dsa-code-
   ```

2. Run any script directly using Python:
   ```bash
   # Run Singly Linked List
   python singly_linked_list.py

   # Run Binary Tree Traversals
   python binry_tree.py

   # Run Circular Queue
   python circular_queue.py

   # Run Infix to Postfix Converter
   python infix_to_postfix.py
   ```

---

## 💡 Quick Demo

### 1. Infix to Postfix Conversion
```bash
$ python infix_to_postfix.py
Infix: (A+B)*(C-D)/E
Postfix: AB+CD-*E/
```

### 2. Balanced Parentheses Validator
```bash
$ python parenthesess.py
Enter expression: {[()]}
Parentheses are Balanced

$ python parenthesess.py
Enter expression: {[(])}
Parentheses are Not Balanced
```

### 3. Singly Linked List CLI
```text
1.Insert Beginning  2.Insert End  3.Delete Beginning  4.Delete End  5.Traversal  6.Size  7.Exit
Enter choice: 1
Enter value: 10

1.Insert Beginning  2.Insert End  3.Delete Beginning  4.Delete End  5.Traversal  6.Size  7.Exit
Enter choice: 2
Enter value: 20

1.Insert Beginning  2.Insert End  3.Delete Beginning  4.Delete End  5.Traversal  6.Size  7.Exit
Enter choice: 5
10->20
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/namaysingh3925/dsa-code-/issues).

1. **Fork** the project
2. **Create** your feature branch (`git checkout -b feature/AmazingDSA`)
3. **Commit** your changes (`git commit -m 'Add some AmazingDSA'`)
4. **Push** to the branch (`git push origin feature/AmazingDSA`)
5. **Open** a Pull Request

---

## 👤 Author

**Namay Singh**
- GitHub: [@namaysingh3925](https://github.com/namaysingh3925)
- Repository: [namaysingh3925/dsa-code-](https://github.com/namaysingh3925/dsa-code-)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - feel free to use and adapt it for learning and academic purposes.
