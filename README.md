# Library Management System

## Overview
The Library Management System is a simple Python application that allows users to view details about different books in the library. The system displays a list of books and allows users to select a book by its number to read information such as the title, author, published year, and a brief description. Users can continue browsing or exit the system.

## Features
- View a list of books in the library.
- Select a book by its number to get more details.
- Continue browsing or exit the system.
- Input validation for book selection.
- Reusable and maintainable structure using dictionaries.

## Books Available
1. **Train to Pakistan** - Khushwant Singh
2. **The God of Small Things** - Arundhati Roy
3. **The White Tiger** - Aravind Adiga
4. **Family Life** - Akhil Sharma
5. **Wings of Fire** - A. P. J. Abdul Kalam & Arun Tiwari

## Requirements
- Python 3.x or higher

## How to Run
1. Download the Python file `library_management.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the Python script using the command:

    ```bash
    python library_management.py
    ```

5. Follow the prompts to select books and explore the library.

## Example Interaction
```bash
Welcome to the library

TITLE OF BOOKS
  1. Train to Pakistan
  2. The God of Small Things
  3. The White Tiger
  4. Family Life
  5. Wings of Fire

Select number to read about book: 1
1. [BOOK NAME]: Train to Pakistan
2. [AUTHOR NAME]: Khushwant Singh
3. [PUBLISHED YEAR]: 1956
4. [DESCRIPTION]: Train to Pakistan is a novel by Khushwant Singh that tells the story of a peaceful village on the border of India and Pakistan, that is torn apart by the partition of India in 1947.

Do you want to continue? (yes/no): yes

...



## Screenshot

![Screenshot 2024-12-13 172011](https://github.com/user-attachments/assets/ae99511d-79b1-4a31-b6d9-319c88680be7)
![Screenshot 2024-12-13 172044](https://github.com/user-attachments/assets/226061bf-a365-4336-beb4-ca5e03aee8ca)
![Screenshot 2024-12-13 172105](https://github.com/user-attachments/assets/7479ce21-c25d-4102-8343-5db1f4d377d8)




## Code Explanation
- **Data Storage**: Book details are stored in a dictionary, making it easy to retrieve and update information.
- **Input Handling**: Input is validated to ensure that the user selects a valid book number.
- **Looping**: A `while` loop is used for continued interaction with the system until the user chooses to exit.

## License
This project is open source and available under the MIT License.

