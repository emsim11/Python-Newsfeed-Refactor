# `python Seeds.py`

from App.Models import User
from App.Database import Session, Base, Engine

# Drop And Rebuild Tables
Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)

# Establish Temporary Session Connection
Database = Session()

# Insert Users
Database.add_all([
    User(Username='testuser', Email='testing@example.com', Password='Password123456')
])

# Run The Insert Statements
Database.commit()

# Close The Session Connection
Database.close()