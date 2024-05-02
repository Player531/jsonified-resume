from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

resume = {
    "name": "Chirag Barbhaya", 
    "place": "Kolkata, West Bengal, India",
    "contact": {
        "phone": "8334822751",
        "email": "chiragbarbhaya@gmail.com",
        "linkedin": "https://www.linkedin.com/in/chirag-barbhaya-0bb190228/"
    },
    "skills": {
        "languages": [
            "python",
            "java",
            "javascript",
            "c",
            "SQL(MySQL, SQLite)",
            "HTML",
            "CSS"
        ],
        "frameworks": [
            "flask"
        ],
        "tools": [
            "Github",
            "VS Code",
            "postman"
        ]
    },
    "projects": [
        "Weather dashboard which calls the REST API endpoint, made with python using external libraries: requests and tkinter",
        "Designing a CRUD application with the Flask framework",
        "Engineered a Face Recognition Attendance System which outputs an Excel sheet, made using python external libraries"
    ],
    "Education": {
        "undergraduate": {
            "college": "The Bhawanipur Education Society College(November 2020 - September 2023)",
            "degree": "(B.Sc Hons.)Bachelor of Science in Computer Science Honours",
            "CGPA": "8.246",
            "status": "Graduated in September 2023"
        },
        "postgraduate": {
            "college": "Brainware University(August 2023 - August 2025)",
            "degree": "(MCA)Master of Computer Applications",
            "CGPA": "Coming Soon",
            "status": "Graduating in july 2025"
        }   
    },
    "additional": [
        "TCS National Qualifier Test : https://drive.google.com/file/d/1ZpPV4pLra9IueRv-nnVPAe2IFrZq3dt5/view?usp=drive_link",
        "Coding Profile : https://leetcode.com/u/Player531/"
    ]    
}

@app.route("/resume", methods=["GET"])
def getResume():
    try:
        if request.method == "GET":
            return jsonify(resume)
        raise Exception("Resume Not Found")
    except Exception as error:
        return jsonify({"error": str(error)})
    
if __name__ == "__main__":
    app.run()

