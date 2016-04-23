`django-longerusernameandemail` provides a migration and a monkeypatch to make the Django auth.user username and email fields longer, instead of the arbitrarily short 30 and 75 characters. It's designed to be a simple include-and-forget project that makes a little headache go away.  Enjoy, and pull requests welcome!

Note that [Django 1.5 or newer already includes support for custom `User` models][releasenotes15] (read [this tutorial][tutorial] and the [official documentation about *Substituting a custom User model*][documentation15]). So, you only need `django-longerusernameandemail` if you use an older Django version, or if you don't want to create your own User model for some reason.

Also note that:

* in Django 1.8 email length increased to [254 characters][ticket20631]
* in Django 1.10 username length increased to [150 characters][ticket20846].

[tutorial]: http://procrastinatingdev.com/django/using-configurable-user-models-in-django-1-5/
[releasenotes15]: https://docs.djangoproject.com/en/dev/releases/1.5/#configurable-user-model
[documentation15]: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#auth-custom-user
[ticket20631]: https://code.djangoproject.com/ticket/20631
[ticket20846]: https://code.djangoproject.com/ticket/20846


Usage
=====
Step 1. Install django-longerusernameandemail. 
-------------------------------------

- `pip install django-longerusernameandemail` 

You will also need to install [south]() to use the migration. 

- `pip install south` 


Step 2. Add `longerusernameandemail` to your installed apps.
-------------------------
Add 'longerusernameandemail' to the top of your `INSTALLED_APPS` in settings.py

settings.py

```python
INSTALLED_APPS = ("longerusernameandemail",) + INSTALLED_APPS
```

Step 3. (Optional) Specify a custom username length, or other settings.
-----------------------------------------------------------------------
If you want custom behavior, you can specify the following in settings.py

settings.py

```python
MAX_USERNAME_LENGTH = 100  # optional, default is 255.
MAX_EMAIL_LENGTH = 50  # optional, default is 255.
REQUIRE_UNIQUE_EMAIL = False  # optional, default is True
```



Step 4. Run the migration
------------------------------------------------
```
$ python manage.py migrate longerusernameandemail
```

That's it, you should be good to go!


Notes about the built-in forms
==============================
This app also automatically monkey patches the User forms in the Django admin to remove the 30 character limit.

It provides a suitable replacement for the standard AuthenticationForm as well, but due to the implementation you must manually utilize it.

urls.py

```python
from longerusernameandemail.forms import AuthenticationForm

urlpatterns = patterns('',
    # ...
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'authentication_form': AuthenticationForm}),
)
```

Credits
=======

The monkeypatch for this is very largely based on [celement's answer on stackoverflow][so]

[so]: http://stackoverflow.com/questions/2610088/can-djangos-auth-user-username-be-varchar75-how-could-that-be-done
