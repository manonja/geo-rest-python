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

To get started with **geo-rest-python**, follow these steps:

1. Clone this repository:

   `git clone https://github.com/yourusername/geo-rest-python.git`

2. Navigate to the project directory:

   `cd geo-rest-python`

3. Create a virtual environment and install dependencies:

   ```
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   `uvicorn app.main:app --reload`

5. Visit `http://127.0.0.1:8000/docs` to explore the API using the interactive Swagger UI.

## 📚 Usage

Once the server is running, you can access GeoJSON data through the exposed API endpoints. Example:

`GET /geojson/{id}`

This will return the GeoJSON object associated with the provided ID.

## 🤝 Contributing

We welcome contributions! To get started:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -m 'Add a new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a pull request.

Ensure that your code passes the pre-commit hooks by running:

`pre-commit run --all-files`

## 📜 License

This project is licensed under the BSD-3-Clause License. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

Thanks to the FastAPI community and contributors to GitHub Actions for pre-commit hooks for making development smoother and more efficient.
