# from flask import Flask, render_template, request, redirect, url_for
# from flask_mail import Mail, Message
#
# app = Flask(__name__)
#
# # Email Configuration
# app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'app0intment.confirmati0n100@gmail.com'
# app.config['MAIL_PASSWORD'] = 'AppointmentConfirm101!'
#
# mail = Mail(app)
#
# # Sample data
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8", "slots": ["11:45am June 1", "12:00pm June 1"]},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound", "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"]},
# ]
#
# @app.route('/')
# def index():
#     return render_template('index.html', appointments=appointments)
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
# @app.route('/success', methods=['POST'])
# def success():
#     name = request.form['name']
#     email = request.form['email']
#     location = request.form['location']
#     slot = request.form['slot']
#
#     # Send confirmation email
#     msg = Message('Appointment Confirmation', sender='your-email@example.com', recipients=[email])
#     msg.body = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#     mail.send(msg)
#
#     return render_template('success.html', name=name, email=email, location=location, slot=slot)
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import logging
# import os.path
# import base64
# from email.mime.text import MIMEText
# import google.auth
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
#
# app = Flask(__name__)
#
# # Sample data
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8", "slots": ["11:45am June 1", "12:00pm June 1"]},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound", "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"]},
# ]
#
# # If modifying these SCOPES, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
#
# def authenticate_gmail():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES,
#                 redirect_uri='http://127.0.0.1:5000/confirm')  # specify your redirect URI
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as error:
#         print('An error occurred: %s' % error)
#         return None
#
# @app.route('/')
# def index():
#     return render_template('index.html', appointments=appointments)
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
# @app.route('/success', methods=['POST'])
# def success():
#     try:
#         name = request.form['name']
#         email = request.form['email']
#         location = request.form['location']
#         slot = request.form['slot']
#
#         service = authenticate_gmail()
#
#         sender = "your-email@gmail.com"
#         subject = "Appointment Confirmation"
#         message_text = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#         message = create_message(sender, email, subject, message_text)
#         send_message(service, "me", message)
#
#         return render_template('success.html', name=name, email=email, location=location, slot=slot)
#     except Exception as e:
#         logging.error(f"Error: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
# if __name__ == '__main__':
#     app.run(debug=True)


