# Set Card Game Solver

## Overview

This Python repository provides a program to simulate and identify sets of cards from the game "Set." The primary goal of this project is to create an application that allows users to take pictures of a collection of Set cards and use image recognition to identify and output the possible sets within the cards.

## How It Works

The project is divided into several components:

1. **Card Simulation:** The program simulates a deck of Set cards. Set cards have four distinct features: color, shape, number, and shading. The simulation creates a deck of cards with all possible combinations of these features.

2. **Set Identification:** The core functionality is to identify sets within a given collection of cards. This involves analyzing the features of each card and determining if they form a valid set according to the rules of the game.

3. **Image Recognition (Work in Progress):** The project aims to incorporate image recognition capabilities. Users will be able to take a picture of their collection of cards. The application will then process the image and determine the sets present, providing the user with this information.

## Prerequisites

- Python 3.8


## Getting Started

Follow these steps to get started with the project:

1. Clone this repository:

```bash
git clone https://github.com/PnkUncrn/Set
```

2. Navigate to the project directory:

```bash
cd Set
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) To simulate a deck of Set cards and find sets:

```bash
python main.py simulate
```

5. (Work in Progress) For image recognition, use the following command (once implemented):

```bash
python main.py recognize --image path/to/your/image.png
```

## Usage

Add usage.


## Contribution Guidelines

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature`.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request to the `main` branch of the original repository.
5. Be sure to include clear commit messages and comments in your code.

## License



## Contact

- [Aseem Prashar](mailto:prasharaseem@gmail.com)
- [Project Repository](https://github.com/PnkUncrn/Set)


**Note:** This README serves as an initial guide. As the project evolves and image recognition is implemented, make sure to update and improve this documentation accordingly.