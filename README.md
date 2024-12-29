<h1 style="font-size: 28px; font-weight: bold; text-align: center;">Farmatta</h1>

<p style="font-size: 16px;">Farmatta is a farm management platform designed to connect farmers with buyers, suppliers, and agricultural resources. This project aims to <i> empower rural agricultural communities </i> by providing them with tools to manage crops, track progress, and engage in a <em>digital marketplace.</em></p>

<h2 style="font-size: 20px;">Setup Instructions</h2>
<p style="font-size: 16px;">To get started with this project:</p>

<ol>
  <li>Clone the repository: <code>git clone https://github.com/ochogwuprince92/Farmatta.git</code></li>
  <li>Create a virtual environment: <code>python -m venv venv</code></li>
  <li>Activate the virtual environment: <code>source venv/bin/activate</code> (Linux/Mac) or <code>venv\Scripts\activate</code> (Windows)</li>
  <li>Install the dependencies: <code>pip install -r requirements.txt</code></li>
  <li>Run the Django development server: <code>python manage.py runserver</code></li>
</ol>

<h2 style="font-size: 20px;">Project Structure</h2>
<ul>
  <li><b>core/</b> - Contains the main app for the project.</li>
  <li><b>manage.py</b> - The Django management script.</li>
  <li><b>requirements.txt</b> - The list of required packages.</li>
</ul>

<h2 style="font-size: 20px;">Additional Information</h2>
<p style="font-size: 16px;">You can find the project repository here: <a href="https://github.com/ochogwuprince92/Farmatta" target="_blank">Farmatta GitHub Repository</a>.</p>

