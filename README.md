# Bulk Email Sender with Django and Celery

## Overview

This project enables users to send bulk emails with attachments using Django's email functionality. It utilizes Celery tasks for asynchronous email sending, ensuring efficient processing of large volumes of emails.

## Features

- **Bulk Email Sending**: Send emails to multiple recipients at once.
- **Attachment Support**: Include attachments with your emails.
- **Asynchronous Processing**: Utilize Celery to handle email sending tasks asynchronously, improving performance and scalability.
- **Django Integration**: Seamlessly integrates with Django for email configuration and web application functionality.

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/parthdadhaniya/BulkEmailSender.git
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Django Settings**:

   - Update `settings.py` with your email configuration details.
   - Update `settings.py` with your celery configuration details.

4. **Start Celery Worker**:

   ```bash
   celery -A your_project worker --loglevel=info
   ```

5. **Start Django Development Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the Web Application**: Navigate to `http://localhost:8000` in your web browser.

2. **Authenticate**: Log in to the application using your credentials.

3. **Compose Email**: Create a new email, specifying recipients, subject, body, and attachments.

4. **Send Email**: Initiate the email sending process.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryproject.org/en/stable/)

## Authors

- [Parth Dadhaniya](https://github.com/parthdadhaniya)

## Contact

For any inquiries or feedback, feel free to contact [parthdadhaniya079@gmail.com](mailto:parthdadhaniya079@gmail.com).
