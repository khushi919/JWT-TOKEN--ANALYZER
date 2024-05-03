
# JWT Token Analyzer

A simple Python script to analyze JSON Web Tokens (JWT), decode token information, and verify token signatures.

## Features

- Decodes and inspects JWT tokens.
- Verifies token signature using a provided secret key.
- Checks token expiration time and issued-at time (iat).
- Displays custom claims extracted from the token payload.

## Prerequisites

- Python 3.x installed on your system.
  
## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/khushi919/JWT-TOKEN--ANALYZER.git
   ```
   
2. **Navigate to the Project Directory**

   ```bash
   cd JWT-TOKEN--ANALYZER
   ```
   
3. **Install Required Python Packages**

   ```bash
   pip install -r requirements.txt
   ```
   

## Usage

4. **Run the Script**

   Execute the script with Python and follow the prompts:

   ```bash
   python3 token_analyzer.py
   ```

5. **Input a JWT Token**

   Enter a valid JWT token when prompted:

   ```plaintext
   🔐 JWT Token Analyzer
   Enter JWT token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkRvZSIsImlhdCI6MTYyMTI4OTIyMX0.YAvpV5Xzf2bt9lB70tqsYis2Go5ZyZcj86joFbw8vYg
   ```

6. **Provide Secret Key (if applicable)**

   Optionally, provide a secret key to verify the token signature. Press Enter if no secret key is required.

   ```plaintext
   Enter secret key (press Enter if no secret key is required):
   ```

7. **Review Token Information**

   The tool will decode the token, display its contents, and verify the signature if a secret key is provided.

   Example output:
   ```plaintext
   Token Information:
   sub: 1234567890
   name: Doe
   iat: 1621289221
   ✅ Token signature verified successfully.
   🕒 Token issued at: 2021-05-18 14:27:01

   Do you want to analyze another token? (yes/no): no
   Exiting...
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