<h2 style="font-size: 20px;">Author</h2>
<p style="font-size: 16px;">This project is authored by <b>Ochogwu Prince</b>.</p>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Farmatta API - Project Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        header {
            background-color: #00796b;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        h1, h2 {
            color: #00796b;
        }
        .content {
            padding: 20px;
        }
        .content ul {
            list-style-type: none;
            padding: 0;
        }
        .content ul li {
            margin: 5px 0;
        }
        code {
            background-color: #f1f1f1;
            padding: 2px 4px;
            border-radius: 3px;
        }
        .author {
            margin-top: 20px;
            background-color: #e0f2f1;
            padding: 10px;
            border-left: 5px solid #00796b;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            padding: 10px 0;
            background-color: #00796b;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        <h1>Farmatta API - Project Documentation</h1>
    </header>

    <div class="content">
        <h2>Project Description</h2>
        <p>Farmatta API is a RESTful platform designed to connect farmers specializing in cash crops like rice, yam, and cassava with buyers, suppliers, and agricultural resources. This platform bridges the gap in the agricultural supply chain by offering tools for crop management, marketplace operations, transaction tracking, and land management. The API provides a comprehensive solution for farmers to manage their crops, land, and farming activities and engage with buyers and suppliers efficiently and transparently.</p>

        <h2>Core Features and Functionality</h2>
        <ul>
            <li><strong>Farmer Registration and Authentication</strong>: 
                <ul>
                    <li>Users can sign up and log in using email and password.</li>
                    <li>Farmers can manage their profiles, including personal details such as <code>address</code>, <code>phone number</code>, and farm locations.</li>
                    <li>The system will distinguish between <strong>Farmers</strong> and <strong>Buyers</strong> during registration.</li>
                </ul>
            </li>
            <li><strong>Cash Crop Management</strong>: 
                <ul>
                    <li>Farmers can list cash crops for sale, update crop details, and manage crop inventory.</li>
                    <li>Crop types include <code>rice</code>, <code>yam</code>, <code>cassava</code>, and other regional crops.</li>
                    <li>Each crop can have a <code>picture</code> uploaded to provide better visualization for buyers.</li>
                </ul>
            </li>
            <li><strong>Crop Care Management</strong>: 
                <ul>
                    <li>Track and manage crop care activities, including watering schedules, pest control, and fertilization.</li>
                    <li>Record growth stages of crops (e.g., <code>germination</code>, <code>flowering</code>, <code>harvesting</code>).</li>
                </ul>
            </li>
            <li><strong>Marketplace for Crops</strong>: 
                <ul>
                    <li>Farmers can list crops and services for sale.</li>
                    <li>Buyers can search, filter, and view available crop listings.</li>
                    <li>Buyers can view detailed crop listings, including crop pictures, quantity, and price.</li>
                </ul>
            </li>
            <li><strong>Transaction History</strong>: 
                <ul>
                    <li>Track transactions between farmers and buyers.</li>
                    <li>View completed and pending transaction details for both farmers and buyers.</li>
                </ul>
            </li>
            <li><strong>Land Management</strong>: 
                <ul>
                    <li>Farmers can record land plot details, including <code>location</code>, <code>size</code>, and <code>crop rotation</code>.</li>
                    <li>Track soil health metrics such as <code>pH levels</code>, <code>moisture</code>, and <code>nutrients</code>.</li>
                </ul>
            </li>
            <li><strong>Location-Based Search</strong>: 
                <ul>
                    <li>Match farmers with buyers and suppliers based on geographical proximity.</li>
                </ul>
            </li>
        </ul>

        <h2>API Endpoints Overview</h2>
        <h3>Authentication</h3>
        <ul>
            <li><code>POST /auth/register</code> - Registers users as either <strong>Farmers</strong> or <strong>Buyers</strong> with <code>address</code>, <code>phone number</code>, and other relevant details.</li>
            <li><code>POST /auth/login</code> - Logs users in and returns an authentication token.</li>
        </ul>

        <h3>Crop Management</h3>
        <ul>
            <li><code>POST /crops/</code> - Create a new crop record (including <code>name</code>, <code>growth stage</code>, <code>health status</code>, and <code>picture</code>).</li>
            <li><code>GET /crops/</code> - Retrieve a list of crops (available for buyers and farmers).</li>
            <li><code>GET /crops/<crop_id>/</code> - Retrieve details of a specific crop.</li>
            <li><code>PUT /crops/<crop_id>/</code> - Update crop details (e.g., changing growth stage or adding a picture).</li>
            <li><code>DELETE /crops/<crop_id>/</code> - Delete a crop record.</li>
        </ul>

        <h3>Crop Tracking</h3>
        <ul>
            <li><code>POST /crops/<crop_id>/track/</code> - Log tracking activity (e.g., irrigation, pest control).</li>
            <li><code>GET /crops/<crop_id>/track/</code> - View the full tracking log of a specific crop.</li>
        </ul>

        <h3>Crop Care</h3>
        <ul>
            <li><code>POST /crops/<crop_id>/care/</code> - Log a crop care activity (e.g., watering, fertilization).</li>
            <li><code>GET /crops/<crop_id>/care/</code> - Retrieve care activity logs for a specific crop.</li>
        </ul>

        <h3>Land Management</h3>
        <ul>
            <li><code>POST /lands/</code> - Create a new farmland record (location, size, crops).</li>
            <li><code>GET /lands/</code> - Retrieve a list of all registered lands.</li>
            <li><code>GET /lands/<land_id>/</code> - Retrieve details of a specific farmland.</li>
            <li><code>PUT /lands/<land_id>/</code> - Update farmland details.</li>
            <li><code>DELETE /lands/<land_id>/</code> - Delete a farmland record.</li>
        </ul>

        <h3>Marketplace</h3>
        <ul>
            <li><code>POST /marketplace/</code> - Create a crop listing for sale.</li>
            <li><code>GET /marketplace/</code> - View all crop listings (with filtering options based on crop type, price, location, etc.).</li>
            <li><code>GET /marketplace/<listing_id>/</code> - View details of a specific crop listing.</li>
            <li><code>POST /marketplace/<listing_id>/purchase/</code> - Purchase a crop from the listing.</li>
        </ul>

        <h3>Transactions</h3>
        <ul>
            <li><code>GET /transactions/</code> - View all transactions for the logged-in user, including completed and pending transactions.</li>
        </ul>

        <h2>Models Overview</h2>
        <ul>
            <li><strong>User</strong>: Handles user roles (<strong>Farmer/Buyer</strong>) and includes fields for <code>address</code> and <code>phone number</code>.</li>
            <li><strong>Crop</strong>: Represents crops with attributes like <code>name</code>, <code>growth stage</code>, <code>health status</code>, <code>picture</code>, and <code>farmer</code>.</li>
            <li><strong>CropTrackingLog</strong>: Records monitoring and supervision activities for crops.</li>
            <li><strong>CropCareLog</strong>: Tracks care activities for crops.</li>
            <li><strong>Land</strong>: Represents farmland with details like <code>location</code>, <code>size</code>, and <code>crops</code>.</li>
            <li><strong>Listing</strong>: Manages crop sale listings in the marketplace, with details such as <code>crop type</code>, <code>price</code>, and <code>farmer</code>.</li>
            <li><strong>Transaction</strong>: Tracks crop purchases between farmers and buyers, including transaction details such as <code>quantity</code> and <code>date</code>.</li>
        </ul>

        <h2>Tools and Libraries to Use</h2>
        <h3>Backend Framework</h3>
        <ul>
            <li><strong>Django</strong>: For building the web application.</li>
            <li><strong>Django REST Framework (DRF)</strong>: To build RESTful API endpoints efficiently.</li>
        </ul>

        <h3>Authentication</h3>
        <ul>
            <li><strong>Django REST Framework JWT</strong>: For handling user authentication via tokens.</li>
        </ul>

        <h3>Database</h3>
        <ul>
            <li><strong>PostgreSQL</strong>: For production environments.</li>
        </ul>

        <h3>Development Tools</h3>
        <ul>
            <li><strong>Git & GitHub</strong>: For version control and collaboration.</li>
            <li><strong>Postman</strong>: For API testing and documentation.</li>
        </ul>

        <h3>Additional Libraries</h3>
        <ul>
            <li><strong>Django-filter</strong>: To implement filtering for crop listings and search.</li>
            <li><strong>Django-environ</strong>: For environment variable management.</li>
            <li><strong>Celery</strong>: For task scheduling and notifications, such as sending reminders for crop care activities.</li>
        </ul>
    </div>

    <div class="author">
        <h2>Author</h2>
        <p>Project developed by <strong>Prince</strong> as part of the Farmatta initiative to bridge the gap in the agricultural supply chain and empower farmers in Nigeria and beyond.</p>
    </div>

    <div class="footer">
        <p>&copy; 2024 Farmatta API Documentation. All rights reserved.</p>
    </div>

</body>
</html>

