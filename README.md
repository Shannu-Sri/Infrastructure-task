# Infrastructure-task
# Orders Analysis

## Description

This project analyzes customer orders data to compute various metrics like monthly revenue, product revenue, customer revenue, and top 10 customers by revenue.

## How to Run

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Build the Docker image:
    ```sh
    docker build -t orders-analysis -f Dockerfile .
    ```

2. Run the Docker container:
    ```sh
    docker run --rm orders-analysis
    ```

### Running the Tests

1. Build the test Docker image:
    ```sh
    docker build -t orders-analysis-test -f Dockerfile.test .
    ```

2. Run the test Docker container:
    ```sh
    docker run --rm orders-analysis-test
    ```

## Project Structure

- `main.py`: Main program logic.
- `test_main.py`: Test cases for the main program.
- `Dockerfile`: Dockerfile for the main application.
- `Dockerfile.test`: Dockerfile for the tests.
- `README.md`: Instructions to run the application and tests.
- `orders.csv`: A csv file for storing data.
