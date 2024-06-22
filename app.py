from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a rota para a URL raiz ('/') que aceita métodos GET e POST
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
         # Verifica se o nome de usuário e a senha estão corretos# Aqui você pode adicionar a lógica de autenticação
        if name == "admin" and password == "admin":  # Apenas um exemplo
            # Redireciona para a página do dashboard 
            return redirect(url_for('dashboard'))
        else:
             # Retorna uma mensagem de erro se as informações estiverem erradas
            return "Credenciais inválidas"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Mensagem ao acessar a página do dashboard
    return "Bem-vindo ao dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
