# Distributed-Healthcare-System
This is a project for the COMP5504: Distributed Systems course. The project aims to provide practical experience in the different aspects covered in this course.

**Product Name:** Distributed Healthcare Communication System

**Version:** 1.0

**Introduction:**

Effective communication and seamless data exchange are key components of efficient healthcare delivery, as they ensure rapid decision-making, coordinated care, and optimal patient outcomes. However, in many healthcare organizations, old technologies frequently fail to match the expectations of modern healthcare environments, resulting in fragmented communication channels and a limited ability to share critical patient information between departments and hospitals. As a result, healthcare personnel struggle to acquire accurate and pertinent data, potentially resulting in treatment delays, compromised patient safety, and insufficient service delivery. To solve these issues, this project proposes implementing a distributed healthcare system using Python programming language that improves communication, teamwork, and data sharing among healthcare companies. The distributed healthcare system aims to transform healthcare communication practices by utilizing new technologies and placing security and efficiency first, ultimately enhancing patient care delivery and outcomes.


**Installation Instructions:**

**1. Server Side:**

·         Ensure Python 3.x is installed on the server machine.

·   Install Flask framework and cryptography library using pip: pip install Flask  cryptography

·         Copy the server-side script to the desired location on the server.

·         Run the server-side script using the following command: python server_side.py

**2. Client Side:**

·         Ensure Python 3.x is installed on the client machine.

·         Install the required libraries using pip: pip install requests cryptography

·         Copy the client-side script to the desired location on the client machine.

·         Run the client-side script using the following command: python client_side.py




**User Guide:**

**1. Listing Files:**

·         Upon running the client-side script, choose option 1 to list files available on the server.

·      The system will display the available files along with their priorities (low, medium, high).

**2. Downloading Files:**

·         Choose option 2 from the menu and enter the filename you wish to download.

·         The file will be downloaded from the server and decrypted automatically.

·         Decrypted files will be saved in the 'downloads_files' directory.

**3. Uploading Files:**

·         Select option 3 from the menu to upload a file.

·         Enter the filename, content, and priority level (low, medium, high) as prompted.

·        The file will be encrypted, uploaded to both the primary and backup servers, and stored securely.

**Troubleshooting:**

**1. Server Side:**

·    Ensure that Python 3.x, Flask framework, and cryptography library are installed correctly.

·    Check that ports 5000 and 5001 are not blocked by any firewall or antivirus software.

·        Verify that the 'uploads' and 'uploads_backup' directories have appropriate permissions.

**2. Client Side:**

·         Make sure Python 3.x, requests, and cryptography libraries are installed properly.

·         Ensure that the client-side script is pointing to the correct server URLs.

·         Check internet connectivity and firewall settings on the client machine.

