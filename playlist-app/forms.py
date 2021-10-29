"""Forms for playlist app."""

from wtforms import validators, StringField, SelectField, TextAreaField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    name = StringField('name',validators=[validators.DataRequired()])
    description = TextAreaField('description')


class SongForm(FlaskForm):

    title= StringField('title',validators=[validators.DataRequired()])
    artist= StringField('artist',validators=[validators.DataRequired()])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
