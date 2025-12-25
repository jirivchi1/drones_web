"""
Test email configuration
Run this script to verify that your email setup is working correctly
"""
from app import create_app
from app.services import send_contact_email

def test_email_config():
    """Test email configuration by sending a test email"""
    app = create_app()

    with app.app_context():
        print("\n" + "="*60)
        print("EMAIL CONFIGURATION TEST")
        print("="*60)

        # Display current configuration
        print("\nCurrent Email Configuration:")
        print(f"  MAIL_SERVER: {app.config.get('MAIL_SERVER')}")
        print(f"  MAIL_PORT: {app.config.get('MAIL_PORT')}")
        print(f"  MAIL_USE_TLS: {app.config.get('MAIL_USE_TLS')}")
        print(f"  MAIL_USERNAME: {app.config.get('MAIL_USERNAME')}")
        print(f"  MAIL_DEFAULT_SENDER: {app.config.get('MAIL_DEFAULT_SENDER')}")
        print(f"  ADMIN_EMAIL: {app.config.get('ADMIN_EMAIL')}")

        # Check if email is configured
        if not app.config.get('MAIL_USERNAME') or app.config.get('MAIL_USERNAME') == 'your-email@gmail.com':
            print("\n" + "!"*60)
            print("WARNING: Email is not configured!")
            print("!"*60)
            print("\nPlease configure your email settings in the .env file:")
            print("  1. Set MAIL_USERNAME to your email address")
            print("  2. Set MAIL_PASSWORD to your app password")
            print("  3. Set ADMIN_EMAIL to where you want to receive notifications")
            print("\nFor detailed instructions, see: docs/EMAIL_SETUP.md")
            print("="*60 + "\n")
            return

        # Ask user if they want to send a test email
        print("\n" + "-"*60)
        response = input("\nDo you want to send a test email? (yes/no): ").strip().lower()

        if response not in ['yes', 'y', 'si', 's']:
            print("\nTest cancelled.")
            print("="*60 + "\n")
            return

        # Prepare test contact data
        test_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '123456789',
            'message': 'This is a test message to verify that the email configuration is working correctly.',
            'service_types': ['Bodas', 'Naturaleza']
        }

        print("\nSending test email...")
        print(f"  From: {app.config.get('MAIL_DEFAULT_SENDER')}")
        print(f"  To: {app.config.get('ADMIN_EMAIL')}")
        print(f"  Subject: Nuevo mensaje de contacto - {test_data['name']}")

        # Send test email
        success = send_contact_email(test_data)

        print("\n" + "-"*60)
        if success:
            print("\nSUCCESS: Test email sent successfully!")
            print(f"\nCheck your inbox at: {app.config.get('ADMIN_EMAIL')}")
            print("(Don't forget to check spam folder)")
        else:
            print("\nERROR: Failed to send test email.")
            print("\nPossible issues:")
            print("  1. Incorrect email credentials in .env file")
            print("  2. Two-step verification not enabled (for Gmail)")
            print("  3. App password not generated (for Gmail)")
            print("  4. SMTP server or port incorrect")
            print("  5. Network/firewall blocking SMTP")
            print("\nCheck logs/app.log for detailed error messages")
            print("\nFor setup instructions, see: docs/EMAIL_SETUP.md")

        print("="*60 + "\n")


if __name__ == '__main__':
    test_email_config()
