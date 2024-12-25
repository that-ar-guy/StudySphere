# Contributing to StudySphere  

Thank you for your interest in contributing to StudySphere! 🎉 Your help is greatly appreciated, whether it's reporting bugs, suggesting new features, or submitting a pull request to improve the project. This guide will help you get started.  

---

## Table of Contents  
1. [Code of Conduct](#code-of-conduct)  
2. [How Can I Contribute?](#how-can-i-contribute)  
   - [Reporting Bugs](#reporting-bugs)  
   - [Suggesting Features](#suggesting-features)  
   - [Improving Documentation](#improving-documentation)  
   - [Submitting Code](#submitting-code)  
3. [Development Setup](#development-setup)  
4. [Submitting a Pull Request](#submitting-a-pull-request)  

---

## Code of Conduct  
Please make sure to read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to create a welcoming and respectful environment for everyone.  

---

## How Can I Contribute?  

### Reporting Bugs  
If you find a bug in the project, please report it by opening an [issue](https://github.com/that-ar-guy/StudySphere/issues). Make sure to include:  
- A clear and descriptive title.  
- Steps to reproduce the issue.  
- Expected and actual behavior.  
- Any relevant logs, screenshots, or additional context.  

### Suggesting Features  
We’d love to hear your ideas for improving StudySphere! To suggest a feature:  
- Open an [issue](https://github.com/that-ar-guy/StudySphere/issues) with the label `feature request`.  
- Provide a detailed explanation of your idea and how it would benefit users.  

### Improving Documentation  
If you spot an issue in the documentation or want to add helpful instructions, feel free to submit changes. Documentation updates are always welcome!  

### Submitting Code  
If you'd like to implement a new feature or fix a bug, check out the existing [issues](https://github.com/that-ar-guy/StudySphere/issues) or create a new one to discuss your idea with the maintainers.  

---

## Development Setup  

To get started with development, follow these steps:  

1. **Fork the Repository**:  
   Click on the "Fork" button at the top right of this repository to create your copy.  

2. **Clone Your Fork**:  
   ```bash  
   git clone https://github.com/your-username/StudySphere.git  
   cd StudySphere

3. ** Set Up a Virtual Environment:**
   ```bash
   python -m venv env  
   source env/bin/activate  # For Windows: env\Scripts\activate  
   ```

4. ** Install Dependencies**:
    ```bash
    pip install -r requirements.txt  
    ```

5.** Run Migrations: ** 
  ```bash
    python manage.py migrate  
  ```

6. ** Start the Development Server **
     ```bash
     python manage.py runserver
     ```

7. ** Test the Setup**
     Open your browser and go to `http://127.0.0.1:8000/`


## Submitting a Pull Request

When you're ready to contribute, follow these steps:

1. **Create a Branch:**

Create a new branch for your work:
```bash
git checkout -b feature-or-bug-name  
```

2.**Make Your Changes:**

Implement your changes and make sure your code is clean and well-documented.

3.**Run Tests:**

Ensure all existing tests pass and add tests for any new functionality.

4. **Commit Your Changes:**

```bash
git add .  
git commit -m "Describe your changes here"  
```

5.**Push Your Branch:**

```bash
   git push origin feature-or-bug-name  
```

6. **Open a Pull Request:**
   
Go to the original repository and open a pull request. Provide a clear description of your changes and link to any relevant issues.

 
 

