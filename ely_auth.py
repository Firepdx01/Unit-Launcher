from flask import Flask, redirect, request, session
import requests
import secrets
import webbrowser

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Needed for session management

# === Ely.by OAuth2 configuration ===
ELY_CLIENT_ID = 'YOUR_CLIENT_ID_HERE'
ELY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET_HERE'
ELY_REDIRECT_URI = 'http://localhost:5000/callback'

ELY_AUTH_URL = 'https://account.ely.by/oauth2/v1/authorize'
ELY_TOKEN_URL = 'https://account.ely.by/oauth2/v1/token'
ELY_USER_INFO_URL = 'https://account.ely.by/api/profile'

@app.route('/')
def index():
    oauth_state = secrets.token_urlsafe(16)
    session['oauth_state'] = oauth_state

    params = {
        'client_id': ELY_CLIENT_ID,
        'redirect_uri': ELY_REDIRECT_URI,
        'response_type': 'code',
        'scope': 'account_info',
        'state': oauth_state
    }

    auth_url = f"{ELY_AUTH_URL}?{requests.compat.urlencode(params)}"
    webbrowser.open(auth_url)
    return 'Opening browser for Ely.by login...'

@app.route('/callback')
def callback():
    if request.args.get('state') != session.get('oauth_state'):
        return 'State mismatch!', 400

    code = request.args.get('code')
    if not code:
        return 'Missing authorization code!', 400

    # Exchange code for access token
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': ELY_REDIRECT_URI,
        'client_id': ELY_CLIENT_ID,
        'client_secret': ELY_CLIENT_SECRET
    }

    token_response = requests.post(ELY_TOKEN_URL, data=token_data)
    if token_response.status_code != 200:
        return f"Token request failed: {token_response.text}", 400

    token_json = token_response.json()
    access_token = token_json.get('access_token')

    # Fetch user info
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get(ELY_USER_INFO_URL, headers=headers)

    if user_response.status_code != 200:
        return f"User info fetch failed: {user_response.text}", 400

    user_info = user_response.json()
    username = user_info.get('username')
    uuid = user_info.get('id')

    return f'Logged in as {username} (UUID: {uuid})'

if __name__ == '__main__':
    app.run(debug=True)
