from website import create_app # since website is a Python package, everything auto runs in its __init_ file

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)