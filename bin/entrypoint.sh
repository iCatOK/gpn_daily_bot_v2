#!/bin/sh

alembic upgrade head

if [ -z "$WEBHOOK_PATH" ]
then
      python app.py
else
      python webhook.py
fi