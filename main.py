from website import create_app  

app = create_app()

if __name__ == '__main__':
    #runs our app and starts the web
    app.run(debug=True)