# # app.py
# from flask import Flask, render_template, request, redirect, url_for
# import logging
# import os.path
# import sys
# import os
# import base64
# from email.mime.text import MIMEText
# from datetime import datetime
#
# import google.auth
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
# from flask import Flask, render_template, request, redirect, url_for
# import logging
# import os.path
# import base64
# from email.mime.text import MIMEText
# import google.auth
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
# from search import perform_search
# from flask import Flask, render_template, request, redirect, url_for
# import logging
# import os
# import base64
# from email.mime.text import MIMEText
# import google.auth
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
# from search import perform_search
#
# app = Flask(__name__)
# second_project_path = os.getenv('SECOND_PROJECT_PATH')
#
#
#
# # Sample data
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8", "slots": ["11:45am June 1", "12:00pm June 1"]},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound", "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"]},
# ]
#
# # If modifying these SCOPES, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
#
# @app.route('/schedule', methods=['POST'])
# def schedule():
#     if request.method == 'POST':
#         hospital = request.form['hospital']
#         time_slot = request.form['time_slot']
#         name = request.form['name']
#         email = request.form['email']
#
#         # Basic form validation (you can expand this)
#         if not (hospital and time_slot and name and email):
#             return "All fields are required. Please go back and fill out the form."
#
#         # Store the appointment (in this example, we append to a list)
#         appointment = {
#             "hospital": hospital,
#             "time_slot": time_slot,
#             "name": name,
#             "email": email,
#             "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         }
#         appointments.append(appointment)
#
#         # Render a confirmation page or redirect as needed
#         return render_template('confirmation.html', appointment=appointment)
#
# @app.route('/search', methods=['GET'])
#
#
# def authenticate_gmail():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES,
#                 redirect_uri='http://127.0.0.1:5000/confirm')  # specify your redirect URI
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as error:
#         print('An error occurred: %s' % error)
#         return None
#
# @app.route('/index')
# def index():
#     return render_template('index.html', appointments=appointments)
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
# @app.route('/success', methods=['POST'])
# def success():
#     try:
#         name = request.form['name']
#         email = request.form['email']
#         location = request.form['location']
#         slot = request.form['slot']
#
#         service = authenticate_gmail()
#
#         sender = "your-email@gmail.com"
#         subject = "Appointment Confirmation"
#         message_text = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#         message = create_message(sender, email, subject, message_text)
#         send_message(service, "me", message)
#
#         return render_template('success.html', name=name, email=email, location=location, slot=slot)
#     except Exception as e:
#         logging.error(f"Error: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
# @app.route('/')
# def home():
#     return render_template('home.html')
#
# @app.route('/search', methods=['POST'])
# def search():
#     appointment_type = request.form['appointment_type']
#     city_province = request.form['city_province']
#     priority_number = request.form['priority_number']
#
#     # Perform the search logic from another Python file
#     search_results = perform_search(appointment_type, city_province, priority_number)
#
#     # Pass the search results to the template (if needed)
#     return render_template('index.html', appointments=appointments, search_results=search_results)
#
# # @app.route('/scan_document', methods=['POST'])
# # def scan_document():
# #     # Get the path to the second project from an environment variable
# #     second_project_path = os.getenv('SECOND_PROJECT_PATH')
# #     if second_project_path:
# #         # Run the second project dynamically
# #         os.system(f'python3 {second_project_path}')
# #         return "Scanning Document...", 200
# #     else:
# #         return "Error: SECOND_PROJECT_PATH not set.", 500
#
# @app.route('/scan_document', methods=['POST'])
# def scan_document():
#     try:
#         # Get the path to the second project from an environment variable
#         second_project_path = os.getenv('SECOND_PROJECT_PATH')
#         if second_project_path:
#             # Debugging print statements
#             logging.debug(f"SECOND_PROJECT_PATH: {second_project_path}")
#             command = f'python3 {second_project_path}'
#             logging.debug(f"Executing command: {command}")
#             # Run the second project dynamically
#             result = os.system(command)
#             if result != 0:
#                 logging.error(f"Command execution failed with exit code: {result}")
#                 return f"Error: Command execution failed with exit code: {result}", 500
#             return "Scanning Document...", 200
#         else:
#             logging.error("Error: SECOND_PROJECT_PATH not set.")
#             return "Error: SECOND_PROJECT_PATH not set.", 500
#     except Exception as e:
#         logging.error(f"An error occurred: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
# from flask import Flask, render_template, request, redirect, url_for
# import logging
# import os.path
# import base64
# from email.mime.text import MIMEText
# from datetime import datetime
# import google.auth
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
# from search import perform_search
# from geopy.geocoders import Nominatim
#
# app = Flask(__name__)
#
# # Sample data
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8", "slots": ["11:45am June 1", "12:00pm June 1"], "coordinates": (43.4712, -79.7016)},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound", "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"], "coordinates": (43.5123, -79.6857)},
# ]
#
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
#
# @app.route('/schedule', methods=['POST'])
# def schedule():
#     if request.method == 'POST':
#         hospital = request.form['hospital']
#         time_slot = request.form['time_slot']
#         name = request.form['name']
#         email = request.form['email']
#
#         if not (hospital and time_slot and name and email):
#             return "All fields are required. Please go back and fill out the form."
#
#         appointment = {
#             "hospital": hospital,
#             "time_slot": time_slot,
#             "name": name,
#             "email": email,
#             "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         }
#         appointments.append(appointment)
#
#         return render_template('confirmation.html', appointment=appointment)
#
# def authenticate_gmail():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES,
#                 redirect_uri='http://127.0.0.1:5000/confirm')
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as error:
#         print('An error occurred: %s' % error)
#         return None
#
# @app.route('/index')
# def index():
#     return render_template('index.html', appointments=appointments)
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
# @app.route('/success', methods=['POST'])
# def success():
#     try:
#         name = request.form['name']
#         email = request.form['email']
#         location = request.form['location']
#         slot = request.form['slot']
#
#         service = authenticate_gmail()
#
#         sender = "your-email@gmail.com"
#         subject = "Appointment Confirmation"
#         message_text = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#         message = create_message(sender, email, subject, message_text)
#         send_message(service, "me", message)
#
#         return render_template('success.html', name=name, email=email, location=location, slot=slot)
#     except Exception as e:
#         logging.error(f"Error: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
# @app.route('/')
# def home():
#     return render_template('home.html')
#
# @app.route('/search', methods=['POST'])
# def search():
#     address = request.form['address']
#
#     search_results = perform_search(address, appointments)
#
#     return render_template('index.html', appointments=search_results)
#
# @app.route('/scan_document', methods=['POST'])
# def scan_document():
#     try:
#         second_project_path = os.getenv('SECOND_PROJECT_PATH')
#         if second_project_path:
#             logging.debug(f"SECOND_PROJECT_PATH: {second_project_path}")
#             command = f'python3 {second_project_path}'
#             logging.debug(f"Executing command: {command}")
#             result = os.system(command)
#             if result != 0:
#                 logging.error(f"Command execution failed with exit code: {result}")
#                 return f"Error: Command execution failed with exit code: {result}", 500
#             return "Scanning Document...", 200
#         else:
#             logging.error("Error: SECOND_PROJECT_PATH not set.")
#             return "Error: SECOND_PROJECT_PATH not set.", 500
#     except Exception as e:
#         logging.error(f"An error occurred: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
# if __name__ == '__main__':
#     app.run(debug=True)

