# Student Grader (Flask) — Web App  
برنامج تقييم الطلاب (Flask) — تطبيق ويب

A modular, web-based student grading system built with Flask.  
نظام تقييم طلاب يعمل عبر الويب باستخدام فريمورك Flask، يدعم إدخال درجات متعددة، حساب المعدل، وحفظ البيانات.

---

## 📦 Project Overview

[![Build](https://github.com/OmegaCrimson/StudentGrader-Flask/actions/workflows/release.yml/badge.svg)](https://github.com/OmegaCrimson/StudentGrader-Flask/actions/workflows/release.yml)
![Release](https://img.shields.io/github/v/release/OmegaCrimson/StudentGrader-Flask)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Platform](https://img.shields.io/badge/platform-Web%20%7C%20Flask-green)
![License](https://img.shields.io/github/license/OmegaCrimson/StudentGrader-Flask)
![Downloads](https://img.shields.io/github/downloads/OmegaCrimson/StudentGrader-Flask/total)
![Last Commit](https://img.shields.io/github/last-commit/OmegaCrimson/StudentGrader-Flask)
![Commits per Month](https://img.shields.io/github/commit-activity/m/OmegaCrimson/StudentGrader-Flask)
![Issues](https://img.shields.io/github/issues/OmegaCrimson/StudentGrader-Flask)
![PRs](https://img.shields.io/github/issues-pr/OmegaCrimson/StudentGrader-Flask)
![Contributors](https://img.shields.io/github/contributors/OmegaCrimson/StudentGrader-Flask)
![Code Size](https://img.shields.io/github/languages/code-size/OmegaCrimson/StudentGrader-Flask)
![Top Language](https://img.shields.io/github/languages/top/OmegaCrimson/StudentGrader-Flask)
![Maintenance](https://img.shields.io/maintenance/yes/2025)
![GitHub Stars](https://img.shields.io/github/stars/OmegaCrimson/StudentGrader-Flask?style=social)
![GitHub Forks](https://img.shields.io/github/forks/OmegaCrimson/StudentGrader-Flask?style=social)
![Built by Mohamed Gonem](https://img.shields.io/badge/built%20by-Mohamed%20Gonem-blue?style=flat-square&logo=github)
![Made with Flask and ❤️](https://img.shields.io/badge/made%20with-Flask%20and%20%E2%9D%A4-red?style=flat-square&logo=flask)
![Open Source](https://img.shields.io/badge/open%20source-yes-brightgreen?style=flat-square&logo=github)
![Maintained](https://img.shields.io/badge/maintained-actively-blue?style=flat-square)
![Web App](https://img.shields.io/badge/interface-Web--based-lightgrey?style=flat-square&logo=html5)

---

## ✨ Features

- Add, view, and delete student records via web interface  
- Multi-subject support per student  
- GPA and percentage calculation  
- Input validation (Arabic & English digits)  
- Persistent storage using JSON  
- Clean UI with Jinja2 templates  
- Modular Flask architecture  
- Action/error logging  
- Easy to deploy and extend

---

## 🚀 Getting Started

### Option 1: Run Locally

```bash
git clone https://github.com/OmegaCrimson/StudentGrader-Flask.git
cd StudentGrader-Flask
pip install -r requirements.txt
python main.py
```

Then open your browser and go to:  
`http://localhost:5000`

### Option 2: Download Executable (Windows)

1. Visit the [Releases](https://github.com/OmegaCrimson/StudentGrader-Flask/releases) page  
2. Download the latest `.zip` or `.exe`  
3. Run `StudentGrader.exe` (self-contained Flask server)

---

## 🧪 Sample UI Screens

- **Home Page**: View all students  
- **Add Student**: Form to input name, age, subjects, scores  
- **Student Detail**: View GPA, subjects, and delete option

---

## 🗂️ Project Structure

```
StudentGrader-Flask/
├── main.py                  # Flask app entry point
├── models/
│   ├── student.py           # Student class
│   └── subject.py           # Subject class
├── templates/
│   ├── index.html           # Home page
│   ├── add_student.html     # Add student form
│   └── student.html         # Student detail view
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

- Python 3.11
- Flask (web framework)
- Jinja2 (templating)
- JSON (data storage)
- PyInstaller (for packaging)
- GitHub Actions (CI/CD)

---

## 🔁 CI/CD Automation

This project uses GitHub Actions to:

- Build the Flask app on manual trigger
- Package the `.exe` and `.zip` artifacts
- Upload them to the [Releases](https://github.com/OmegaCrimson/StudentGrader-Flask/releases) page

You can trigger a release manually using the GitHub Actions tab.

---

## 📄 License

Licensed under the [MIT License](LICENSE).  
Use, modify, and distribute freely — just credit the author: **Mohamed Gonem / محمد غنيم**

---

## 🙌 Acknowledgments

- Built with care, clarity, and curiosity  
- Inspired by real-world grading systems and Flask design patterns  
- Thanks to the open-source community for tools and ideas

---

**Built to be useful. Designed to be clear.  
تم بناؤه ليكون مفيدًا، وصُمم ليكون واضحًا.**