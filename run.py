from blog import create_app

if __name__ == '__main__':
    create_app(config='testing').run(host='0.0.0.0', port=5000)