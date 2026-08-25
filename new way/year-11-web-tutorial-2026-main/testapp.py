from bottle import route, run, template, view, static_file
#test
@route('/')
@view('home')
def home():
    return template('home')

@route('/about')
@view('about')
def about():
    return template('about')

@route('/contact')
@view('contact')
def contact():
    return template('contact')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True )