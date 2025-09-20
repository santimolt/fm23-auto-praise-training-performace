# FM23 Auto Praise Players Training

Automates praising players who train well in Football Manager 23.
No more manually checking training scores: this program detects when FM23 is running and automatically praises players with a training score of 7.50 or higher.

Table of Contents

- [FM23 Auto Praise Players Training](#fm23-auto-praise-players-training)
  - [Description](#description)
  - [Installation](#installation)
    - [Windows](#windows)
    - [Mac/Linux](#maclinux)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)

## Description

This project is an automation script that interacts with Football Manager 23.

- Detects if FM23 is running.
- Checks the training scores of your players.
- Automatically praises players with a performance score ≥ 7.50.

Goal: save time and keep your players motivated without manual effort.

## Installation

1. Clone the repository:
   git clone <https://github.com/your_username/FM23-Auto-Praise-Players-Training.git>
   cd FM23-Auto-Praise-Players-Training

2. Create and activate a virtual environment:
   python -m venv venv

   ### Windows

   venv\Scripts\activate

   ### Mac/Linux

   source venv/bin/activate

3. Install dependencies (to be defined as the project progresses):
   pip install -r requirements.txt

Note: The project is in its early stages, so dependencies will be added as development continues.

## Usage

Run the main script while FM23 is open:
   python main.py

The program will automatically:

- Check if FM23 is running.
- Praise players with training ≥ 7.50.

It is recommended to keep FM23 running in the background while the script executes.

## Project Structure

```bash
FM23-Auto-Praise-Players-Training/
├── venv/               # Virtual environment
├── main.py             # Main script
├── requirements.txt    # Dependencies
├── README.md           # This file
└── .gitignore
```

## Contributing

1. Fork the project
2. Create a branch: git checkout -b my-new-feature
3. Commit your changes: git commit -m "Add new feature"
4. Push to the branch: git push origin my-new-feature
5. Open a Pull Request

## License

MIT License
