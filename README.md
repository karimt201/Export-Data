# Export Data
 
## 📌 Overview
This project is designed to fetch data from a database and generate reports in multiple formats, including Excel (.xlsx), CSV (.csv), and PDF (.pdf). It provides a flexible and scalable solution for exporting data, making it suitable for various use cases such as data analysis, reporting, and sharing.

## 🚀 Features

- **Multi-format Export**: Export data in Excel, CSV, and PDF formats.
- **Database Integration**: Fetch data directly from a database.
- **Customizable Reports**: Easily customize the structure and content of the exported reports.
- **Error Handling**: Robust error handling to ensure smooth operation.
- **Scalable**: Designed to handle large datasets efficiently.

## 📂 Supported Export Formats
- **Excel (.xlsx)**: Export data to Excel spreadsheets for easy analysis and sharing.
- **CSV (.csv)**: Generate CSV files for compatibility with various tools and systems.
- **PDF (.pdf)**: Create PDF reports for professional documentation and printing.

## 🛠️ Installation
Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

Steps
1. Clone the repository:
```bash 
git clone https://github.com/karimt201/Export-Data.git
cd export-data
```
2. Install dependencies:
```bash 
pip install -r requirements.txt
```
3. Configure the database connection in **config.py** (if applicable).
4. Run the application:
```bash 
python app.py
```

## 🖥️ Usage
Exporting Data
1. Start the application by running:
```bash
python app.py
```
2. Use the API endpoints or command-line interface to export data:
    - **Export to Excel:**
    ```bash
    curl -X POST http://localhost:5000/export/excel -H "Authorization: YOUR_TOKEN" -d '{"filename": "report.xlsx"}'
    ```
    - **Export to CSV:**
    ```bash 
    curl -X POST http://localhost:5000/export/csv -H "Authorization: YOUR_TOKEN" -d '{"filename": "report.csv"}'
    ```
    - **Export to PDF:**
    ```bash
    curl -X POST http://localhost:5000/export/pdf -H "Authorization: YOUR_TOKEN" -d '{"filename": "report.pdf"}'
    ```
3. The exported file will be saved in the exports/ directory.

## 📁 Project Structure
```plaintext
export-data/
├── controllers/ # Contains business logic and controllers
├── helpers/ # Utility functions and exception handling
├── instance/ # sqlite file
├── migrations/ # Database migration files
├── models/ # Database models
├── resourses/ # Resource files (e.g., templates, static files)
├── routes/ # API routes and endpoints
├── services/ # Services for data handling and business logic
├── tests/ # Test cases and testing utilities
├── env/ # Environment-specific files (e.g., virtual environment)
├── .flaskenv # Flask environment configuration
├── .gitattributes # Git attributes configuration
├── .gitignore # Git ignore configuration
├── app.py # Main application entry point
├── config.py # Configuration file (e.g., database connection)
├── extensions.py # Flask extensions and plugins
├── README.md # Project documentation
├── requirements.txt # List of dependencies
└── swagger.yaml # Swagger/OpenAPI documentation

## 📝 API Documentation
Endpoints
- **POST /export/excel**: Export data to Excel.
    - **Request Body:**
    ```json
    {
        "filename": "report.xlsx"
    }
    ```
    - **Response:**
    ```json
    {
        "message": "File exported successfully",
        "filename": "report.xlsx"
    }
    ```
- **POST /export/csv**: Export data to CSV.
    - **Request Body:**
    ```json
    {
        "filename": "report.csv"
    }
    ```
    - **Response:**
    ```json
    {
        "message": "File exported successfully",
        "filename": "report.csv"
    }
    ```
- **POST /export/pdf**: Export data to PDF.
    - **Request Body:**
    ```json
    {
        "filename": "report.pdf"
    }
    ```
    - **Response:**
    ```json
    {
        "message": "File exported successfully",
        "filename": "report.pdf"
    }
    ```

## 🛑 Error Handling
The application handles common errors gracefully, including:
- **Invalid Token**: Returns a 401 Unauthorized response.
- **Invalid Filename**: Returns a 400 Bad Request response.
- **Database Errors**: Returns a 500 Internal Server Error response


## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeatureName).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeatureName).
5. Open a pull request

