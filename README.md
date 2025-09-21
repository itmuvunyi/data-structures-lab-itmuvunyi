# Data Structures Implementation Lab
## Enterprise Web Development - Week 3 Assignment

---

## Overview

This project focuses on implementing fundamental **data structures** in Python from scratch, including **Stack**, **Queue**, and **LinkedList**. The goal is to:

- Build a working data structure
- Write comprehensive **unit tests**
- Analyze **time and space complexity**
- Demonstrate practical use cases in **enterprise web development**

This lab provides hands-on experience with algorithmic thinking, Python programming, and best practices for testing and documentation.

---

## Repository Structure
```bash
data-structures-lab-itmuvunyi/
├── README.md
├── requirements.txt
├── .github/
│ └── workflows/
│ └── test.yml # GitHub Actions workflow for automated testing
├── src/
│ ├── init.py
│ ├── stack.py # Stack implementation (LIFO)
│ ├── queue.py # Queue implementation (FIFO)
│ └── linked_list.py # Linked List implementation
├── tests/
│ ├── init.py
│ ├── test_stack.py
│ ├── test_queue.py
│ └── test_linked_list.py
├── docs/
│ └── COMPLEXITY_ANALYSIS.md
└── examples/
  └── demo.py
```


---

## Learning Objectives

By completing this project:

- Implement a core data structure from scratch in Python
- Analyze and document **time and space complexity**
- Write **unit tests** for all standard operations and edge cases
- Explore **enterprise web development use cases**
- Practice professional **Git workflow and documentation**

---

## Choosing a Data Structure

Select **one** data structure to implement:

| Structure     | Type | Example Use Case |
|---------------|------|----------------|
| Stack         | LIFO | Browser history, undo operations, function call management |
| Queue         | FIFO | Print jobs, request handling, BFS traversal |
| LinkedList    | Dynamic | Dynamic collections, building other data structures |

>

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/data-structures-lab-itmuvunyi.git
cd data-structures-lab-itmuvunyi
```

## Create and Activate Virtual Environment
```
python -m venv venv
```
## Install Dependencies
```
pip install -r requirements.txt
```
## Running Tests
```
pytest tests/ -v
```
## My Implementation
```bash
Chosen Data Structure: LinkedList
Enterprise Use Case: Managing dynamic queues of user requests in a web application
Key Insight: LinkedList allows O(1) insertion and deletion without shifting elements, making it efficient for dynamic collections.
---




