# 🌍 geo-rest-python

A simple and efficient REST HTTP server built to serve GeoJSON data. **geo-rest-python** is designed as a boilerplate for future projects, allowing you to quickly set up a REST API for serving GeoJSON data in any application.

## 🛠️ Tech Stack

- **Python**: Powering the backend for processing GeoJSON data.
- **FastAPI**: A high-performance web framework for building the REST API, known for its speed and ease of use.
- **GitHub Actions**: Automated pre-commit hooks to ensure clean and consistent code quality.

## 🚀 Features

- 📄 Serve GeoJSON data via RESTful API endpoints.
- ⚡ FastAPI framework for minimal latency and maximum performance.
- 🧰 Extensible structure for future GeoJSON-based projects.
- 🔄 GitHub Actions for automated pre-commit hooks to enforce code quality.

## 📦 Installation and Setup

### Prerequisites
Before you begin, ensure you have the following installed on your system:

- Python 3.8 or higher
- pip (or your prefered python package installer)
- Git

### Quick start
To get started with **geo-rest-python**, follow these steps:

1. Clone this repository:

   `git clone https://github.com/yourusername/geo-rest-python.git`
   `cd geo-rest-python`

2. Install Poetry (if not already installed):

   `pip install poetry`

3. Install project dependencies

   `poetry install`

## 📚 Usage

### Step 1: Run the server

Before using the client, you need to start the server. Open a terminal and run:
   `poetry run run-server`

This will start the server using Uvicorn. Keep this terminal open and running.

### Step 2: Run the client

Open a new terminal window. To run the script and fetch GeoJSON data for a country, use the following command:

   `poetry run client-example [COUNTRY_NAME]`

For example:
   `poetry run client-example Netherlands`

### Optional: Specify a custom API URL
If you need to use a different API URL, you can specify it using the --base-url option:

   `poetry run client-example Netherlands --base-url "http://example.com"`

## ⚽️ Running Tests
To run the tests for this project, use the following command:
   `poetry run test`

This will run all the tests in the tests/ directory.

## 🐿️ Troubleshooting
If you encounter any issues while running the script, please ensure that:

- You have correctly installed all prerequisites.
- You are in the correct directory (geo-rest-python).
- You have run poetry install to install all dependencies.
- The server is running in a separate terminal window before you try to use the client.

## 🤝 Contributing

Have ideas to improve the geo-rest-python? We welcome your contributions! Whether it's fixing a bug or adding new features, feel free to fork the repository, create a feature branch, and send a pull request:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -m 'Add a new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a pull request.

Ensure that your code passes the pre-commit hooks by running:

`pre-commit run --all-files`

## 📣 Spread the Word

If you enjoy using geo-rest-python, share it with your friends and fellow developers!

[Twitter](#) | [Facebook](#) | [LinkedIn](#)

## 📜 License

This project is licensed under the BSD-3-Clause License. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

Thanks to the FastAPI community and contributors to GitHub Actions for pre-commit hooks for making development smoother and more efficient.
