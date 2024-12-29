
<h1 style="font-family: Arial, sans-serif; text-align: center; background-color: #00796b; color: white; padding: 10px 0;">Farmatta API - Project Documentation</h1>

<h2 style="font-family: Arial, sans-serif; color: #00796b;">Project Description</h2>
<p style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0 20px;">Farmatta API is a RESTful platform designed to connect farmers specializing in cash crops like rice, yam, and cassava with buyers, suppliers, and agricultural resources. This platform bridges the gap in the agricultural supply chain by offering tools for crop management, marketplace operations, transaction tracking, and land management. The API provides a comprehensive solution for farmers to manage their crops, land, and farming activities and engage with buyers and suppliers efficiently and transparently.</p>

<h2 style="font-family: Arial, sans-serif; color: #00796b;">Core Features and Functionality</h2>
<ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
    <li><strong>Farmer Registration and Authentication</strong>:
        <ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
            <li>Users can sign up and log in using email and password.</li>
            <li>Farmers can manage their profiles, including personal details such as <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">address</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">phone number</code>, and farm locations.</li>
            <li>The system will distinguish between <strong>Farmers</strong> and <strong>Buyers</strong> during registration.</li>
        </ul>
    </li>
    <li><strong>Cash Crop Management</strong>:
        <ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
            <li>Farmers can list cash crops for sale, update crop details, and manage crop inventory.</li>
            <li>Crop types include <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">rice</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">yam</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">cassava</code>, and other regional crops.</li>
            <li>Each crop can have a <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">picture</code> uploaded to provide better visualization for buyers.</li>
        </ul>
    </li>
    <li><strong>Crop Care Management</strong>:
        <ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
            <li>Track and manage crop care activities, including watering schedules, pest control, and fertilization.</li>
            <li>Record growth stages of crops (e.g., <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">germination</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">flowering</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">harvesting</code>).</li>
        </ul>
    </li>
    <li><strong>Marketplace for Crops</strong>:
        <ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
            <li>Farmers can list crops and services for sale.</li>
            <li>Buyers can search, filter, and view available crop listings.</li>
            <li>Buyers can view detailed crop listings, including crop pictures, quantity, and price.</li>
        </ul>
    </li>
    <li><strong>Transaction History</strong>:
        <ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
            <li>Track transactions between farmers and buyers.</li>
            <li>View completed and pending transaction details for both farmers and buyers.</li>
        </ul>
    </li>
    <li><strong>Land Management</strong>:
        <ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
            <li>Farmers can record land plot details, including <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">location</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">size</code>, and <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">allocated crops</code>.</li>
            <li>Track soil health metrics such as <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">pH levels</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">moisture</code>, and <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">nutrients</code>.</li>
        </ul>
    </li>
    <li><strong>Location-Based Search</strong>:
        <ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
            <li>Match farmers with buyers and suppliers based on geographical proximity.</li>
        </ul>
    </li>
</ul>

<h2 style="font-family: Arial, sans-serif; color: #00796b;">API Endpoints Overview</h2>

<h3 style="font-family: Arial, sans-serif; color: #00796b;">Authentication</h3>
<ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
    <li><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">POST /auth/register</code> - Registers users as either <strong>Farmers</strong> or <strong>Buyers</strong> with <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">address</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">phone number</code>, and other relevant details.</li>
    <li><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">POST /auth/login</code> - Logs users in and returns an authentication token.</li>
</ul>

<h3 style="font-family: Arial, sans-serif; color: #00796b;">Crop Management</h3>
<ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
    <li><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">POST /crops/</code> - Create a new crop record (including <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">name</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">growth stage</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">health status</code>, and <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">picture</code>).</li>
    <li><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">GET /crops/</code> - List all crops (with filtering options such as <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">type</code>, <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">growth stage</code>, etc.).</li>
</ul>

<h3 style="font-family: Arial, sans-serif; color: #00796b;">Marketplace & Transactions</h3>
<ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
    <li><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">POST /marketplace/</code> - List crops for sale with price and quantity.</li>
    <li><code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">GET /marketplace/</code> - View crop listings for sale with filtering options.</li>
</ul>

<h2 style="font-family: Arial, sans-serif; color: #00796b;">Setup Instructions</h2>
<p style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0 20px;">Follow the steps below to set up the Farmatta API project:</p>
<ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
    <li><strong>Step 1: Clone the repository</strong>
        <p style="font-family: Arial, sans-serif; line-height: 1.6;">Clone the project repository to your local machine using the following command:</p>
        <pre style="background-color: #f1f1f1; padding: 10px; border-radius: 3px;">git clone https://github.com/ochogwuprince92/farmatta-api.git</pre>
    </li>
    <li><strong>Step 2: Install dependencies</strong>
        <p style="font-family: Arial, sans-serif; line-height: 1.6;">Navigate to the project directory and install the required dependencies using <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">pip</code>:</p>
        <pre style="background-color: #f1f1f1; padding: 10px; border-radius: 3px;">pip install -r requirements.txt</pre>
    </li>
    <li><strong>Step 3: Configure environment variables</strong>
        <p style="font-family: Arial, sans-serif; line-height: 1.6;">Create a <code style="background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px;">.env</code> file in the project root directory and add your environment variables (e.g., database credentials, API keys).</p>
    </li>
    <li><strong>Step 4: Migrate the database</strong>
        <p style="font-family: Arial, sans-serif; line-height: 1.6;">Run the following command to apply database migrations:</p>
        <pre style="background-color: #f1f1f1; padding: 10px; border-radius: 3px;">python manage.py migrate</pre>
    </li>
    <li><strong>Step 5: Run the server</strong>
        <p style="font-family: Arial, sans-serif; line-height: 1.6;">Start the development server using:</p>
        <pre style="background-color: #f1f1f1; padding: 10px; border-radius: 3px;">python manage.py runserver</pre>
    </li>
</ul>

<h2 style="font-family: Arial, sans-serif; color: #00796b;">Security Considerations</h2>
<p style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0 20px;">Ensure sensitive information, such as authentication tokens, is transmitted over HTTPS. Use appropriate access controls and permissions to restrict sensitive data based on user roles (e.g., Farmer, Buyer).</p>

<h2 style="font-family: Arial, sans-serif; color: #00796b;">Future Enhancements</h2>
<ul style="font-family: Arial, sans-serif; margin-left: 20px; padding-left: 0;">
    <li>Integrate real-time notifications for crop care reminders and transactions.</li>
    <li>Provide farm equipment listing and rental functionalities.</li>
</ul>

<p style="font-family: Arial, sans-serif; text-align: center; font-size: 12px; color: #00796b; margin: 20px 0;">Authored by Ochogwu Prince<br>&copy; 2024 Farmatta - All Rights Reserved</p>