########### WORKING CODE BELOW ########


# from flask import Flask, render_template, request
# import logging
# import os
# import base64
# from email.mime.text import MIMEText
# from datetime import datetime
# import google.auth
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
# from search import perform_search
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# app = Flask(__name__)
#
# # Sample data with coordinates
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8", "slots": ["11:45am June 1", "12:00pm June 1"], "coordinates": (43.4712, -79.7016)},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound", "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"], "coordinates": (43.5123, -79.6857)},
# ]
#
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
#
# def authenticate_gmail():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as error:
#         print('An error occurred: %s' % error)
#         return None
#
# @app.route('/')
# def home():
#     return render_template('home.html')
#
# @app.route('/index')
# def index():
#     return render_template('index.html', appointments=appointments)
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
# @app.route('/success', methods=['POST'])
# def success():
#     try:
#         name = request.form['name']
#         email = request.form['email']
#         location = request.form['location']
#         slot = request.form['slot']
#
#         service = authenticate_gmail()
#         sender = "your-email@gmail.com"
#         subject = "Appointment Confirmation"
#         message_text = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#         message = create_message(sender, email, subject, message_text)
#         send_message(service, "me", message)
#
#         return render_template('success.html', name=name, email=email, location=location, slot=slot)
#     except Exception as e:
#         logging.error(f"Error: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
# @app.route('/search', methods=['POST'])
# def search():
#     appointment_type = request.form['appointment_type']
#     city_province = request.form['city_province']
#     priority_number = request.form['priority_number']
#
#     # Perform the search logic from another Python file
#     search_results = perform_search(appointment_type, city_province)
#     # Pass the search results to the template (if needed)
#     return render_template('index.html', appointments=appointments, search_results=search_results)
#
#
#     # address = request.form['address']
#     # geolocator = Nominatim(user_agent="appointment_booking")
#     # location = geolocator.geocode(address)
#     #
#     # if location:
#     #     user_coordinates = (location.latitude, location.longitude)
#     #     sorted_appointments = sorted(appointments, key=lambda x: geodesic(user_coordinates, x['coordinates']).km)
#     #     return render_template('index.html', appointments=sorted_appointments)
#     # else:
#     #     return render_template('index.html', appointments=appointments, error="Address not found.")
#
# def find_location():
#     try:
#         address = request.form['address']
#         logging.debug(f"Received address: {address}")
#
#         if not address:
#             raise ValueError("Address is required")
#
#         geolocator = Nominatim(user_agent="appointment_booking")
#         location = geolocator.geocode(address)
#
#         if location:
#             user_coordinates = (location.latitude, location.longitude)
#             logging.debug(f"User coordinates: {user_coordinates}")
#
#             sorted_appointments = sorted(appointments, key=lambda x: geodesic(user_coordinates, x['coordinates']).km)
#             return render_template('index.html', appointments=sorted_appointments)
#         else:
#             return render_template('index.html', appointments=appointments, error="Address not found.")
#     except Exception as e:
#         logging.error(f"Error in find_location: {str(e)}")
#         return render_template('index.html', appointments=appointments,
#                                error="An error occurred while processing your request.")
#
#
# @app.route('/scan_document', methods=['POST'])
# def scan_document():
#     try:
#         second_project_path = os.getenv('SECOND_PROJECT_PATH')
#         if second_project_path:
#             logging.debug(f"SECOND_PROJECT_PATH: {second_project_path}")
#             command = f'python3 {second_project_path}'
#             logging.debug(f"Executing command: {command}")
#             result = os.system(command)
#             if result != 0:
#                 logging.error(f"Command execution failed with exit code: {result}")
#                 return f"Error: Command execution failed with exit code: {result}", 500
#             return "Scanning Document...", 200
#         else:
#             logging.error("Error: SECOND_PROJECT_PATH not set.")
#             return "Error: SECOND_PROJECT_PATH not set.", 500
#     except Exception as e:
#         logging.error(f"An error occurred: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# import logging
# import os
# import base64
# from email.mime.text import MIMEText
# from datetime import datetime
# import google.auth
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# from search import perform_search
#
# app = Flask(__name__)
#
# # Sample data with coordinates
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8", "slots": ["11:45am June 1", "12:00pm June 1"], "coordinates": (43.4712, -79.7016)},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound", "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"], "coordinates": (43.5123, -79.6857)},
# ]
#
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
#
# def authenticate_gmail():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as error:
#         print('An error occurred: %s' % error)
#         return None
#
# @app.route('/')
# def home():
#     return render_template('home.html')
#
# @app.route('/index')
# def index():
#     return render_template('index.html', appointments=appointments)
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
# @app.route('/success', methods=['POST'])
# def success():
#     try:
#         name = request.form['name']
#         email = request.form['email']
#         location = request.form['location']
#         slot = request.form['slot']
#
#         service = authenticate_gmail()
#         sender = "your-email@gmail.com"
#         subject = "Appointment Confirmation"
#         message_text = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#         message = create_message(sender, email, subject, message_text)
#         send_message(service, "me", message)
#
#         return render_template('success.html', name=name, email=email, location=location, slot=slot)
#     except Exception as e:
#         logging.error(f"Error: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
# @app.route('/search', methods=['POST'])
# def search():
#     appointment_type = request.form['appointment_type']
#
#     city_province = request.form['city_province']
#     priority_number = request.form['priority_number']
#
#     # Perform the search logic from another Python file
#     search_results = perform_search(appointment_type, city_province)
#     # Pass the search results to the template (if needed)
#     return render_template('index.html', appointments=appointments, search_results=search_results)
#
# @app.route('/scan_document', methods=['POST'])
# def scan_document():
#     try:
#         second_project_path = os.getenv('SECOND_PROJECT_PATH')
#         if second_project_path:
#             logging.debug(f"SECOND_PROJECT_PATH: {second_project_path}")
#             command = f'python3 {second_project_path}'
#             logging.debug(f"Executing command: {command}")
#             result = os.system(command)
#             if result != 0:
#                 logging.error(f"Command execution failed with exit code: {result}")
#                 return f"Error: Command execution failed with exit code: {result}", 500
#             return "Scanning Document...", 200
#         else:
#             logging.error("Error: SECOND_PROJECT_PATH not set.")
#             return "Error: SECOND_PROJECT_PATH not set.", 500
#     except Exception as e:
#         logging.error(f"An error occurred: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
# if __name__ == '__main__':
#     app.run(debug=True)

