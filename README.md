# SMSuela

Web application to send SMS to multiple phone numbers with Twilio.

## Usage

**Twilio active account required**

You need to generate your Twilio credentials in the `common.py` file
or in your `ENV_VARS`, also you need a `SECRET_KEY` for your project.

Install all the requirements with:
```
pip install -r requirements.txt
```

Run migrations into your database:
```
python manange.py migrate
```

Finally run the application with:
```
python manage.py runserver
```

It is necessary to use Python2.7 or above.

## Purpose

This entire application was created in order to inform people who live
in areas with poor connection around Venezuela 🇻🇪.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details