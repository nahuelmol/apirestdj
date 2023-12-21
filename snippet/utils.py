from django.conf import settings
import jwt

def generate_access_token(user):

	try:
		payload = {
			'user_id':user.id,
		}

		access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
		return access_token

	except Exception as e:
		errmessage = 'the access token was not created'
		return errmessage

	