from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, input_required

# criando a aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'


class RegisterForm(FlaskForm):
    first_name = StringField('primeiro nome', validators=[DataRequired()])
    last_name = StringField('sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[Email(message='E-mail inválido!')])
    password = PasswordField('Senha', validators=[input_required(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirmar senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
   
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5152)