#WORKNG CODEEEE


# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import logging
# import os
# import base64
# from email.mime.text import MIMEText
# from datetime import datetime
# import google.auth
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import pickle
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# from search import perform_search
# from werkzeug.utils import secure_filename
# from flask import Flask, render_template, request, jsonify
# import os
# from werkzeug.utils import secure_filename
# import pytesseract
# from PIL import Image
# import PyPDF2
# import json
# import os
# import pytesseract
# from PIL import Image
# from pdf2image import convert_from_path
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'
# app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'png', 'jpg', 'jpeg'}
#
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
#
#
# def extract_text_from_image(image_path):
#     # Use pytesseract to extract text from an image
#     try:
#         text = pytesseract.image_to_string(Image.open(image_path))
#         return text
#     except Exception as e:
#         print(f"Error extracting text from image: {e}")
#         return ""
#
#
# def extract_text_from_pdf(pdf_path):
#     # Use PyPDF2 to extract text from a PDF
#     text = ""
#     try:
#         with open(pdf_path, "rb") as file:
#             pdf = PyPDF2.PdfFileReader(file)
#             for page in range(pdf.numPages):
#                 text += pdf.getPage(page).extract_text()
#         return text
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return ""
#
#
# app.config['UPLOAD_FOLDER'] = 'Uploads'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
#
# # Ensure the upload folder exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
#
# # Sample data with coordinates
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8",
#      "slots": ["11:45am June 1", "12:00pm June 1"], "coordinates": (43.4712, -79.7016)},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound",
#      "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"],
#      "coordinates": (43.5123, -79.6857)},
# ]
#
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
#
#
# def authenticate_gmail():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as error:
#         print('An error occurred: %s' % error)
#         return None
#
#
# @app.route('/')
# def home():
#     return render_template('home.html')
#
#
# @app.route('/index')
# def index():
#     return render_template('index.html', appointments=appointments)
#
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
#
# @app.route('/success', methods=['POST'])
# def success():
#     try:
#         name = request.form['name']
#         email = request.form['email']
#         location = request.form['location']
#         slot = request.form['slot']
#
#         service = authenticate_gmail()
#         sender = "your-email@gmail.com"
#         subject = "Appointment Confirmation"
#         message_text = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#         message = create_message(sender, email, subject, message_text)
#         send_message(service, "me", message)
#
#         return render_template('success.html', name=name, email=email, location=location, slot=slot)
#     except Exception as e:
#         logging.error(f"Error: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
#
# @app.route('/search', methods=['POST'])
# def search():
#     appointment_type = request.form['appointment_type']
#     city_province = request.form['city_province']
#     priority_number = request.form['priority_number']
#
#     # Perform the search logic from another Python file
#     search_results = perform_search(appointment_type, city_province)
#     # Pass the search results to the template (if needed)
#     return render_template('index.html', appointments=appointments, search_results=search_results)
#
#
# @app.route('/scan_document', methods=['POST'])
# def scan_document():
#     try:
#         second_project_path = os.getenv('SECOND_PROJECT_PATH')
#         if second_project_path:
#             logging.debug(f"SECOND_PROJECT_PATH: {second_project_path}")
#             command = f'python3 {second_project_path}'
#             logging.debug(f"Executing command: {command}")
#             result = os.system(command)
#             if result != 0:
#                 logging.error(f"Command execution failed with exit code: {result}")
#                 return f"Error: Command execution failed with exit code: {result}", 500
#             return "Scanning Document...", 200
#         else:
#             logging.error("Error: SECOND_PROJECT_PATH not set.")
#             return "Error: SECOND_PROJECT_PATH not set.", 500
#     except Exception as e:
#         logging.error(f"An error occurred: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
#
# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
#
# poppler_path = '/opt/homebrew/bin/pdfinfo'
# images = convert_from_path('sample.pdf', poppler_path=poppler_path)
#
#
# def extract_information(file_path):
#     text = ""
#
#     # Check the file extension
#     _, file_extension = os.path.splitext(file_path)
#
#     if file_extension.lower() in ['.png', '.jpg', '.jpeg']:
#         text = pytesseract.image_to_string(Image.open(file_path))
#     elif file_extension.lower() == '.pdf':
#         try:
#             pages = convert_from_path(file_path)
#             text = "\n".join(pytesseract.image_to_string(page) for page in pages)
#         except Exception as e:
#             print(f"Error processing PDF file: {e}")
#             raise
#     else:
#         raise ValueError("Unsupported file type")
#
#     # Now parse the extracted text to find the required information
#     # This is a simple example. You'll need to adjust the logic based on your actual document's structure
#     appointment_type = "General Checkup" if "General Checkup" in text else ""
#     city_province = "Toronto, ON"  # You can use regex to find city and province from text
#     priority_number = "1"  # Use regex or string matching to find priority number
#
#     # Dummy parsing logic for demonstration
#     if "Checkup" in text:
#         appointment_type = "General Checkup"
#     if "Toronto" in text:
#         city_province = "Toronto, ON"
#     if "Priority" in text:
#         priority_number = text.split("Priority")[1].split()[0]  # Simplified parsing logic
#
#     return {
#         'appointment_type': appointment_type,
#         'city_province': city_province,
#         'priority_number': priority_number
#     }
#
#
# @app.route('/upload_file', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#
#     if file:
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
#
#         try:
#             extracted_info = extract_information(file_path)
#         except Exception as e:
#             return jsonify({'error': f'Error extracting information: {e}'}), 500
#
#         return jsonify({
#             'message': 'File uploaded successfully',
#             'appointment_type': extracted_info['appointment_type'],
#             'city_province': extracted_info['city_province'],
#             'priority_number': extracted_info['priority_number']
#         }), 200
#     else:
#         return jsonify({'error': 'File upload failed'}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
# from flask import Flask, render_template, request, jsonify
# import logging
# import os
# import base64
# from email.mime.text import MIMEText
# import pickle
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from werkzeug.utils import secure_filename
# import pytesseract
# from PIL import Image
# from pdf2image import convert_from_path
# import PyPDF2
# import json
# from search import perform_search  # Assuming this is a custom module
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'
# app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'png', 'jpg', 'jpeg'}
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
#
# # Ensure the upload folder exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
#
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
# POPPLER_PATH = '/opt/homebrew/bin/'  # Set your poppler path here
# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
#
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8",
#      "slots": ["11:45am June 1", "12:00pm June 1"], "coordinates": (43.4712, -79.7016)},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound",
#      "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"],
#      "coordinates": (43.5123, -79.6857)},
# ]
#
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
#
#
# def extract_text_from_image(image_path):
#     try:
#         text = pytesseract.image_to_string(Image.open(image_path))
#         return text
#     except Exception as e:
#         print(f"Error extracting text from image: {e}")
#         return ""
#
#
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     try:
#         with open(pdf_path, "rb") as file:
#             pdf = PyPDF2.PdfFileReader(file)
#             for page in range(pdf.numPages):
#                 text += pdf.getPage(page).extract_text()
#         return text
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return ""
#
#
# def authenticate_gmail():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as error:
#         print('An error occurred: %s' % error)
#         return None
#
#
# @app.route('/')
# def login():
#     return render_template('login.html')
#
#
# @app.route('/clinician_login')
# def clinician_login():
#     return render_template('clinician_login.html')
#
#
# @app.route('/home')
# def home():
#     return render_template('home.html')
#
#
# @app.route('/index')
# def index():
#     return render_template('index.html', appointments=appointments)
#
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
#
# @app.route('/success', methods=['POST'])
# def success():
#     try:
#         name = request.form['name']
#         email = request.form['email']
#         location = request.form['location']
#         slot = request.form['slot']
#
#         service = authenticate_gmail()
#         sender = "your-email@gmail.com"
#         subject = "Appointment Confirmation"
#         message_text = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#         message = create_message(sender, email, subject, message_text)
#         send_message(service, "me", message)
#
#         return render_template('success.html', name=name, email=email, location=location, slot=slot)
#     except Exception as e:
#         logging.error(f"Error: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
#
# @app.route('/search', methods=['POST'])
# def search():
#     appointment_type = request.form['appointment_type']
#     city_province = request.form['city_province']
#     priority_number = request.form['priority_number']
#
#     # Perform the search logic from another Python file
#     search_results = perform_search(appointment_type, city_province)
#     # Pass the search results to the template (if needed)
#     return render_template('index.html', appointments=appointments, search_results=search_results)
#
#
# @app.route('/scan_document', methods=['POST'])
# def scan_document():
#     try:
#         second_project_path = os.getenv('SECOND_PROJECT_PATH')
#         if second_project_path:
#             logging.debug(f"SECOND_PROJECT_PATH: {second_project_path}")
#             command = f'python3 {second_project_path}'
#             logging.debug(f"Executing command: {command}")
#             result = os.system(command)
#             if result != 0:
#                 logging.error(f"Command execution failed with exit code: {result}")
#                 return f"Error: Command execution failed with exit code: {result}", 500
#             return "Scanning Document...", 200
#         else:
#             logging.error("Error: SECOND_PROJECT_PATH not set.")
#             return "Error: SECOND_PROJECT_PATH not set.", 500
#     except Exception as e:
#         logging.error(f"An error occurred: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
#
# def extract_information(file_path):
#     text = ""
#     _, file_extension = os.path.splitext(file_path)
#
#     if file_extension.lower() in ['.png', '.jpg', '.jpeg']:
#         text = pytesseract.image_to_string(Image.open(file_path))
#     elif file_extension.lower() == '.pdf':
#         try:
#             pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
#             text = "\n".join(pytesseract.image_to_string(page) for page in pages)
#         except Exception as e:
#             print(f"Error processing PDF file: {e}")
#             raise
#     else:
#         raise ValueError("Unsupported file type")
#
#     appointment_type = "General Checkup" if "General Checkup" in text else ""
#     city_province = "Toronto, ON"
#     priority_number = "1"
#
#     if "Checkup" in text:
#         appointment_type = "General Checkup"
#     if "Toronto" in text:
#         city_province = "Toronto, ON"
#     if "Priority" in text:
#         priority_number = text.split("Priority")[1].split()[0]
#
#     return {
#         'appointment_type': appointment_type,
#         'city_province': city_province,
#         'priority_number': priority_number
#     }
#
#
# @app.route('/upload_file', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
#
#         try:
#             extracted_info = extract_information(file_path)
#         except Exception as e:
#             return jsonify({'error': f'Error extracting information: {e}'}), 500
#
#         return jsonify({
#             'message': 'File uploaded successfully',
#             'appointment_type': extracted_info['appointment_type'],
#             'city_province': extracted_info['city_province'],
#             'priority_number': extracted_info['priority_number']
#         }), 200
#     else:
#         return jsonify({'error': 'File upload failed'}), 500
#
#
# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
# from flask import Flask, render_template, request, jsonify
# import logging
# import os
# import base64
# from email.mime.text import MIMEText
# import pickle
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from werkzeug.utils import secure_filename
# import pytesseract
# from PIL import Image
# from pdf2image import convert_from_path
# import PyPDF2
# import json
# from search import perform_search
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'
# app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'png', 'jpg', 'jpeg'}
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
#
# # Ensure the upload folder exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
#
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
# POPPLER_PATH = '/opt/homebrew/bin/'  # Set your poppler path here
# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
#
# appointments_folder = 'appointments'
#
#
# appointments = [
#     {"location": "Oakville Trafalgar Hospital", "address": "3001 Hospital Gate, Oakville, ON L6M 0L8",
#      "slots": ["11:45am June 1", "12:00pm June 1"], "coordinates": (43.4712, -79.7016)},
#     {"location": "Ontario Diagnostic Centres X-Ray & Ultrasound",
#      "address": "2315 Bristol Cir Suite#102, Oakville, ON L6H 6P8", "slots": ["1:00pm June 1", "2:00pm June 1"],
#      "coordinates": (43.5123, -79.6857)},
# ]
#
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
#
#
# def extract_text_from_image(image_path):
#     try:
#         text = pytesseract.image_to_string(Image.open(image_path))
#         return text
#     except Exception as e:
#         print(f"Error extracting text from image: {e}")
#         return ""
#
#
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     try:
#         with open(pdf_path, "rb") as file:
#             pdf = PyPDF2.PdfFileReader(file)
#             for page in range(pdf.numPages):
#                 text += pdf.getPage(page).extract_text()
#         return text
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return ""
#
#
# def authenticate_gmail():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service
#
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as error:
#         print('An error occurred: %s' % error)
#         return None
#
#
# @app.route('/')
# def login():
#     return render_template('login.html')
#
#
# @app.route('/clinician_login')
# def clinician_login():
#     return render_template('clinician_login.html')
#
#
# @app.route('/home')
# def home():
#     return render_template('home.html')
#
#
# @app.route('/index')
# def index():
#     return render_template('index.html', appointments=appointments)
#
#
# @app.route('/confirm', methods=['POST'])
# def confirm():
#     location = request.form['location']
#     slot = request.form['slot']
#     return render_template('confirm.html', location=location, slot=slot)
#
#
# if not os.path.exists(appointments_folder):
#     os.makedirs(appointments_folder)
#
# def save_appointment(appointment):
#     file_path = os.path.join(appointments_folder, f"{appointment['name']}.json")
#     with open(file_path, 'w') as f:
#         json.dump(appointment, f)
#
# @app.route('/appointment_pending', methods=['POST'])
# def appointment_pending():
#     name = request.form['name']
#     email = request.form['email']
#     healthcare_number = request.form['healthcare_number']
#     location = request.form.get('location', 'the hospital')
#     # Here you would typically save the appointment details to a database
#     appointment = {
#         'name': name,
#         'email': email,
#         'healthcare_number': healthcare_number,
#         'location': location,
#         'file_src': 'Appointments'  # Add file_src if needed
#     }
#
#     save_appointment(appointment)
#
#     return render_template('appointment_pending.html', hospital=location)
#
#
# @app.route('/success', methods=['POST'])
# def success():
#     try:
#         name = request.form['name']
#         email = request.form['email']
#         location = request.form['location']
#         slot = request.form['slot']
#
#         service = authenticate_gmail()
#         sender = "your-email@gmail.com"
#         subject = "Appointment Confirmation"
#         message_text = f"Hello {name},\n\nYour appointment is confirmed at {location} on {slot}.\n\nThank you!"
#         message = create_message(sender, email, subject, message_text)
#         send_message(service, "me", message)
#
#         return render_template('success.html', name=name, email=email, location=location, slot=slot)
#     except Exception as e:
#         logging.error(f"Error: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
#
# @app.route('/search', methods=['POST'])
# def search():
#     appointment_type = request.form['appointment_type']
#     city_province = request.form['city_province']
#     priority_number = request.form['priority_number']
#
#     # Perform the search logic from another Python file
#     search_results = perform_search(appointment_type, city_province)
#     # Pass the search results to the template (if needed)
#     return render_template('index.html', appointments=appointments, search_results=search_results)
#
#
#
# @app.route('/scan_document', methods=['POST'])
# def scan_document():
#     try:
#         second_project_path = os.getenv('SECOND_PROJECT_PATH')
#         if second_project_path:
#             logging.debug(f"SECOND_PROJECT_PATH: {second_project_path}")
#             command = f'python3 {second_project_path}'
#             logging.debug(f"Executing command: {command}")
#             result = os.system(command)
#             if result != 0:
#                 logging.error(f"Command execution failed with exit code: {result}")
#                 return f"Error: Command execution failed with exit code: {result}", 500
#             return "Scanning Document...", 200
#         else:
#             logging.error("Error: SECOND_PROJECT_PATH not set.")
#             return "Error: SECOND_PROJECT_PATH not set.", 500
#     except Exception as e:
#         logging.error(f"An error occurred: {e}", exc_info=True)
#         return "Internal Server Error", 500
#
#
# def extract_information(file_path):
#     text = ""
#     _, file_extension = os.path.splitext(file_path)
#
#     if file_extension.lower() in ['.png', '.jpg', '.jpeg']:
#         text = pytesseract.image_to_string(Image.open(file_path))
#     elif file_extension.lower() == '.pdf':
#         try:
#             pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
#             text = "\n".join(pytesseract.image_to_string(page) for page in pages)
#         except Exception as e:
#             print(f"Error processing PDF file: {e}")
#             raise
#     else:
#         raise ValueError("Unsupported file type")
#
#     appointment_type = "General Checkup" if "General Checkup" in text else ""
#     city_province = "Toronto, ON"
#     priority_number = "1"
#
#     if "Checkup" in text:
#         appointment_type = "General Checkup"
#     if "Toronto" in text:
#         city_province = "Toronto, ON"
#     if "Priority" in text:
#         priority_number = text.split("Priority")[1].split()[0]
#
#     return {
#         'appointment_type': appointment_type,
#         'city_province': city_province,
#         'priority_number': priority_number
#     }
#
#
# @app.route('/upload_file', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
#
#         try:
#             extracted_info = extract_information(file_path)
#             appointments.append({
#                 'name': extracted_info.get('name', 'Unknown'),
#                 'email': extracted_info.get('email', 'Unknown'),
#                 'healthcare_number': extracted_info.get('healthcare_number', 'Unknown'),
#                 'file_src': file_path
#             })
#         except Exception as e:
#             return jsonify({'error': f'Error extracting information: {e}'}), 500
#
#         return jsonify({
#             'message': 'File uploaded successfully',
#             'appointment_type': extracted_info['appointment_type'],
#             'city_province': extracted_info['city_province'],
#             'priority_number': extracted_info['priority_number']
#         }), 200
#     else:
#         return jsonify({'error': 'File upload failed'}), 500
#
#
# APPROVED_APPOINTMENTS_FILE = 'approved_appointments.json'
#
#
# def save_approved_appointments(appointments):
#     with open(APPROVED_APPOINTMENTS_FILE, 'w') as f:
#         json.dump(appointments, f)
#
#
# def load_approved_appointments():
#     if not os.path.exists(APPROVED_APPOINTMENTS_FILE):
#         return []
#     with open(APPROVED_APPOINTMENTS_FILE, 'r') as f:
#         return json.load(f)
#
#
# @app.route('/dashboard')
# def dashboard():
#     approved_appointments = load_approved_appointments()
#     return render_template('dashboard.html', approved_appointments=approved_appointments)
#
#
# @app.route('/save_approved_appointments', methods=['POST'])
# def save_approved_appointments_route():
#     approved_appointments = request.json
#     save_approved_appointments(approved_appointments)
#     return '', 204
#
#
# @app.route('/load_approved_appointments', methods=['GET'])
# def load_approved_appointments_route():
#     approved_appointments = load_approved_appointments()
#     return jsonify(approved_appointments)
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)




