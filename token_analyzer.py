import jwt
from datetime import datetime

def analyze_jwt_token(token, secret_key=None):
    try:
        # Validate token format
        if token.count(".") != 2:
            raise ValueError("Invalid JWT token format: Expected three parts separated by dots.")

        # Decode the JWT token
        decoded_token = jwt.decode(token, options={'verify_signature': False})

        # Print decoded token information
        print("\nToken Information:")
        for key, value in decoded_token.items():
            print(f"{key}: {value}")

        # Verify token signature if a secret key is provided
        if secret_key:
            decoded_token = jwt.decode(token, key=secret_key, algorithms=['HS256'], options={'verify_signature': True})
            print("✅ Token signature verified successfully.")

        # Check token expiration
        if "exp" in decoded_token:
            expiration_time = datetime.utcfromtimestamp(decoded_token["exp"])
            current_time = datetime.utcnow()
            if current_time > expiration_time:
                print("⚠ Warning: Token has expired!")
            else:
                time_remaining = expiration_time - current_time
                print(f"ℹ Token expires in: {time_remaining}")

        # Check issued at time (iat)
        if "iat" in decoded_token:
            issued_at_time = datetime.utcfromtimestamp(decoded_token["iat"])
            print(f"🕒 Token issued at: {issued_at_time}")

        # Extract and display custom claims (non-standard claims)
        custom_claims = {key: value for key, value in decoded_token.items() if key not in ["exp", "iat"]}
        if custom_claims:
            print("\nCustom Claims:")
            for key, value in custom_claims.items():
                print(f"{key}: {value}")

    except jwt.exceptions.DecodeError:
        print("❌ Error: Invalid JWT token format or signature.")

    except jwt.exceptions.ExpiredSignatureError:
        print("⚠ Warning: Token has expired.")

    except jwt.InvalidTokenError:
        print("❌ Error: Invalid JWT token or signature.")

    except ValueError as ve:
        print(f"❌ Error: {ve}")

if __name__ == "__main__":
    # Prompt the user to enter a JWT token and secret key
    print("🔐 JWT Token Analyzer")
    sample_jwt_token = input("Enter JWT token: ")
    secret_key = input("Enter secret key (press Enter if no secret key is required): ")

    # Analyze the JWT token
    analyze_jwt_token(sample_jwt_token, secret_key)
