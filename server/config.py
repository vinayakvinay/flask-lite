# Development
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://vinayagaperumalmariyappan:Vinayak@0612@localhost/gp"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


# # Production
# class Config:
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://vinayagaperumalmariyappan:Vinayak@0612@localhost/gp"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     WTF_CSRF_ENABLED = True
