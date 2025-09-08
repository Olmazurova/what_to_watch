import click
import csv


from flask import Flask, abort, flash, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy







@app.cli.command('load_opinions')
def load_opinions_command():
    """Функция загрузки мнений в базу данных."""
    with open('../opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            opinion = Opinion(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено мнений: {counter}')

if __name__ == '__main__':
    app.run()