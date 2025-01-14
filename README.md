# Integration Platform

This project is an integration platform that connects with various services like Airtable, Notion, and HubSpot. It uses FastAPI for the backend and React for the frontend.

## Project Structure
## Backend

The backend is built using FastAPI and handles OAuth2 authorization and data fetching from Airtable, Notion, and HubSpot.

### Setup

1. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install the dependencies:
    ```sh
    pip install -r backend/requirements.txt
    ```

3. Create a `.env` file in the [backend](http://_vscodecontentref_/1) directory with the following content:
    ```
    REDIS_HOST=localhost
    HUBSPOT_CLIENT_ID=your_hubspot_client_id
    HUBSPOT_CLIENT_SECRET=your_hubspot_client_secret
    ```

4. Run the FastAPI server:
    ```sh
    uvicorn backend.main:app --reload
    ```

### Endpoints

- `GET /`: Returns a welcome message.
- `POST /integrations/notion/authorize`: Authorizes Notion integration.
- `GET /integrations/notion/oauth2callback`: Handles Notion OAuth2 callback.
- `POST /integrations/notion/credentials`: Retrieves Notion credentials.
- `POST /integrations/notion/load`: Loads Notion data.
- `POST /integrations/airtable/authorize`: Authorizes Airtable integration.
- `GET /integrations/airtable/oauth2callback`: Handles Airtable OAuth2 callback.
- `POST /integrations/airtable/credentials`: Retrieves Airtable credentials.
- `POST /integrations/airtable/load`: Loads Airtable data.
- `POST /integrations/hubspot/authorize`: Authorizes HubSpot integration.
- `GET /integrations/hubspot/oauth2callback`: Handles HubSpot OAuth2 callback.
- `POST /integrations/hubspot/credentials`: Retrieves HubSpot credentials.
- `POST /integrations/hubspot/load`: Loads HubSpot data.

## Frontend

The frontend is built using React and Material-UI. It provides a user interface to connect to the integrations and load data.

### Setup

1. Navigate to the [frontend](http://_vscodecontentref_/2) directory:
    ```sh
    cd frontend
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```

3. Run the React development server:
    ```sh
    npm start
    ```

### Components

- [App.js](http://_vscodecontentref_/3): Main application component.
- [integration-form.js](http://_vscodecontentref_/4): Form to select and authorize integrations.
- [data-form.js](http://_vscodecontentref_/5): Form to load and display data from integrations.
- [airtable.js](http://_vscodecontentref_/6): Airtable integration component.
- [hubspot.js](http://_vscodecontentref_/7): HubSpot integration component.
- [notion.js](http://_vscodecontentref_/8): Notion integration component.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
