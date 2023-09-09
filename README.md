# Dialogflow Chatbot with FastAPI Backend

This project is a chatbot implemented using Dialogflow for natural language understanding and FastAPI for the backend server. It allows users to interact with the chatbot for placing food orders, tracking orders, adding and removing items from their order, and completing orders. This README provides an overview of the project's structure and usage.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgments)
- [Contributing](#contributing)
- [License](#license)


## Project Overview

The project consists of a chatbot backend implemented in FastAPI, which integrates with Dialogflow for handling user requests and providing responses. The chatbot can perform the following actions:

- **Place an Order**: Users can add food items and quantities to their order.
- **Remove Items from Order**: Users can remove items from their current order.
- **Complete Order**: Users can complete their order, which will be saved in the database.
- **Track Order**: Users can check the status of their placed orders.

The project uses a combination of FastAPI routing and Dialogflow intents to handle user requests and provide relevant responses.

## Setup and Installation

To set up and run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd dialogflow-fastapi-chatbot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Dialogflow agent and configure it to use the FastAPI server as a webhook for fulfillment.

4. Configure the database connection in the `db_helper.py` file.

5. Run the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. Your FastAPI server should now be running and ready to accept requests from Dialogflow.

## Usage

Once the FastAPI server is running, you can interact with the chatbot using Dialogflow or any client that can send POST requests to the server's endpoints.

## Endpoints

- **POST /:** This endpoint handles incoming requests from Dialogflow, processes them, and returns JSON responses based on the user's intent.

## Project Structure

The project structure is organized as follows:

- `main.py`: The FastAPI application and request handling logic.
- `db_helper.py`: Database helper functions for interacting with the database.
- `generic_helper.py`: Generic helper functions used across the application.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This README file.

## Acknowledgments

This project was built following the tutorial by Dhaval Patel on the Codebasics YouTube Channel. I would like to acknowledge Dhaval Patel for providing the educational content that helped me develop this chatbot.

- [Dhaval Patel's YouTube Channel](https://www.youtube.com/codebasics)
- [Tutorial Link (if available)](https://www.youtube.com/example-tutorial-link)


## Contributing

Contributions to this project are welcome. You can contribute by submitting bug reports, feature requests, or pull requests to enhance the functionality or fix issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify and expand upon this README to provide more specific details about your project, deployment instructions, and any additional information that may be relevant to users and contributors.

