#!/usr/bin/env python3
"""
Script to create admin user account for Zitouna Tamkeen application
"""

import requests
import json
import sys

def create_admin_user():
    """Create admin user account via API"""
    
    # API endpoint
    api_url = "https://0vhlizc36w0g.manus.space/api/auth/signup"
    
    # Admin user data
    admin_data = {
        "username": "admin_youssef",
        "email": "youssefbenyounes69@gmail.com",
        "password": "AdminQA2025!",
        "first_name": "Youssef",
        "last_name": "Ben Younes",
        "phone": "+216 20 123 456"
    }
    
    # Headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    try:
        print("Creating admin user account...")
        print(f"Email: {admin_data['email']}")
        print(f"Username: {admin_data['username']}")
        
        # Make the request
        response = requests.post(api_url, json=admin_data, headers=headers)
        
        print(f"Response Status: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Admin user created successfully!")
            print(f"User ID: {result.get('user', {}).get('id')}")
            print(f"Token: {result.get('token', 'N/A')[:50]}...")
            
            # Now we need to manually set the user as admin in the database
            print("\n⚠️  Note: User created but needs to be set as admin in database.")
            print("The user role needs to be updated manually to 'admin' in the database.")
            
            return True
            
        else:
            print(f"❌ Failed to create user: {response.status_code}")
            try:
                error_data = response.json()
                print(f"Error: {error_data}")
            except:
                print(f"Error text: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_login():
    """Test login with the created admin account"""
    
    api_url = "https://0vhlizc36w0g.manus.space/api/auth/login"
    
    login_data = {
        "username": "youssefbenyounes69@gmail.com",
        "password": "AdminQA2025!"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        print("\nTesting login...")
        response = requests.post(api_url, json=login_data, headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Login successful!")
            print(f"User: {result.get('user', {})}")
            return True
        else:
            print(f"❌ Login failed: {response.status_code}")
            try:
                error_data = response.json()
                print(f"Error: {error_data}")
            except:
                print(f"Error text: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Login test error: {e}")
        return False

if __name__ == "__main__":
    print("=== Zitouna Tamkeen Admin User Creation ===\n")
    
    # Create admin user
    if create_admin_user():
        # Test login
        test_login()
    
    print("\n=== Process Complete ===")

