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
  <li><b>requirements.txt</b> - The list of required packages.</li><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farmatta API - Project Documentation</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #f4f4f4; color: #333;">
    <header style="background-color: #00796b; color: white; padding: 10px 0; text-align: center;">
        <h1 style="color: white;">Farmatta API - Project Documentation</h1>
    </header>

    <div class="content" style="padding: 20px;">
        <h2 style="color: #00796b;">Project Description</h2>
        <p>Farmatta API is a RESTful platform designed to connect farmers specializing in cash crops like rice, yam, and cassava with buyers, suppliers, and agricultural resources. This platform bridges the gap in the agricultural supply chain by offering tools for crop management, marketplace operations, transaction tracking, and land management. The API provides a comprehensive solution for farmers to manage their crops, land, and farming activities and engage with buyers and suppliers efficiently and transparently.</p>

        <h2 style="color: #00796b;">Core Features and Functionality</h2>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin: 5px 0;"><strong>Farmer Registration and Authentication</strong>: 
                <ul style="list-style-type: none; padding: 0;">
                    <li style="margin: 5px 0;">Users can sign up and log in using email and password.</li>
                    <li style="margin: 5px 0;">Farmers can manage their profiles, including personal details such as <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">address</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">phone number</code>, and farm locations.</li>
                    <li style="margin: 5px 0;">The system will distinguish between <strong>Farmers</strong> and <strong>Buyers</strong> during registration.</li>
                </ul>
            </li>
            <li style="margin: 5px 0;"><strong>Cash Crop Management</strong>: 
                <ul style="list-style-type: none; padding: 0;">
                    <li style="margin: 5px 0;">Farmers can list cash crops for sale, update crop details, and manage crop inventory.</li>
                    <li style="margin: 5px 0;">Crop types include <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">rice</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">yam</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">cassava</code>, and other regional crops.</li>
                    <li style="margin: 5px 0;">Each crop can have a <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">picture</code> uploaded to provide better visualization for buyers.</li>
                </ul>
            </li>
            <li style="margin: 5px 0;"><strong>Crop Care Management</strong>: 
                <ul style="list-style-type: none; padding: 0;">
                    <li style="margin: 5px 0;">Track and manage crop care activities, including watering schedules, pest control, and fertilization.</li>
                    <li style="margin: 5px 0;">Record growth stages of crops (e.g., <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">germination</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">flowering</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">harvesting</code>).</li>
                </ul>
            </li>
            <li style="margin: 5px 0;"><strong>Marketplace for Crops</strong>: 
                <ul style="list-style-type: none; padding: 0;">
                    <li style="margin: 5px 0;">Farmers can list crops and services for sale.</li>
                    <li style="margin: 5px 0;">Buyers can search, filter, and view available crop listings.</li>
                    <li style="margin: 5px 0;">Buyers can view detailed crop listings, including crop pictures, quantity, and price.</li>
                </ul>
            </li>
            <li style="margin: 5px 0;"><strong>Transaction History</strong>: 
                <ul style="list-style-type: none; padding: 0;">
                    <li style="margin: 5px 0;">Track transactions between farmers and buyers.</li>
                    <li style="margin: 5px 0;">View completed and pending transaction details for both farmers and buyers.</li>
                </ul>
            </li>
            <li style="margin: 5px 0;"><strong>Land Management</strong>: 
                <ul style="list-style-type: none; padding: 0;">
                    <li style="margin: 5px 0;">Farmers can record land plot details, including <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">location</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">size</code>, and <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">crops</code>.</li>
                    <li style="margin: 5px 0;">Track soil health metrics such as <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">pH levels</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">moisture</code>, and <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">nutrients</code>.</li>
                </ul>
            </li>
            <li style="margin: 5px 0;"><strong>Location-Based Search</strong>: 
                <ul style="list-style-type: none; padding: 0;">
                    <li style="margin: 5px 0;">Match farmers with buyers and suppliers based on geographical proximity.</li>
                </ul>
            </li>
        </ul>

        <h2 style="color: #00796b;">API Endpoints Overview</h2>
        <h3 style="color: #00796b;">Authentication</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin: 5px 0;"><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">POST /auth/register</code> - Registers users as either <strong>Farmers</strong> or <strong>Buyers</strong> with <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">address</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">phone number</code>, and other relevant details.</li>
            <li style="margin: 5px 0;"><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">POST /auth/login</code> - Logs users in and returns an authentication token.</li>
        </ul>

        <h3 style="color: #00796b;">Crop Management</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin: 5px 0;"><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">POST /crops/</code> - Create a new crop record (including <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">name</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">growth stage</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">health status</code>, and <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">picture</code>).</li>
            <li style="margin: 5px 0;"><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">GET /crops/</code> - Retrieve a list of crops (available for buyers and farmers).</li>
            <li style="margin: 5px 0;"><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">GET /crops/<crop_id>/</code> - Retrieve details of a specific crop.</li>
            <li style="margin: 5px 0;"><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">PUT /crops/<crop_id>/</code> - Update crop details (e.g., changing growth stage or adding a picture).</li>
            <li style="margin: 5px 0;"><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">DELETE /crops/<crop_id>/</code> - Delete a crop record.</li>
        </ul>
    </div>

    <footer style="text-align: center; margin-top: 20px; padding: 10px 0; background-color: #00796b; color: white;">
        <p>&copy; 2024 Farmatta. All rights reserved.</p>
    </footer>
</body>
</html>

</ul>

<h2 style="font-size: 20px;">Additional Information</h2>
<p style="font-size: 16px;">You can find the project repository here: <a href="https://github.com/ochogwuprince92/Farmatta" target="_blank">Farmatta GitHub Repository</a>.</p>

<h2 style="font-size: 20px;">Author</h2>
<p style="font-size: 16px;">This project is authored by <b>Ochogwu Prince</b>.</p>

