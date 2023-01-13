from flask_sqlalchemy import SQLAlchemy

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


db = SQLAlchemy()

# helper function for adding prefix to foreign key column references in production
def add_prefix_for_prod(attr):
    if environment == "production":
      # making connection between 2 tables using foreign key, specifically when in production environment
        return f"{SCHEMA}.{attr}"    
    else:
        return attr