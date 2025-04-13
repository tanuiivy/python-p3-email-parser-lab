# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split by comma or space using regex
        split_addresses = re.split(r'[,\s]+', self.addresses)

        # Regex pattern for a valid email address
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Filter valid emails only
        valid_emails = [email for email in split_addresses if re.match(email_pattern, email)]

        # Remove duplicates and sort
        return sorted(set(valid_emails))

