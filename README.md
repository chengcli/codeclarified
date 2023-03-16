# CodePrettifier.ai

CodePrettifier.ai is a web application that accepts a code file and outputs a prettified and commented version of the code without changing its content. This project is built using Python, Flask, and the OpenAI API.

## Features

- File upload functionality for code files.
- Code processing with the OpenAI API to generate prettified code and comments.
- Progress bar indicating the progress of code processing.
- Syntax highlighting and a mobile-optimized layout for displaying results.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip
- virtualenv (optional but recommended)

### Steps

1. Clone the repository:
```
git clone https://github.com/chengcli/CodePrettifier.git
```

2. (Optional) Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate # For Unix systems
venv\Scripts\activate # For Windows
```

3. Install the required packages 
```
pip install -r requirements.txt
```

4. Set your OpenAI API key as an environment variable:
```
export OPENAI_API_KEY="your-api-key" # For Unix systems
set OPENAI_API_KEY="your-api-key" # For Windows
```

## Running the Application

1. Make sure your virtual environment is active (if you're using one).
2. Run the Flask app:
```
python app.py
```
3. Open your web browser and navigate to http://127.0.0.1:5000. You should see the home page with the file upload form and progress bar.

## Usage

1. Click "Choose File" and select a code file from your local system.
2. Click "Upload" to submit the file for processing.
3. The progress bar will update as your application processes the code file and communicates with the OpenAI API.
4. Once the processing is completed, you will be redirected to the results page, which displays the prettified code and comments with syntax highlighting and a mobile-optimized layout.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
