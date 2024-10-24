# FastAPI MongoDB Project - Items and User Clock-In Records API

## Table of Contents
* Project Overview
* Features
* Tech Stack
* Setup and Installation
* Endpoints

## Project Overview
This project implements two main APIs:

1. Items API - Manages items with fields like name, email, quantity, expiry date, and insert date.
2. User Clock-In Records API - Manages user clock-in data, including email, location, and clock-in time.
MongoDB is used as the database, and FastAPI is the framework for building the API. It supports typical CRUD operations and advanced filtering using MongoDB's aggregation framework.

## Features
* CRUD operations for both items and user clock-in records.
* MongoDB aggregation for item filtering and counting by email.
* Filtering on expiry date, quantity, insert date, email, and clock-in location.
* Automatically managed fields such as insert date and clock-in time.

## Setup and Installation
### Prerequisites
* Python 3.8+
* MongoDB instance (Atlas or local)
* Virtual environment

## Steps to run the project locally
1. **Clone the repository:**
    ```bash
    git clone https://github.com/aboobacker-bilal/fastapi_curd_project.git
    cd your-repo
    ```
2. **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up MongoDB:**
    - If using MongoDB Atlas, create a free cluster and obtain your connection string.
    - If using a local MongoDB instance, ensure MongoDB is installed and running.
5. **Configure environment variables:**
    - Create a `.env` file in the project root and add your MongoDB URI:
    ```bash
    MONGO_URI="your_mongo_connection_string"
    ```
### Running the Application
1. **Start the FastAPI application:**
    ```bash
    uvicorn main:app --reload
    ```
## Endpoints
### A. Items API
##### 1. POST /items
* Create a new item.
* Input: name, email, item_name, quantity, expiry_date (YYYY-MM-DD)
##### 2. GET /items/{id}
* Retrieve an item by its ID.
##### 3. GET /items/filter
* Filter items based on the following criteria:
* email (exact match)
* expiry_date (expiring after the provided date)
* insert_date (inserted after the provided date)
* quantity (greater than or equal to the provided number)
##### 4. GET /items/aggregate
* Aggregate items by email and return the count of items per email.
##### 5. DELETE /items/{id}
* Delete an item by its ID.
##### 6. PUT /items/{id}
* Update an item by its ID (excluding the insert date).

### B. Clock-In Records API
##### 1. POST /clock-in
* Create a new clock-in record.
* Input: email, location
##### 2. GET /clock-in/{id}
* Retrieve a clock-in record by its ID.
##### 3. GET /clock-in/filter
* Filter clock-in records based on:
* email (exact match)
* location (exact match)
* insert_datetime (clock-ins after the provided date)
##### 4. DELETE /clock-in/{id}
* Delete a clock-in record by its ID.
##### 5. PUT /clock-in/{id}
* Update a clock-in record by its ID (excluding the insert date).

## License
This project is licensed under the MIT License. See the LICENSE file for details.
