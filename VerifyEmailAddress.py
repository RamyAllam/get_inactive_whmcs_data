import re
import smtplib
import dns.resolver
from vars import smtp_timeout

'''''
This is a modified version of
https://github.com/scottbrady91/Python-Email-Verification-Script
'''''


def verify_email(from_address, address_to_verify):
	try:
		# Address used for SMTP MAIL FROM command
		from_address = from_address

		# Simple Regex for syntax checking
		# regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
		# regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
		regex = "[^@]+@[^@]+\.[^@]+"
		# Email address to verify
		address_to_verify = str(address_to_verify)

		# Syntax check
		match = re.match(regex, address_to_verify)
		if match:
			# Get domain for DNS lookup
			split_address = address_to_verify.split('@')
			domain = str(split_address[1])

			# MX record lookup
			records = dns.resolver.query(domain, 'MX')
			mx_record = records[0].exchange
			mx_record = str(mx_record)

			# SMTP lib setup (use debug level for full output)
			server = smtplib.SMTP(timeout=smtp_timeout)
			server.set_debuglevel(0)

			# SMTP Conversation
			server.connect(mx_record)
			server.helo(server.local_hostname)
			server.mail(from_address)
			code, message = server.rcpt(str(address_to_verify))
			server.quit()

			# Assume SMTP response 250 is success
			if code == 250:
				return True
			else:
				return False
	except ValueError:
		return False
	except dns.resolver.NXDOMAIN:
		return False
	except Exception as e:
		return False, e
