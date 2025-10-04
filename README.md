COSC 520: The Login Checker Problem
This repository contains a performance analysis of various data structures for solving the "Login Checker Problem." The goal is to efficiently determine if a given login exists within a very large dataset of unique logins.

Overview
The project compares five different methods for checking the existence of a login string in a dataset of up to 50 million entries. The analysis focuses on build times, lookup times, and memory usage for each data structure.

Data Structures Analyzed
The following methods were implemented and compared:

Linear Search: A simple scan through an unsorted list.

Binary Search: Requires a pre-sorted list for efficient lookups.

Hashing (Set): Utilizes Python's built-in hash set for average O(1) lookups.

Bloom Filter: A probabilistic data structure that is space-efficient but may produce false positives.

Cuckoo Filter: Another probabilistic data structure that is also space-efficient and allows for deletions, unlike a standard Bloom Filter.

Dataset

You can generate the dataset using the provided Python script or download it from the following link:

Dataset Link: https://drive.google.com/file/d/1Yl8NTkzK7QA1cl4inRCTQPCEDcJB22U-/view?usp=sharing

Usage
To run this project, follow the steps below.

1. Generate the Dataset (Optional)
If you do not download the dataset, you can generate it locally. The following command will create a 1 billion login file named logins_all_1B.txt.

python generate_dataset.py --total 1000000000 --out logins_all_1B

2. Run the Performance Analysis
The main analysis is conducted in the Jupyter Notebook.

Ensure you have the required libraries installed:

pip install jupyter matplotlib numpy pybloom-live pyprobables

Launch the notebook and run the cells.

Files in this Repository
assignment.ipynb: The main Jupyter Notebook containing the analysis and plotting code.
generate_dataset.py: Script to generate the login dataset.
