## Installation

First, we need to install the required package:

pip install django-oauth-toolkit


## Configuration

Next, add the following to your `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'oauth2_provider',
]


## OAuth2 Configuration with Django

**Next Step: Add `oauth2_provider` to MIDDLEWARE**

Update your `MIDDLEWARE` in `settings.py`:

```python
MIDDLEWARE = [
    ...
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

**Run Migrate**

Execute the following command to apply migrations:


Afterwards, several tables will be created to store OAuth2 applications, tokens, and related data.

**Make an OAuth2 App**

- Go to [http://localhost:8000/admin/](http://localhost:8000/admin/).
- Click on `OAUTH2_PROVIDER` and then `Applications`.
- Click `Add Application`.

Fill in the application details as follows:

- **User**: Choose the user who owns these apps (admin or user system).
- **Redirect uris**: Leave this field blank for "client credentials".
- **Client Type**: Choose the Confidential option. This means your apps need a `client_secret` to get a token.
- **Authorization Grant Type**: Choose Client credentials. This flow is used for server-to-server authentication without user intervention.
- **Name**: Name your app, for example, "Review Service".

After completing the above steps, you will see the `Client id` and `Client secret` that you have created. Make sure to copy both values.

Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' in your code with the values obtained in the previous step.

**Configuring OAuth2**

You can adjust the OAuth2 settings by adding configurations to `settings.py`. For example, you can set the token expiration, type of grant accessed, and more.

To ensure that only authenticated applications can access your API, add the `@protected_resource()` decorator to the views you want to protect.

With the steps mentioned above, you now have a working OAuth2 authentication system with Django. 
Your application can now request a token using the `client_id` and `client_secret` and use the token to access the protected API.

Each OAuth2 application you create in the Django admin panel will have a unique `client_id` and `client_secret`. 
This allows you to set different access rights and restrictions for each application.
