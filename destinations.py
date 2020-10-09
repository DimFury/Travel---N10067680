from flask import Blueprint, render_template, url_for, redirect, request
from .models import Destination, Comment
from Travel.forms import DestinationForm, CommentForm

from datetime import datetime




#create blueprint
bp = Blueprint('destination', __name__, url_prefix='/destinations')

@bp.route('/<id>')
def show(id):
    destination = get_destination()
    comment_form = CommentForm()
    return render_template('destinations/show.html', destination=destination, form=comment_form)

@bp.route('/<id>/comment', methods=['GET', 'POST'])
def comment(id):
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
      print('Comment form is valid. The Comment Was {comment_form.comment.data}')
    else:
      print('Comment form is invalid')

    return redirect(url_for('destination.show', id=id))


def get_destination():
  b_desc= """Brazil is considered an advanced emerging economy.
    It has the ninth largest GDP in the world by nominal, and eight by PPP measures. 
    It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""

  image_loc='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
  destination = Destination('Brazil',b_desc,image_loc,'10 R$')


  comment = Comment("User1", "Visited during the olympics, was great",'2019-11-12 11:00:00')
  comment2 = Comment("User2", "Visited during the olympics, was great",'2019-11-13 11:00:00')

  destination.set_comments(comment)
  destination.set_comments(comment2)
  
  return destination



@bp.route('/create', methods=['GET', 'POST'])
def create():
  destination_form_instance = DestinationForm()
  if destination_form_instance.validate_on_submit():
    print('form is valid')
    return redirect(url_for('destination.create'))
  else:
    print('form is not valid')

  return render_template('destinations/create.html', form=destination_form_instance) 

