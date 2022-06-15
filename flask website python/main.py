from website import create_app #website is a package

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #everytime we make a change to Python code, it will automatically rerun the web server
