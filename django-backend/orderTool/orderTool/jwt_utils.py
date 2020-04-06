def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token,
        'user': {
            'username': user.username, 'id': user.id, "is_staff": user.is_staff, "full_name": user.last_name + user.first_name,
        }
    }