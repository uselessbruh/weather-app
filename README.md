# 🌤️ MyWeather - A Linux Shell Scripting Learning Project

<div align="center">

![Weather](https://img.shields.io/badge/Weather-App-blue?style=for-the-badge&logo=weather&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![WSL](https://img.shields.io/badge/WSL-0078D4?style=for-the-badge&logo=windows&logoColor=white)

</div>

A comprehensive weather application that combines **🐍 Python GUI development** with **🐧 Linux shell scripting** to demonstrate practical command-line tools and API integration.

## 📋 Project Overview

This weather application was created as a learning project to understand shell scripting, Linux command-line tools, and cross-platform development. It fetches real-time weather data using shell scripts and displays it through an intuitive Python GUI with rich visualizations.

## ✨ Features

### 🌍 Weather Information

- 🌡️ **Current Weather Conditions** with emoji weather icons
- 📅 **3-Day Forecast** with hourly breakdown
- 📊 **Detailed Meteorological Data** (40+ parameters per hour)
- 🌙 **Astronomical Information** (moon phases, sunrise/sunset times)

### 📊 Visualizations

- 🌡️ **Temperature Charts** (Celsius and Fahrenheit)
- 💧 **Humidity Trends**
- ☁️ **Cloud Coverage Graphs**
- 🌧️ **Precipitation Analysis**
- 🌫️ **Atmospheric Conditions** (fog, frost, thunder, etc.)
- ☀️ **UV Index and Pressure Monitoring**

### 🖥️ User Interface

- 📑 **4-Tab Layout** for organized data presentation
- 📜 **Scrollable Tables** for hourly weather data
- 📈 **Interactive Charts** using Matplotlib
- 🔍 **Search Functionality** for any city worldwide

## 🛠️ Technology Stack

### 🎨 Frontend

- 🐍 **Python 3.x**
- 🖼️ **Tkinter** - GUI framework
- 📊 **Matplotlib** - Data visualization
- ✨ **ttk** - Enhanced UI components

### ⚙️ Backend & Data Processing

- 🐧 **Bash Scripting** - Data fetching and processing
- 🔧 **WSL (Windows Subsystem for Linux)** - Cross-platform compatibility
- 🌐 **wttr.in API** - Weather data source

### 🛠️ Command-Line Tools Used

- 🌐 **`curl`** - HTTP requests
- 📝 **`jq`** - JSON parsing and manipulation
- ✂️ **`sed`** - Stream editing and text processing
- 🔍 **`grep`** - Pattern matching with regex
- 📄 **`printf`** - Formatted output

## 📁 Project Structure

```txt
weather-app/
├── 📄 mainpro.py      # Main Python GUI application (792 lines)
├── 🐧 lalu.sh         # Bash script for weather data fetching (51 lines)
└── 📖 README.md       # Project documentation
```

## 🚀 Getting Started

### 🚀 Prerequisites

- 🐍 **Python 3.x** with tkinter and matplotlib
- 🐧 **WSL** (Windows Subsystem for Linux) if on Windows
- 💻 **Linux/Unix system** with bash
- 🌐 **Internet connection** for API access

### 🔧 Required Command-Line Tools

```bash
# Install required tools (Ubuntu/Debian)
sudo apt update
sudo apt install curl jq

# For other distributions, use appropriate package manager
```

### 🛠️ Installation & Usage

1. 📥 **Clone or download** the project files
2. 🔑 **Make the shell script executable**:

   ```bash
   chmod +x lalu.sh
   ```

3. ▶️ **Run the application**:

   ```bash
   python mainpro.py
   ```

4. 🔍 **Search for weather** by entering a city name and clicking "SEARCH"

## 🧠 Learning Objectives & Shell Scripting Concepts

This project demonstrates the following shell scripting and Linux concepts:

### 🧠 Core Shell Scripting

- ⚡ **Shebang (`#!/bin/bash`)** for script execution
- 📝 **Command-line arguments** using `$1`
- 🔗 **Variable assignment** and usage
- 🔄 **Command chaining** with pipes (`|`)

### ✨ Text Processing Mastery

```bash
# JSON cleaning with sed
sed 's/\[{"value//g' | sed 's/\":"//g' | sed 's/\"}]//g'

# Regex pattern matching with grep
grep -oP '(?<=astronomy=\[).*(?=\])'

# Multiple text transformations
sed 's/{//g; s/}//g; s/"//g; s/,/\n/g'
```

### 🌐 API Integration

- 🔌 **RESTful API calls** with curl
- 📋 **HTTP headers** manipulation
- 📊 **JSON data processing** with jq
- ⚠️ **Error handling** and data validation

### 🚀 Advanced Techniques

- 👀 **Lookahead/lookbehind regex** patterns
- 🗂️ **JSON path expressions** with jq
- 🌊 **Stream editing** for real-time data processing
- 🔄 **Cross-platform subprocess** communication

## 📊 Data Flow Architecture

```txt
User Input (City) → 🐍 Python GUI → 🐧 WSL/Bash Script → 🌐 wttr.in API
                                       ↓
Weather Data ← 📊 Python Processing ← 📝 JSON Parsing ← 🌐 curl Response
                ↓
GUI Visualization (📈 Charts, 📋 Tables, 🌤️ Icons)
```

## 🎯 Key Shell Scripting Techniques Demonstrated

### 1. 🌐 **API Data Fetching**

```bash
json=$(curl -H "Accept: application/json" "wttr.in/$inpval?format=j1" | jq .)
```

### 2. 📊 **JSON Processing Pipeline**

```bash
echo $json | jq -r '.current_condition[0] | to_entries | map("\(.key)=\(.value)") | .[]'
```

### 3. ✂️ **Complex Text Cleaning**

```bash
sed 's/\[{"value//g' | sed 's/\":"//g' | sed 's/\"}]//g'
```

### 4. 🔍 **Regex Pattern Extraction**

```bash
grep -oP '(?<=astronomy=\[).*(?=\])'
```

## 🔧 Advanced Features

- 🔄 **Cross-platform compatibility** (Windows WSL + Linux)
- ⚡ **Real-time data processing** with shell pipelines
- 🏗️ **Modular architecture** separating data fetching from presentation
- 🛡️ **Error-resistant parsing** with multiple fallback methods
- 📱 **Responsive UI** with scrollable content areas

## 📚 Learning Outcomes

By studying this project, you'll understand:

1. 🐧 **Shell Scripting Fundamentals**
2. 🛠️ **Linux Command-Line Tools**
3. 📝 **JSON Processing Techniques**
4. 🌐 **API Integration Patterns**
5. 🔄 **Cross-Platform Development**
6. 🔍 **Text Processing with Regex**
7. 🔗 **Python-Shell Integration**

## 🤝 Contributing

This is a learning project! Feel free to:

- 💡 Suggest improvements to shell scripting techniques
- ➕ Add new weather visualization features
- ⚡ Optimize the data processing pipeline
- 🛡️ Enhance error handling mechanisms

## 📝 License

This project is licensed under the **MIT License** - see below for details:

```
MIT License

Copyright (c) 2025 MyWeather Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- 🌤️ **wttr.in** - Excellent weather API service
- 🐧 **Linux/Unix community** - For amazing command-line tools
- 🔓 **Open source projects** - jq, curl, and all the tools that make this possible

---

<div align="center">

*🎓 This project serves as a practical demonstration of how shell scripting can be integrated with modern GUI applications to create powerful, real-world tools while learning fundamental Linux/Unix concepts.*

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)
![Educational](https://img.shields.io/badge/Purpose-Educational-green?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open-Source-blue?style=for-the-badge)

</div>
